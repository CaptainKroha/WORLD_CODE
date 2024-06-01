import spacy
from spacy.tokens import DocBin
from spacy.training import Example
from spacy.scorer import Scorer
import json
import random


def do_markup():
    nlp = spacy.blank('en')
    with open('./JSONS/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    data = data['list']

    doc_bin = DocBin()

    for item in data:
        text = item['text'].replace('\n', '\n ')
        entities = [(ann['start'], ann['end'], ann['mark']) for ann in item['annotations']]
        doc = nlp(text)
        spans = [doc.char_span(start, end, label=label) for start, end, label in entities]
        if None in spans:
            continue

        seen_tokens = set()
        valid_ents = []
        for span in sorted(spans, key=lambda span: span.start):
            token_ids = set(range(span.start, span.end))
            if not token_ids & seen_tokens:
                valid_ents.append(span)
                seen_tokens.update(token_ids)

        doc.ents = valid_ents
        doc_bin.add(doc)

    docs = list(doc_bin.get_docs(nlp.vocab))
    for doc in docs[:10]:
        print("Text: ", doc.text)
        print("Entities: ")
        for ent in doc.ents:
            print(f"  Label: {ent.label_}, Text: {ent.text}, Start: {ent.start}, End: {ent.end}\n")

    doc_bin.to_disk('./MODELv2/train.spacy')


def do_validation():
    nlp = spacy.load('ru_core_news_md')
    doc_bin = DocBin().from_disk('./MODELv2/train.spacy')
    docs = list(doc_bin.get_docs(nlp.vocab))

    for doc in docs[:5]:
        print("Text: ", doc.text)
        for ent in doc.ents:
            print("Entity:", ent.text, ent.label_)


def do_split():
    nlp = spacy.load('ru_core_news_md')
    doc_bin = DocBin().from_disk('./MODELv2/train.spacy')
    docs = list(doc_bin.get_docs(nlp.vocab))
    train_size = int(0.8 * len(docs))
    val_size = int(0.25 * train_size)
    train_data = docs[:train_size]
    val_data = docs[val_size:train_size]
    test_data = docs[train_size:]
    DocBin(docs=train_data).to_disk('./MODELv2/RES/train.spacy')
    DocBin(docs=val_data).to_disk("./MODELv2/RES/val.spacy")
    DocBin(docs=test_data).to_disk("./MODELv2/RES/test.spacy")


def train():
    nlp = spacy.blank("en")
    train_docs = list(DocBin().from_disk("./MODEL/RES/train.spacy").get_docs(nlp.vocab))
    # val_docs = DocBin().from_disk("./MODEL/RES/val.spacy").get_docs(nlp.vocab)

    # Подготовка данных для обучения
    train_examples = [
        Example.from_dict(doc, {"entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]}) for doc
        in train_docs]

    # Настройка компонента NER
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)

    labels = ["NAME", "AGE", "BIRTH_DATA", "PHONE", "EMAIL", "POS_TO", "EXP", "WPLACE",
              "WPERIOD", "WROLE", "SKILLS", "EDUCATION"]
    for label in labels:
        ner.add_label(label)

    # Обучение модели
    nlp.initialize(get_examples=lambda: train_examples)
    optimizer = nlp.create_optimizer()
    for epoch in range(10):
        losses = {}
        random.shuffle(train_examples)
        for batch in spacy.util.minibatch(train_examples, size=8):
            nlp.update(batch, drop=0.5, losses=losses, sgd=optimizer)
        print(f"Epoch {epoch}, Losses: {losses}")

    # Сохранение обученной модели
    nlp.to_disk("./MODEL/resume_ner_model")


def train_v2():
    nlp = spacy.load('ru_core_news_md')
    train_docs = list(DocBin().from_disk("./MODELv2/train.spacy").get_docs(nlp.vocab))
    # val_docs = DocBin().from_disk("./MODEL/RES/val.spacy").get_docs(nlp.vocab)
    # Подготовка данных для обучения
    train_examples = [
        Example.from_dict(doc, {"entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]}) for doc
        in train_docs]
    # for text, annotation in train_docs:
    #     train_examples.append(Example.from_dict(nlp.make_doc(text), annotation))

    # Настройка компонента NER
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
    else:
        ner = nlp.get_pipe('ner')

    labels = ["NAME", "AGE", "BIRTH_DATA", "PHONE", "EMAIL", "POS_TO", "EXP", "WPLACE",
              "WPERIOD", "WROLE", "SKILLS", "EDUCATION"]
    for label in labels:
        ner.add_label(label)

    # Обучение модели
    optimizer = nlp.resume_training()
    for i in range(10):
        for example in train_examples:
            nlp.update([example], drop=0.5, sgd=optimizer)

    # Сохранение обученной модели
    nlp.to_disk("./MODELv2/model_ru")


def make_validation():
    nlp = spacy.load("./MODEL/resume_ner_model")
    val_docs = list(DocBin().from_disk("./MODEL/RES/val.spacy").get_docs(nlp.vocab))
    scorer = Scorer()
    val_examples = [Example.from_dict(doc, {"entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]}) for doc in val_docs]

    print(scorer.score(val_examples))
 

def make_test():
    nlp = spacy.load("./MODEL/resume_ner_model")
    test_docs = DocBin().from_disk("./MODEL/RES/test.spacy").get_docs(nlp.vocab)
    test_examples = [
        Example.from_dict(doc,{"entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]}) for doc
        in test_docs]
    scorer = Scorer()
    for example in test_examples:
        pred_value = nlp(example.text)
        scorer.score(pred_value, example)
    print("Test Score:", scorer)


train_v2()

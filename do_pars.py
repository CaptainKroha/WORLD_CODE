import spacy
from resume_to_txt import select_file

nlp = spacy.load("./MODELv2/model_ru")
i_file = select_file()
with open(i_file, 'r', encoding='utf-8') as f:
    text = f.read()
doc = nlp(text)
print("Entities: ")
for ent in doc.ents:
    print(ent.text, ent.label_)


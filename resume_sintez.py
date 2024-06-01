import random
from make_json import JSONFile


def generate_cv(num):
    fio_file = './DATA/fio_file.txt'
    dob_file = './DATA/dob_file.txt'
    education_file = './DATA/education_file.txt'
    email_file = './DATA/email_file.txt'
    phone_file = './DATA/phone_file.txt'
    skils_file = './DATA/skils_file.txt'
    job_file = './DATA/job_file.txt'
    info_file = './DATA/info_file.txt'

    # Чтение данных из файлов
    fios = []
    dobs = []
    educations = []
    phones = []
    emails = []
    skils = []
    job = []
    info = []

    with open(fio_file, 'r', encoding='utf-8') as f:
        fios = [line.strip() for line in f.readlines()]
    with open(dob_file, 'r', encoding='utf-8') as f:
        dobs = [line.strip() for line in f.readlines()]
    with open(education_file, 'r', encoding='utf-8') as f:
        educations = [line.strip() for line in f.readlines()]
    with open(phone_file, 'r', encoding='utf-8') as f:
        phones = [line.strip() for line in f.readlines()]
    with open(email_file, 'r', encoding='utf-8') as f:
        emails = [line.strip() for line in f.readlines()]
    with open(skils_file, 'r', encoding='utf-8') as f:
        skils = list(set([line.strip() for line in f.readlines()]))  # преобразуем в множество, чтобы избежать повторов
    with open(job_file, 'r', encoding='utf-8') as f:
        jobs = [line.strip() for line in f.readlines()]
    with open(info_file, 'r', encoding='utf-8') as f:
        infos = [line.strip() for line in f.readlines()]

    marks = JSONFile('./JSONS/res.json')
    for j in range(num):
        output_file = f'./SINT_RESUMES/output_file{j}.txt'
        a = random.randint(3, 10)
        b = random.randint(a, 15)
        # Генерация нового файла
        with open(output_file, 'w', encoding='utf-8') as f:
            fio = random.choice(fios)
            dob = random.choice(dobs)
            education = random.choice(educations)
            phone = random.choice(phones)
            email = random.choice(emails)
            selected_skils = random.sample(skils, random.randint(a, b))
            job = random.choice(jobs)
            info = random.choice(infos)

            blocks = [
                ("EDUCATION", education),
                ("SKILLS", ", ".join(selected_skils)),
                ("JOBS", job),
                ("INFOS", info)
            ]
            random.shuffle(blocks)

            # Перемещаем основные блоки (имя, дата рождения, телефон, почта) в начало списка
            main_blocks = [("NAME", fio), ("DATE_OF_BIRTH", dob), ("PHONE", phone), ("EMAIL", email)]
            blocks = main_blocks + blocks

            text = ""
            start = 0
            for mark, value in blocks:
                if mark == "INFOS":
                    text += f"{value}"
                    end = len(text) - 1
                    start = end + 1
                    continue
                text += f"{value} "
                end = len(text) - 1
                marks.add_annotation(start, end, mark)
                start = end + 1

            text = text.strip()
            marks.add_text(text)
            f.write(text)
    marks.close_item()


if __name__ == "__main__":
    generate_cv(1000)

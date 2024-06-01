import pypandoc
from pathlib import Path
import fitz
import tkinter as tk
from tkinter import filedialog
import markdown
from bs4 import BeautifulSoup
import re
import os
from test import clean_html


def select_file() -> str:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def docx_to_txt(i_file='') -> Path:
    if not i_file:
        i_file = select_file()
    i_file = Path(i_file)
    html_text = docx_to_html(i_file)
    clean_text = clean_html(html_text)
    output_file = Path('./TXTS1/').joinpath(i_file.with_suffix('.txt').name)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(clean_text)
    return output_file


def docx_to_html(i_file) -> str:
    html_text = pypandoc.convert_file(i_file, 'html')
    return html_text


if __name__ == "__main__":
    rpath = './CV/'
    docx_files = [f for f in os.listdir(rpath) if f.endswith('.docx')]
    for item in docx_files:
        path = rpath + item
        docx_to_txt(path)

# subprocess.Popen(r'explorer /select')


def docx_to_md(input_file) -> Path:
    output_file = Path('./MDS/').joinpath(input_file.with_suffix('.md').name)
    pypandoc.convert_file(input_file, 'md', outputfile=output_file)
    return output_file


def pdf_to_txt(input_file) -> Path:
    output_file = Path('./MDS/').joinpath(input_file.with_suffix('.txt').name)
    pdf_doc = fitz.open(input_file)
    all_text = ""
    for page_num in range(len(pdf_doc)):
        page = pdf_doc.load_page(page_num)
        text = page.get_text('text')
        all_text += text
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(all_text)
    return output_file


# def rtf_to_md(input_file) -> str:
#     output_file = input_file.with_suffix('.docx').name
#     pypandoc.convert_file(input_file, 'docx', outputfile=output_file)
#     return output_file


def md_to_str(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    html_text = markdown.markdown(markdown_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text(strip=True, separator=' ')
    return text


def convert(i_file="") -> str:
    if not i_file:
        i_file = select_file()
    i_file = Path(i_file)
    if i_file.suffix in ['.docx', '.doc']:
        o_file = docx_to_md(i_file)
    elif i_file.suffix in ['.pdf']:
        o_file = pdf_to_txt(i_file)
    elif i_file.suffix in ['.rtf']:
        # o_file = rtf_to_md(i_file)
        pass
    else:
        return ""
    return md_to_str(o_file)
    # pypandoc.convert_file('./CV/*.docx', 'md', outputfile='./MDS/res.md')


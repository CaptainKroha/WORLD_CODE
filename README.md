Список используемых библиотек:

aiohttp==3.9.5
aiosignal==1.3.1
annotated-types==0.7.0
anyio==4.4.0
attrs==23.2.0
beautifulsoup4==4.12.3
blis==0.7.11
catalogue==2.0.10
category-encoders==2.6.3
certifi==2024.2.2
charset-normalizer==3.3.2
click==8.1.7
cloudpathlib==0.16.0
colorama==0.4.6
confection==0.1.4
contourpy==1.2.1
cycler==0.12.1
cymem==2.0.8
datasets==2.19.1
DAWG-Python==0.7.2
dill==0.3.8
dnspython==2.6.1
email_validator==2.1.1
fastapi==0.111.0
fastapi-cli==0.0.4
filelock==3.14.0
fonttools==4.52.4
frozenlist==1.4.1
fsspec==2024.3.1
h11==0.14.0
httpcore==1.0.5
httptools==0.6.1
httpx==0.27.0
huggingface-hub==0.23.2
idna==3.7
iniconfig==2.0.0
intel-openmp==2021.4.0
Jinja2==3.1.4
joblib==1.4.2
kiwisolver==1.4.5
langcodes==3.4.0
language_data==1.2.0
marisa-trie==1.1.1
Markdown==3.6
markdown-it-py==3.0.0
markdownify==0.12.1
MarkupSafe==2.1.5
matplotlib==3.9.0
mdurl==0.1.2
mkl==2021.4.0
mpmath==1.3.0
multidict==6.0.5
multiprocess==0.70.16
murmurhash==1.0.10
networkx==3.3
numpy==1.26.4
orjson==3.10.3
packaging==24.0
pandas==2.2.2
patsy==0.5.6
pillow==10.3.0
pluggy==1.5.0
preshed==3.0.9
pyarrow==16.1.0
pyarrow-hotfix==0.6
pydantic==2.7.2
pydantic_core==2.18.3
pydot==2.0.0
Pygments==2.18.0
pymorphy3==2.0.1
pymorphy3-dicts-ru==2.4.417150.4580142
PyMuPDF==1.24.4
PyMuPDFb==1.24.3
pypandoc==1.13
pyparsing==3.1.2
pytest==8.2.1
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
python-multipart==0.0.9
pytz==2024.1
PyYAML==6.0.1
regex==2024.5.15
requests==2.32.3
rich==13.7.1
ru-core-news-lg @ https://github.com/explosion/spacy-models/releases/download/ru_core_news_lg-3.7.0/ru_core_news_lg-3.7.0-py3-none-any.whl#sha256=fffc0e466b2ec712fd580e351c9107af667118284c9456c2c856e24ce4d58f7b
ru-core-news-md @ https://github.com/explosion/spacy-models/releases/download/ru_core_news_md-3.7.0/ru_core_news_md-3.7.0-py3-none-any.whl#sha256=a94b21e001c4f2cbe2f1e702785943dba83f2883d5a0a1ceac5363a2413082f8
safetensors==0.4.3
scikit-learn==1.5.0
scipy==1.13.1
setuptools==70.0.0
shellingham==1.5.4
six==1.16.0
sklearn2==0.0.13
smart-open==6.4.0
sniffio==1.3.1
soupsieve==2.5
spacy==3.7.4
spacy-legacy==3.0.12
spacy-loggers==1.0.5
srsly==2.4.8
starlette==0.37.2
statsmodels==0.14.2
sympy==1.12.1
tbb==2021.12.0
thinc==8.2.3
threadpoolctl==3.5.0
tokenizers==0.19.1
torch==2.3.0
tqdm==4.66.4
transformers==4.41.2
typer==0.9.4
typing_extensions==4.12.0
tzdata==2024.1
ujson==5.10.0
urllib3==2.2.1
uvicorn==0.30.0
wasabi==1.1.2
watchfiles==0.22.0
weasel==0.3.4
websockets==12.0
xxhash==3.4.1
yarl==1.9.4


Список используемых моделей:

spacy.blank('en')  и spacy.ru__core_news_md


Описание архитектуры:

Дообучение преобученной модели от spacy.

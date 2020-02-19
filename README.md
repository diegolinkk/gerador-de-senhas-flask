# gerador-de-senhas-flask
gerador de senhas simples feito em flask

- carrega um formulário (em template)
- envia informações via POST
- retorna senhas conforme solicitado no formulário

Para executar esse aplicativo

- ```python python -m venv venv ``` (gerar virtual env)
- ```python pip install -r requirements.txt ``` (instalar pacotes - aqui no caso apenas flask e suas dependências)
- ```bash env FLASK_APP=app.py  ``` (adiciona aplicativo no ambiente flask)
- ```bash flask run ``` (executa o aplicativo flask)
- abre navegador em: http://127.0.0.1:5000

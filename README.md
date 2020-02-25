# gerador-de-senhas-flask
## gerador de senhas simples feito em flask

- carrega um formulário (em template)
- envia informações via POST
- retorna senhas conforme solicitado no formulário

## Para executar esse aplicativo

### 1 - Criando virtual env
- `python -m venv venv`

### 2 - Ativando o virtual env
- `source venv/bin/activate` (Linux) ou
- `venv\Scripts\activate.bat` (Windows)

### 3 - Instalar o Flask
- `pip install flask`

### 4 - Configurando variável de ambiente

- `env FLASK_APP=app.py` (Linux) ou
- `$env:FLASK_APP = ".\app.py"` (Windows)

### 5 - Executando a aplicação
- `flask run` (executa o aplicativo flask)
- abre navegador em: http://127.0.0.1:5000

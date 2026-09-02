# CRUD de Filmes — Django

Projeto de exemplo: CRUD (Create, Read, Update, Delete) de filmes de um catálogo.

## Campos do model `Filme`
- `titulo` (CharField)
- `diretor` (CharField)
- `estudio` (CharField)
- `genero` (CharField com choices)
- `sinopse` (TextField)
- `duracao_minutos` (IntegerField)
- `data_lancamento` (DateField)
- `assistido` (BooleanField)

## Como executar

```bash
# 1. Criar e ativar um ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Criar o banco de dados (aplicar as migrations)
python manage.py makemigrations
python manage.py migrate

# 4. Criar um super usuário (para acessar o /admin)
python manage.py createsuperuser

# 5. Rodar o servidor
python manage.py runserver
```

Depois é só acessar:
- http://127.0.0.1:8000/ → listagem de filmes (CRUD)
- http://127.0.0.1:8000/admin/ → Django Admin



Feito pelos alunos Gustavo Peres Pereira e Gabriel Di Lorenzo Correa, do 6° Periodo de Sistemas de Informação da FEPI.
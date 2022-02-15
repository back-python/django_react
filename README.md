# Construção de uma API Rest Framework + Comunicação com API externa React

![Lincença do projeto](	https://img.shields.io/github/license/robsonleal/pedroreceitas)
![Bagde status desenvolvimento](https://img.shields.io/static/v1?label=status&message=CONCLUÍDO&color=green)

## Índice

* [Título](#Título)
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)

## Descrição do Projeto

Evolução do construção de API para uma escola.

Agora vai ser possivel listar a lista de curso em uma API externa construinda com React.

## Funcionalidades e Demonstração da Aplicação

Todas as funcionalidades do projeto anterior https://github.com/robsonleal/django_restapi/blob/main/README.md;

- `Funcionalidade 1`: Versionamento da API com Query Parameter Versioning;
- `Funcionalidade 2`: Relacionando as permissões do admin do Django com as permissões da API;
- `Funcionalidade 3`: Limite requisições permitidas por dia, para usuários que não estão logados;
- `Funcionalidade 4`: Documentando a API para retornar um Location no cabeçalho da requisição;
- `Funcionalidade 5`: Configurando o CORS para fazer a comunicação com a API externa;

Dependendo da versão que for solicitada pelo Query Parameter Versioning, será devolvido uma classe diferente de Serializer</br>
![Screenshot_20220215_171547](https://user-images.githubusercontent.com/27708175/154142070-4360121f-0502-4c52-8197-33316938fc7b.png)

Retornando localização do novo curso criado no cabeçalho da requisição:</br>
![Screenshot_20220215_165828](https://user-images.githubusercontent.com/27708175/154140227-8f2a2862-5107-415d-914c-4aaefa771268.png)

API externa, escrita em React listando os cursos da API:</br>
![Screenshot_20220211_121738](https://user-images.githubusercontent.com/27708175/154138576-90dc2b8d-8c91-4a17-a507-fadb54b1e1f8.png)


## Acesso ao Projeto

```console
git clone git@github.com:robsonleal/django-react.git
cd django-react
python -m venv ./venv
source venv/bin/activate
pip install -r 'requirements.txt'
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- Abrir o endereço localhost:8000 no navegador de sua preferência;
- Autenticação é os dados do super usuário que foi criado.

## Tecnologias utilizadas
`Django 4`
`Python 3`
`Django Rest Framework`


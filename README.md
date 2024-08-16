# Django Templates Practice Project

Este é um projeto Django desenvolvido para prática e execução de Django Templates. O projeto consiste em dois aplicativos (`apps`) separados: `consultaCEP` e `consultaPokemon`, cada um com funcionalidades distintas, mas que utilizam a estrutura de templates do Django para exibir dados e interagir com o usuário.

## Funcionalidades

### 1. **consultaCEP**
O app `consultaCEP` permite que o usuário insira um CEP (Código de Endereçamento Postal) brasileiro e, ao clicar em "Buscar", o sistema consulta a API viaCEP para buscar o endereço correspondente ao CEP informado. Os dados do endereço são exibidos na página, utilizando templates Django.

### 2. **consultaPokemon**
O app `consultaPokemon` permite que o usuário insira o nome de um Pokémon e, ao clicar em "Buscar", o sistema consulta a PokeAPI para buscar os dados do Pokémon informado. Se o nome do Pokémon estiver incorreto ou não existir, uma mensagem de erro é exibida. Caso contrário, as informações do Pokémon (como altura, peso e tipo) são exibidas na página, utilizando templates Django.

## Estrutura do Projeto

O projeto Django é estruturado da seguinte forma:

project_root/
│
├── apps/
│ ├── consultaCEP/
│ │ ├── migrations/
│ │ ├── templates/
│ │ │ └── consultaCEP.html
│ │ ├── init.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── forms.py
│ │ ├── models.py
│ │ ├── tests.py
│ │ ├── urls.py
│ │ └── views.py
│ │
│ ├── consultaPokemon/
│ │ ├── migrations/
│ │ ├── templates/
│ │ │ └── consultaPokemon.html
│ │ ├── init.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── forms.py
│ │ ├── models.py
│ │ ├── tests.py
│ │ ├── urls.py
│ │ └── views.py
│
├── project/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
└── README.md

## Como Instalar

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```
###2. Criar e Ativar um Ambiente Virtual
python -m venv env
source env/bin/activate   # No Windows: env\Scripts\activate
###3. Instalar as Dependências
pip install -r requirements.txt
###4. Aplicar as Migrações
python manage.py makemigrations consultaCEP consultaPokemon
python manage.py migrate
###5. Executar o Servidor de Desenvolvimento
python manage.py runserver
###**Como Usar**
Acessar a Aplicação
Consulta CEP: Acesse http://127.0.0.1:8000/consultaCEP/ para inserir um CEP e buscar o endereço correspondente.
Consulta Pokémon: Acesse http://127.0.0.1:8000/consultaPokemon/ para inserir o nome de um Pokémon e buscar suas informações.
Testando Funcionalidades
consultaCEP: Insira um CEP válido (por exemplo, 01001-000) e veja os detalhes do endereço retornados pela API viaCEP.
consultaPokemon: Insira o nome de um Pokémon (por exemplo, Pikachu) e veja as informações retornadas pela PokeAPI. Tente inserir um nome incorreto para ver a mensagem de erro.
Notas Finais
Este projeto é voltado para a prática de Django Templates e integração com APIs externas, utilizando Django Models, Forms, e Views. Ele serve como um ótimo ponto de partida para entender como Django lida com templates e renderização de dados dinâmicos em páginas web.

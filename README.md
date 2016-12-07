#Bem vindo ao repositório do projeto GDE

### Introdução

Este repositório contém o código do sistema web, que foi desenvolvido em Python utilizando a framework Django, para levantar as tipologias documentais existentes no IFES e educar os servidores quanto a utilização de seus documentos. Este documento mostrará os pré-requisitos, o processo de instalação e configuração em um ambiente linux, e por último como executá-lo e disponibilizá-lo para os servidores.

### Pré-Requisitos do Sistema
* **Python >= 3.5.2**
* **Virtualenv >= 15.0.2**
* **Pip >= 8.1.2**
* **python3-dev**
* **PostgreSQL >= 9.3**
* **PhantomJs >= 2.1**

### Processo de Instalação

1. Faça o download do Código:
 * [Download Zip](https://github.com/LEDS/gde/archive/master.zip)
 * Caso possua o git instalado, ao invés de baixar o zip, execute, em um terminal, o seguinte comnando na pasta onde desejar salvar o projeto:
      git glone https://github.com/LEDS/gde.git
2. Abra um terminal e vá até a pasta onde o projeto se econtra. 
3. Crie um ambiente virtual na raiz do projeto executando o comando:
    virtualenv -p python3 env
4. Em seguida ative-o com o comando:
    source env/bin/activate
5. Em seu postgres, crie um banco com o nome 'gde'. Vá até o arquivo settings.py, encontrado na pasta 'wsgi/gde/gde' e altere o campo 'PASSWORD', no else da seção 'Databases', com a senha do banco utilizada.
6. Volte para o terminal e execute o comando:
    pip install -r requirements.txt
7. Agora vá até a pasta 'wsgi/gde' e execute o comando:
    python3 manage.py migrate
   Este comando realizará a criação das tabelas no banco de dados.
8. Em seguida execute o comando:
    python3 manage.py createsuperuser
    Este comando realizará a criação de um usuário com direitos administrativos no sistema.

    
### Executando o projeto

Para executar o projeto vá até a pasta 'wsgi/gde', com o ambiente virtual ativado, e execute o comando:

    python3 manage.py runserver
    
O servidor estará disponível no endereço:

    http://localhost:8000/

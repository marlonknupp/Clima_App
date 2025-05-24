Projeto: Previsão do Tempo com python, Django e AccuWeather

📌 Descrição
è um aplicativo web simples e funcional de previsão do tempo, desenvolvido com Python e Django, que consome dados em tempo real da API gratuita da AccuWeather. 
O usuário pode digitar o nome de uma cidade e visualizar a temperatura, umidade, descrição climática e um ícone representando as condições atuais.
Projeto de aprendizado para consumir APIs externas e trabalhar com dados dinâmicos.

🚀 Tecnologias Utilizadas
Python 3.13
Django 5.2.1
HTML5 + CSS3 
Font Awesome (ícones)
Google Fonts (Roboto)
AccuWeather API (dados meteorológicos)
Requests (requisições HTTP em Python)
Git (controle de versão)

⚙️ Como Instalar e Rodar Localmente
Pré-requisitos: Python instalado na máquina (recomenda-se Python 3.10+), Git.

1. Clone o repositório

git clone [link]

2. Crie e ative o ambiente virtual

python -m venv venv
venv\Scripts\activate

3. Instale as dependências

pip install -r requirements.txt

4. Configure a chave da API AccuWeather
Crie um arquivo .env (ou adicione direto na views.py) com sua chave de API:

API_KEY = "SUA_CHAVE_AQUI"
Você pode obter sua chave gratuita em: https://developer.accuweather.com/

5. Rode o servidor

python manage.py runserver

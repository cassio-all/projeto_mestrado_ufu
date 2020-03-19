# Projeto de Mestrado

O objetivo deste projeto é criar funções que possibilitem a análise de sentimento em diferentes redes sociais de um grupo de usuários. Para isso, serão desenvolvidos métodos de coleta, tratamento e modelagem de dados provenientes de redes sociais.

## Iniciando/Requerimentos/Prerequisitos/Dependencias

- No prompt:
    - rodar <strong>pip install -r requirements.txt</strong> para instalar os requerimentos no seu ambiente
    - <strong>python -m spacy download pt_core_news_sm</strong> para baixar o modelo do spacy em português. Para ver sobre outros modelos, visitar [spacy](https://spacy.io/models).
- Entrar em [twitter-develop](https://developer.twitter.com/) e criar uma conta do Twitter caso não tenha. Você precisará de gerar chaves de acesso a adicioná-las no arquivo api/configs.ini
- Rodando o programa:
    - o programa possui três variáveis de entrada, sendo todas opcionais. São elas: quais redes sociais deseja coletar os dados, qual hashtag deseja pesquisar no Twitter e o número de postagens que deseja coletar. O default é: <em>twitter</em>, <em>política</em>, <em>200</em>, respectivamente.

## To Do

- Adicionar coleta do instagram
- Tentar implementar tradução
- Testar funções de modelagem: fasttext e BERT

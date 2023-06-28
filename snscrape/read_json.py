from json import loads
from database import insert_tweet


# Abre o arquivo json e insere os tweets no banco de dados
with open("jsons/cheese_pizza.json", encoding= "utf-8") as jsonfile:
    # O arquivo json tem um tweet por linha
    # O formato usado pelo SNSCRAPE (jsonl) tem um JSON completo por linha, porém não é um JSON válido
    # Por isso fazemos o parse linha por linha
    for line in jsonfile:
        # Carrega o tweet via json.loads
        tweet = loads(line)

        # insere o tweet no banco de dados
        insert_tweet(tweet)
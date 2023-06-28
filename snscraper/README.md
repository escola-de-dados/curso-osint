# Exemplo de código em Python lendo JSONL do SNSCRAPE

Utilizamos o SNSCRAPE para capturar JSONS, esse comando aqui serve para colocar esses mesmo arquivos num banco de dados para melhor manipulação.

A ordem que vocês devem olhar os arquivos comentados para melhor compreensão:


1) alchemy.py >> arquivo que monta a estrutura do banco de dados, determinando suas colunas;
2) config.json\[.default\] >> arquivo onde devem ser colocadas as credenciais de acesso ao banco;
3) run_configuration.py >> executa a construção da estrutura do banco de dados;
4) database.py >> conjunto de comandos que permitirá inserção de dados no banco de dados;
5) read_json.py >> arquivo que faz a leitura dos json capturados pelo SNSCRAPE;

O arquivo que estou subindo junto é um JSON com cerca de 2000 tweets com a busca `cheese pizza child` apenas para ilustrar.

Os dados foram colocados num banco de dados usando esse código que estou entregando pra vocês, e o resultado pode ser visualizado em ferramentas como o Metabase. Algumas visualizações feitas com o Metabase:

* http://data.7c0.link/public/question/a2fcb5b7-c507-4ef8-8740-4692437aa8ce
* http://data.7c0.link/public/question/5a477e00-3d07-421e-97b8-e3ab663a6da6
  
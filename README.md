# Aplicação de coleta de dados veiculares

## Como utilizar aplicações questão 3
Para utilizar as aplicações seguir os seguintes passos:

O python deve estar instalado na máquina

É necessário instalar a biblioteca requests (presente em requirements.txt)
Pode ser instalado com o seguinte comando no prompt de comando:

* python -m pip install requests
  
Agora, deve-se inicializar o servidor.
Para isso, abrir o arquivo aplicação.bat e digitar o seguinte código:

* python servidor.py

Em seguida, para simular os dados veiculares, a aplicação coletor.py deve ser inicializada
Executar novamente o arquivo aplicação.bat digitar o seguinte código:

* python coletor.py

Agora, no prompt do servidor, é possível ver os dados, além de que na pasta agora existem dois arquivos:

autoInfoFile.csv

autoInfoFile.txt

Nestes estão guardados os dados em seus respectivos formatos.

Para parar qualquer um das duas aplicações basta enviar Ctrl+c nos terminais

## Proposta
Desenvolva duas aplicações usando a linguagem Python ou C++, que simulem um sistema de coleta, envio e
recebimento de dados veiculares. A primeira aplicação, "Coletor", deve ser responsável por coletar dados simulados
de sensores e enviar esses dados para a segunda aplicação, "Servidor". A segunda aplicação, "Servidor", deve
receber os dados enviados pelo Coletor, processar e armazenar os resultados em um banco de dados (ou em algum
arquivo).
Requisitos:
1. O Coletor deve ser capaz de coletar dados simulados de sensores veiculares, como por exemplo
velocidade, temperatura do motor, pressão dos pneus etc. Você deve simular pelos menos 10 variáveis
diferentes.
2. O Coletor deve enviar os dados coletados para o Servidor, utilizando algum mecanismo de comunicação
adequado para receber os dados rapidamente. (HTTP, MQTT, TCP etc.)
3. O Servidor deve receber os dados do Coletor, processar e armazenar os resultados de acordo com a
lógica que você definir (banco de dados ou arquivo).

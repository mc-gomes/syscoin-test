# Teste prático Syscoin Space

## Atividade 1 - Requisição HTTP

Para a realização da atividade 1 foi utilizada a linguagem **Python**. Os arquivos utilizados estão na pasta `atividade1`:

- `.env.example`: arquivo de variáveis de ambiente de exemplo. É **necessário criar um arquivo** `.env`  na mesma pasta, semelhante ao de exemplo, e adicionar a variável `HEADER_TOKEN` com o valor do token de autorização do header.
- `request.py`: arquivo principal com o código implementado para fazer a requisição POST no endpoint indicado. Irá consumir o valor da variável em `.env`

Para executar o código, acesse o diretório da atividade e execute o arquivo principal:

```bash
cd atividade1

python3 request.py

```

## Atividade 2 - Deploy local do Uptime Kuma com Docker

Para a atividade 2 foi criado um arquivo `docker-compose.yml`. O arquivo se encontra na pasta `atividade2` juntamente com um vídeo da gravação da tela mostrando o deploy feito localmente:

Para subir o container, acesse o diretório da atividade e execute o comando:

```bash
cd atividade2

docker compose up

```

Após a inicialização do container, a aplicação deve estar disponível para acesso em `http://localhost:3001/`


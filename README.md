# Steam Sales Scraping

Raspagem e exportação para arquivo CSV de dados do site https://steamdb.info/sales/.

## **Como executar**

**1.** Clone este repositório:

```bash
$ git clone https://github.com/eldersantoss/steam-sales-scraping.git
```

**2.** Acesse o diretório da aplicação, crie um ambiente virtual e ative-o:

```bash
$ python -m venv venv
$ source /venv/bin/activate
```

**3.** Instale as dependências do projeto:
```bash
$ pip install -r requirements.txt
```

**4.** Para o script funcionar corretamente, é preciso que se atualize a constante
`COOKIES` antes da execução. O cookie de nome `__cf_bm` é o mais importante e
deve ser definido sempre. Já no caso do cookie `cf_clearance`, se ele estiver
presente no navegador, então deve-se descomentar no dicionário e colocar seu
valor. Para atualizar a constante `COOKIES`, siga as instruções:
  * Abra o painel de desenvolvedor do navegador e busque pela opção `Network`.
  
  * Acesse o página `https://steamdb.info/sales/` e, quando finalizar
  seu carregamento, busque, no painel network, pela requisição `/sales`.

  * Abra a requisição, acesse a aba de `cookies` e preencha o dicinário `COOKIES`
  com os valores que encontrar nas informações da requisição, seguindo o padrão já
  definido no dicionário.

**5.** Após preenchidos atualizados os cookies, execute o arquivo `main.py`:
```bash
$ python main.py
```


---
## Observações

* O site possui uma série de mecanismos para prevenção de raspagem de dados. Entre
eles, a utilização de alguns cookies de proteção disponibilizados pelo próprio
servidor, o `Cloudflare`. Além dos cookies, o servidor também realiza outras verificações
um pouco mais complexas, como a execução de scripts de validação JavaScript, o que torna
o processo de raspagem ainda mais complicado.

* Para tentar contornar esses problemas, foram realizadas tentativas de obtenção dos
cookies de forma automatizada utilizando a biblioteca `Selenium` para emulação de
navegadores reais, porém o sistema também detectou esse artifício e acabou bloqueando.
Outras tentativas foram realizadas através de pacotes de terceiros como `cloudflare-scrapy`,
mas todas sem sucesso.

* Então, por não ter tempo hábil para buscar outra solução mais robusta, acabou-se por
adotar o método descrito acima, extraindo o cookie manualmente e executando o script.
Apesar de trabalhoso e não muito produtivo do ponto de vista de automação, o resultado
foi satisfatório pois conseguiu-se obter uma grande quantidade de dados da página, conforme
pode ser verificado no arquivo de saída .csv.

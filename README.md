# Imoveis Scraper

Este repositório contém um scraper de propriedades do site [Zap Imoveis](https://www.zapimoveis.com.br/) escrito em Python e que extrai dados de imoveis e salva em arquivos JSON.

## Como usar
1. Clone o repositório para a sua máquina local:
    ```bash
    git clone https://github.com/Ruy-Araujo/properties-scraper.git
    ```
2. Instale as dependências:
    ```bash
    cd 
    pip install -r requirements.txt
    ```
4. Excute o script scrap.py
    ```python3
    python scrap.py
    ```

O scraper irá extrair dados das imoveis e salvara em um arquivo JSON no diretório data do projeto.

## Detalhes técnicos
O scraper usa o framework [Scrapy](https://scrapy.org/)

Os dados brutos estão disponiveis [aqui](data/)

## Contribuindo
Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
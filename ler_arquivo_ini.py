import configparser
"""
Codo inicial para retorno de um dicionario do arquivo fogi.ini

config= {
    secao = {chave: valor},
    secao 2 = {chave: valor},....
}

Willian Ohara em 3/11/2024
"""

def ler_arquivo_ini():
    """Carrega um arquivo de configuração .ini e converte em um dicionário."""
    # Cria um objeto ConfigParser
    config = configparser.ConfigParser()

    # Lê o arquivo de configuração
    config.read('config.ini')

    # Converte o resultado para um dicionário
    ini_data = {}
    for secao in config.sections():  # Recupera as seções do dicionário
        valores = {}
        for chave in config[secao]:  # Recupera a chave e valor de cada seção
            valores[chave] = config[secao][chave]
        ini_data[secao] = valores
    return ini_data

if __name__ == "__main__":
    ini_file=ler_arquivo_ini()
    print(ini_file)
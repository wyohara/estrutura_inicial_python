import configparser

def ler_arquivo_ini(arquivo='config.ini'):
    """
    Carrega um arquivo de configuração .ini e converte em um dicionário.

    Parameters:
    arquivo (String, opcional): arquivo de configuração a ser lido. Padrão é 'config.ini'

    Return:
    Dict do arquivo config.ini. O padrão é:
    config= {
        secao = {chave: valor},
        secao 2 = {chave: valor},....
    }
    """
    config = configparser.ConfigParser().read(arquivo)

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
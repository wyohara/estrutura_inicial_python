import configparser
import os

class ConfiguracaoInit():
    def __init__(self, arquivo='config.ini'):
        self.__ARQUIVO = arquivo
        self.__config = configparser.ConfigParser()
        self.__iniciar_configParser()        
        self.__dados = None
        self.__carregar_config_ini()

    def __iniciar_configParser(self):
        # Verifica se o arquivo existe
        if not os.path.exists(self.__ARQUIVO):
            # Cria a estrutura básica do arquivo INI
            self.__config['AMBIENTE_VIRTUAL'] = {
                'venv_criado': 0,  # Valor padrão
                'pip_instalado': 0,  # Valor padrão
            }
            
            # Salva o arquivo
            with open(self.__ARQUIVO, 'w') as configfile:
                self.__config.write(configfile)

    def __carregar_config_ini(self):

        # Lê o arquivo existente ou recém-criado
        self.__config.read(self.__ARQUIVO)

        if not isinstance(self.__config, configparser.ConfigParser):
            raise TypeError("O argumento deve ser um objeto ConfigParser")
        
        config_dict = {}
        
        # Inclui a seção DEFAULT se existir valores
        if self.__config.defaults():
            config_dict['DEFAULT'] = dict(self.__config.defaults())
        
        # Adiciona todas as outras seções
        for section in self.__config.sections():
            config_dict[section] = dict(self.__config[section])

        self.__dados = config_dict #salvando os dados no dicionario
    
    def set_valor(self, secao='', chave='', valor=''):        
        if not self.__config.has_section(secao):
            self.__dados[secao]={}

        self.__dados[secao][chave]=str(valor)
        
        # Converte para ConfigParser antes de salvar
        self.__config = configparser.ConfigParser()
        self.__config.read_dict(self.__dados)

        # Salva no arquivo
        with open(self.__ARQUIVO, 'w') as configfile:
            self.__config.write(configfile)
    
    @property
    def dados(self): return self.__dados

if __name__ == "__main__":
    c = ConfiguracaoInit()
    c.set_valor('AMBIENTE_VIRTUAL','venv_criado',1)
    print(c.dados)

    

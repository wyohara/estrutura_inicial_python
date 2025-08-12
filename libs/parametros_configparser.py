from libs.init_configparser import ConfiguracaoInit
class ParametrosConfigparser():
    def __init__(self):
        self.initparser = ConfiguracaoInit()

    @property
    def get_venv_criado(self):return self.initparser.dados['AMBIENTE_VIRTUAL']['venv_criado']

    def set_venv_criado(self, valor):self.initparser.set_valor('AMBIENTE_VIRTUAL','venv_criado',valor)

    @property
    def get_pip_instalado(self):return self.initparser.dados['AMBIENTE_VIRTUAL']['pip_instalado']
    
    def set_pip_instalado(self,valor):self.initparser.set_valor('AMBIENTE_VIRTUAL','pip_instalado',valor)
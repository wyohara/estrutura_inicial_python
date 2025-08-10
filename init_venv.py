import os
import sys
import venv
import subprocess
from importlib.metadata import distributions
from libs.init_configparser import ConfiguracaoInit

class AmbienteVirtual:

    def __init__(self, nome_env="venv", requirements_txt="req.txt", salvar_requirements=True):    
        self.nome_env = nome_env
        self.requirements_txt = requirements_txt
        self.initFile = ConfiguracaoInit()

        if salvar_requirements: self.salvar_requirements()

    def ambiente_existe(self): return os.path.exists(self.nome_env)

    def cria_ambiente_virtual(self, instrucoes=True):

        if int(self.initFile.dados['AMBIENTE_VIRTUAL']['venv_criado'])==1:
            print(f"O ambiente virtual '{self.nome_env}' já existe.")
        else:
            self._criar_ambiente()
            self.initFile.set_valor('AMBIENTE_VIRTUAL','venv_criado',1)
        
        self._instalar_dependencias()
        if instrucoes: self.exibir_instrucoes()

    def salvar_requirements(self):
        with open(self.requirements_txt, 'w') as req_file:
            subprocess.run(['pip', 'freeze'], stdout=req_file)
            print(f"Dependências salvas em '{self.requirements_txt}'.")


    def _criar_ambiente(self):
        """Cria o ambiente virtual com pip integrado."""
        try:
            venv.create(self.nome_env, with_pip=True)
            print(f"Ambiente virtual '{self.nome_env}' criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar o ambiente virtual: {e}")

    def _instalar_dependencias(self):
        """Instala as dependências especificadas no arquivo requirements.txt."""
        req_txt_path = os.path.join(os.getcwd(), self.requirements_txt)
        
        if not os.path.isfile(req_txt_path):
            print(f"Arquivo '{self.requirements_txt}' não encontrado.")
            return

        pip_executable = self._get_pip_executable()
        if not pip_executable:
            print("Erro ao localizar o executável do pip.")
            return

        try:
            subprocess.check_call([pip_executable, "install", "-r", self.requirements_txt])
            print("Dependências instaladas com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar dependências: {e}")

    def _get_pip_executable(self):
        """Retorna o caminho do executável pip dependendo do sistema operacional."""
        if os.name == "nt":  # Windows
            return os.path.join(self.nome_env, "Scripts", "pip")
        elif os.name == "posix":  # macOS/Linux
            return os.path.join(self.nome_env, "bin", "pip")
        return None


    def exibir_instrucoes(self):
        """Exibe instruções para ativar o ambiente virtual."""
        comando_ativacao = self._obter_comando_ativacao()
        print(f"Para ativar o ambiente virtual, execute: {comando_ativacao}")
        print(f"Para acessar o diretório do arquivo, execute: cd {os.getcwd()}")
        print("Para iniciar o shell, execute: python -m idlelib.idle")

    def _obter_comando_ativacao(self):
        """Retorna o comando para ativar o ambiente virtual dependendo do sistema operacional."""
        if os.name == "nt":  # Windows
            return f"{self.nome_env}\\Scripts\\activate"
        elif os.name == "posix":  # macOS/Linux
            return f"source {self.nome_env}/bin/activate"
        return ""
    
    def is_venv_ativo():
        # Verifica para Python moderno (3.3+) e antigo
        in_venv = (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix) or (
            hasattr(sys, 'real_prefix'))
        
        if in_venv:
            print ({
                'active': True,
                'path': os.environ.get('VIRTUAL_ENV', sys.prefix),
                'base_python': sys.base_prefix,
                'current_python': sys.prefix
            })
            return True
        return False
            


if __name__ == "__main__":
    ambiente = AmbienteVirtual()
    ambiente.cria_ambiente_virtual()

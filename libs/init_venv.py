import os
import sys
import venv
import subprocess
from libs.parametros_configparser import ParametrosConfigparser

class AmbienteVirtual:

    def __init__(self, nome_env="venv", requirements_txt="req.txt"):    
        self.nome_env = nome_env
        self.requirements_txt = requirements_txt
        self.paramInitParser = ParametrosConfigparser()


    @property
    def is_ambiente_existe(self): return os.path.exists(self.nome_env)
    
    @property
    def is_requeriments_existe(self): return os.path.exists(os.path.join(os.getcwd(), self.requirements_txt))

    def cria_ambiente_virtual(self, instrucoes=True):

        if int(self.paramInitParser.get_venv_criado)==1:
            print(f"O ambiente virtual '{self.nome_env}' já existe.")
        else:
            self.__criar_ambiente()
            self.paramInitParser.set_venv_criado(1)
                
        if not self.is_requeriments_existe: #caso exista req.txt o carrega
            self.salvar_requirements()
        else:
            if 'VIRTUAL_ENV' in os.environ: #caso esteja em um abiente virtual
                self.instalar_dependencias()
                self.paramInitParser.set_pip_instalado(1)

        if instrucoes: self.exibir_instrucoes()

    def salvar_requirements(self):
        with open(self.requirements_txt, 'w') as req_file:
            subprocess.run(['pip', 'freeze'], stdout=req_file)
            print(f"Dependências salvas em '{self.requirements_txt}'.")
            self.paramInitParser.set_pip_instalado(0)


    def __criar_ambiente(self):
        """Cria o ambiente virtual com pip integrado."""
        try:
            venv.create(self.nome_env, with_pip=True)
            print(f"Ambiente virtual '{self.nome_env}' criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar o ambiente virtual: {e}")

    def instalar_dependencias(self):
        """Instala as dependências especificadas no arquivo requirements.txt."""
        req_txt_path = os.path.join(os.getcwd(), self.requirements_txt)
        
        if not os.path.isfile(req_txt_path):
            print(f"Arquivo '{self.requirements_txt}' não encontrado.")
            return

        pip_executable = self.__get_pip_executable()
        if not pip_executable:
            print("Erro ao localizar o executável do pip.")
            return

        try:
            subprocess.check_call([pip_executable, "install", "-r", self.requirements_txt])
            print("Dependências instaladas com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar dependências: {e}")

    def __get_pip_executable(self):
        """Retorna o caminho do executável pip dependendo do sistema operacional."""
        if os.name == "nt":  # Windows
            return os.path.join(self.nome_env, "Scripts", "pip")
        elif os.name == "posix":  # macOS/Linux
            return os.path.join(self.nome_env, "bin", "pip")
        return None


    def exibir_instrucoes(self):
        """Exibe instruções para ativar o ambiente virtual."""
        comando_ativacao = self.__obter_comando_ativacao()
        print(f"Para ativar o ambiente virtual, execute: {comando_ativacao}")
        print(f"Para acessar o diretório do arquivo, execute: cd {os.getcwd()}")
        print("Para iniciar o shell, execute: python -m idlelib.idle")

    def __obter_comando_ativacao(self):
        """Retorna o comando para ativar o ambiente virtual dependendo do sistema operacional."""
        if os.name == "nt":  # Windows
            return f"{self.nome_env}\\Scripts\\activate"
        elif os.name == "posix":  # macOS/Linux
            return f"source {self.nome_env}/bin/activate"
        return ""

    @property
    def is_venv_ativo(self):
        if 'VIRTUAL_ENV' in os.environ:
            print("✅ Ambiente virtual ATIVO")
            print(f"Caminho: {os.environ['VIRTUAL_ENV']}")
            return True
        else:
            print("❌ Ambiente virtual INATIVO")
            return False
            
if __name__ == "__main__":
    ambiente = AmbienteVirtual()
    ambiente.cria_ambiente_virtual()

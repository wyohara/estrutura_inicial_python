from libs.init_venv import AmbienteVirtual


    
if __name__ == "__main__":
    ambiente = AmbienteVirtual()
    ambiente.cria_ambiente_virtual()
    
    if ambiente.is_venv_ativo:
	pass
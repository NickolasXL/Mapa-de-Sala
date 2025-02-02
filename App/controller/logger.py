import logging
import os
from secrets import token_hex

class Log:

    def __init__(self, name="basic") -> None:
        self.logger = logging.getLogger(token_hex(4))
        self.logger.setLevel(logging.DEBUG)

        caminho = 'env/log'
        if (not os.path.exists(caminho)):
            os.mkdir(caminho)

        # HANDLER (ARQUIVO)
        file_handler = logging.FileHandler(f"{caminho}/{name}.log", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter( logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt="%d-%m-%Y %H:%M:%S"))
        self.logger.addHandler(file_handler)

    def debug(self, mensagemErro):
        self.logger.debug(mensagemErro)

    def info(self, mensagemErro):
        self.logger.info(mensagemErro)

    def warning(self, mensagemErro):
        self.logger.warning(mensagemErro)

    def error(self, mensagemErro):
        self.logger.error(mensagemErro)

    def critical(self, mensagemErro):
        self.logger.critical(mensagemErro)

if __name__ == "__main__":
    bd = Log("banco")
    bd.critical("Erro critico no código")

    view = Log("view")
    view.debug("Erro de bug que aconteceu no código")


from typing import Any
import argparse

def parse_args() -> Any:
    """ le os argumentos de linha de comando usando a biblioteca argparse """
    parser = argparse.ArgumentParser(description='Executar o Programa')
    parser.add_argument('config', type=str)
    parser.add_argument('report', type=str)

    # Exemplo. Utilizar o argparse na versao final
    args = parser.parse_args()

    return args

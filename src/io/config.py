

from typing import Dict
import json


def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """
    f = open(path)
    data_dict = json.loads(f.read())

    return data_dict


from typing import Dict
from src.io.config import load_config


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento
     dataset: image
    path: data/datasets/news_small/
    classifier: knn
    training time per sample: 0.01s
    inference time per sample: 0.2s
    accuracy: 0.85"""
    with open(path, 'w') as arquivo:
        arquivo.write(f'dataset: {config["type"]}\n')
        opath = config["train_path"].split("/")
        opath.pop()
        arquivo.write(f'path: {"/".join(opath)}\n')
        arquivo.write(f'classifier: {config["classifier"]}\n')

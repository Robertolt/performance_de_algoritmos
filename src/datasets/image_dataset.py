
from typing import Tuple, Any, Dict
from src.datasets.dataset_interface import DatasetInterface
import cv2

class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar
        # em uma lista

        self.lista_total = []
        with open (path, 'r') as arquivo:
            for line in arquivo:
                img_n_class = line.split()
                self.lista_total.append(img_n_class)

        path = path.split('/')
        path.pop()
        path.append('')
        path = '/'.join(path)
        self.path_tratado = path

    def size(self) -> int:
        # retornar tamanho do dataset (numero de linhas do arquivo)
        return len(self.lista_total)

    def get(self, idx: int) -> Tuple[Any, str]:
        lista_parcial = self.lista_total[idx]
        img = cv2.imread(f'{self.path_tratado}{lista_parcial[0]}', 0)
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe
        return img, f"{lista_parcial[1]}"


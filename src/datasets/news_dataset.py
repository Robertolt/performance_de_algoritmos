
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface


class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes
        self.lista_total = []
        with open(path, 'r') as arquivo:
            for line in arquivo:
                news_n_class = line.split()
                self.lista_total.append(news_n_class)

        path = path.split('/')
        path.pop()
        path.append('')
        path = '/'.join(path)
        self.path_tratado = path

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        return len(self.lista_total)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        lista_parcial = self.lista_total[idx]
        lista_palavras = []
        with open(self.path_tratado + lista_parcial[0], 'r') as arquivo:
            for line in arquivo:
                lista_palavras.append(line.split())

        palavras_a_excluir = ['a', 'as', 'com', 'como', 'da', 'de', 'disse', 'diz', 'do', 'dos', 'e', 'em',
                              'elas', 'eles', 'es', 'foi', 'foram', 'i', 'is', 'no', 'na', 'muito', 'o',
                              'outro', 'outros', 'os', 'para', 'pega','pegou', 'pode',
                              'quando', 'que', 'quem', 'sao', 'se', 'seu', 'ter', 'u', 'um','uma']

        lista_tratada = []

        for lista in lista_palavras:
            for palavra in lista:
                if palavra not in palavras_a_excluir:
                    lista_tratada.append(palavra)

        dct_palavras_numeros = {}

        return lista_tratada, f"{lista_parcial[1]}"



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

        lista_palavras_para_vetorizar = []
        for idx in range(len(self.lista_total)):
            with open(self.path_tratado + self.lista_total[idx][0], 'r') as arquivo:
                for line in arquivo:
                    lista_auxiliar_vetorizacao = line.split()
                    for palavras in lista_auxiliar_vetorizacao:
                        if palavras not in lista_palavras_para_vetorizar:
                            lista_palavras_para_vetorizar.append(palavras)
                        else:
                            pass



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


        lista_tratada = []

        for lista in lista_palavras:
            for palavra in lista:
                if palavra not in palavras_a_excluir:
                    lista_tratada.append(palavra)

        dct_palavras_numeros = {}

        return lista_tratada, f"{lista_parcial[1]}"


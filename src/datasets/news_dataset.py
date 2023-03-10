
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface


class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes
        path = path.split('/')
        self.final_do_path = path.pop()
        path.append('')
        path = '/'.join(path)
        self.lista_total = []
        self.lista_total1 = []
        self.lista_total2 = []
        # é necessário tratar o path antes de adicionar manualmente pois o vetor precisa ter como dimensao
        # todas as palavras, inclusive as de teste e treino juntas
        with open(path + 'test.txt', 'r') as arquivo:
            for line in arquivo:
                news_n_class = line.split()
                self.lista_total1.append(news_n_class) # essa lista apresenta o tamanho do test.txt para a size()

        with open(path + 'train.txt', 'r') as arquivo:
            for line in arquivo:
                news_n_class = line.split()
                self.lista_total2.append(news_n_class) # essa lista apresenta o tamanho do train.txt para a size()

        self.lista_total = self.lista_total2 + self.lista_total1

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

        self.lista_posicao_palavras = lista_palavras_para_vetorizar # esse vetor guarda na classe a posicao de todas
        # as palavras sem repeticao e a comparacao desta lista com o dicionario nos dará o vetor


    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        if self.final_do_path == 'test.txt':
            return len(self.lista_total1)
        else:
            return len(self.lista_total2)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        lista_parcial = self.lista_total[idx]
        lista_palavras = []
        with open(self.path_tratado + lista_parcial[0], 'r') as arquivo:
            for line in arquivo:
                lista_palavras.append(line.split())
                dicionario = {}
                for list_palavra in lista_palavras:
                    for palavras in list_palavra:
                        if palavras in dicionario:
                            dicionario[palavras] += 1
                        else:
                            dicionario[palavras] = 1

            vetor_noticia = []
            for palavras in self.lista_posicao_palavras:
                if palavras in dicionario:
                    vetor_noticia.append(dicionario[palavras])
                else:
                    vetor_noticia.append(0)



        return vetor_noticia, f"{lista_parcial[1]}"


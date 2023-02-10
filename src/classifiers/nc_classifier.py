
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """
        self.lista_treinamento = []
        self.tamanho_da_lista_treino = train_dataset.size()
        self.dct_centroide = {}
        for i in range(train_dataset.size()):
            self.lista_treinamento.append(train_dataset.get(i))
        for x in range(len(self.lista_treinamento)):
            lista_media = []
            lista_classe = []
            for dupla in self.lista_treinamento:
                if self.lista_treinamento[x][1] == dupla[1]:
                    if dupla[0] not in lista_media:
                        lista_media.append(dupla[0])
                        if dupla[1] not in lista_classe:
                            lista_classe.append(dupla[1])

            lista_centroide = []
            for dimensoes in range(len(lista_media[0])):
                contador = 0
                valor_total = 0
                for vetores in lista_media:
                    valor_total += float(vetores[dimensoes])
                    contador += 1
                lista_centroide.append(valor_total/contador)


            self.dct_centroide[lista_classe[0]] = lista_centroide
        # salvar as amostras do dataset
        pass

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        lista_para_decisao_por_amostra = []
        for x in range(test_dataset.size()):
            lista_teste_com_vetor_e_classe = []
            lista_teste_com_vetor_e_classe.append(test_dataset.get(x))
            lista_vetor_teste_2 = lista_teste_com_vetor_e_classe[0]
            lista_vetor_teste = lista_vetor_teste_2[0]
            lista_para_decisao = []
            for k, v in self.dct_centroide.items():
                lista_vetor_treino = self.dct_centroide[k]
                distancia = 0
                for numero_de_coordenada in range(len(lista_vetor_treino)):
                    distancia += (float(lista_vetor_treino[numero_de_coordenada]) -
                                  float(lista_vetor_teste[numero_de_coordenada])) ** 2
                distancia = distancia ** 0.5
                lista_para_decisao.append([distancia, k])
            lista_auxiliar = sorted(lista_para_decisao, key=lambda x: x[0])
            lista_para_decisao_por_amostra.append(lista_auxiliar[0][1])

        return lista_para_decisao_por_amostra

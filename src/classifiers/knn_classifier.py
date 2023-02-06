from typing import Dict, List
from src.classifiers.classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
from src.datasets.image_dataset import ImageDataset


class KnnClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        self.lista_treinamento = []
        self.tamanho_da_lista_treino = train_dataset.size()
        for i in range(train_dataset.size()):
            self.lista_treinamento.append(train_dataset.get(i))
        # salvar as amostras do dataset
        pass

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        lista_para_decisao = [] # está lista guardará a distancia de cada vetor e a classe
        # de forma em que após o predict o programa irá percorrer essa lista e então para as
        # 5 menores distâncias ele irá dizer qual a classe
        for x in range(test_dataset.size()):
            lista_teste_com_vetor_e_classe = []
            lista_teste_com_vetor_e_classe.append(test_dataset.get(x))
            lista_vetor_teste_2 = lista_teste_com_vetor_e_classe[0]
            lista_vetor_teste = lista_vetor_teste_2[0]
            for i in range(self.tamanho_da_lista_treino):
                lista_treinamento_unitária_vetor_classe = self.lista_treinamento[i]
                lista_vetor_treino = lista_treinamento_unitária_vetor_classe[0]
                distancia = 0
                for numero_de_coordenada in range(len(lista_vetor_treino)):
                    distancia += (float(lista_vetor_treino[numero_de_coordenada]) -
                                  float(lista_vetor_teste[numero_de_coordenada])) ** 2
                distancia = distancia ** 0.5
                lista_para_decisao.append([distancia, lista_treinamento_unitária_vetor_classe[1]])
        lista_para_decisao = sorted(lista_para_decisao, key=lambda x: x[0])

        classe_apos_teste = []
        for i in range(5):
            classe_apos_teste.append(lista_para_decisao[i][1])

        return classe_apos_teste


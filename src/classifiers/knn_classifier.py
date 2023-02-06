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
                    lista_coordenada_treino = lista_vetor_treino[numero_de_coordenada]
                    lista_coordenada_teste = lista_vetor_teste[numero_de_coordenada]
                    coordenada_treino = ((str(lista_coordenada_treino)).strip('[]')).split()
                    coordenada_teste = ((str(lista_coordenada_teste)).strip('[]')).split()
                    for numeros in range(len(coordenada_treino)):
                        lista_distancia_classe = []
                        coordenada_numerica_treino = int(coordenada_treino[numeros])
                        coordenada_numerica_teste = int(coordenada_teste[numeros])
                        distancia += ((coordenada_numerica_treino - coordenada_numerica_teste)**2)**0.5
                lista_distancia_classe.extend([distancia, lista_treinamento_unitária_vetor_classe[1]])
                lista_para_decisao.append(lista_distancia_classe)

        menor_distancia = 10000000000000
        for z in range(len(lista_para_decisao)):
            lista_distancia_classe_analise = lista_para_decisao[z]
            if lista_distancia_classe_analise[0] <= menor_distancia:
                menor_distancia = lista_distancia_classe_analise[0]
                classe_apos_teste = lista_distancia_classe_analise[1]
            else:
                pass


        return classe_apos_teste


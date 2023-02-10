from src.classifiers.knn_classifier import KnnClassifier
from src.classifiers.nc_classifier import NearestCentroidClassifier
from typing import List
import numpy


def accuracy(true_classes: List[str], predicted_classes: List) -> float:
    """  calcula o percentual de acerto """
    predict = numpy.array(predicted_classes)
    true = numpy.array(true_classes)

    return ((predict == true).sum()) / true.shape[0]

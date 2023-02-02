from src.datasets.image_dataset import ImageDataset
from src.classifiers.knn_classifier import KnnClassifier

ds = ImageDataset("data/datasets/img_small/train.txt")
print(ds.size())
print(ds.get(0))

knn = KnnClassifier()
knn.train(ImageDataset("data/datasets/img_small/train.txt"))
knn.predict(ImageDataset("data/datasets/img_small/test.txt"))


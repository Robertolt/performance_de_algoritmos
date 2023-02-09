from src.datasets.image_dataset import ImageDataset
from src.classifiers.knn_classifier import KnnClassifier
from src.datasets.news_dataset import NewsDataset

ds = ImageDataset("data/datasets/img_small/train.txt")
print(ds.size())

knn = KnnClassifier()
knn.train(ImageDataset("data/datasets/img_small/train.txt"))
print(knn.predict(ImageDataset("data/datasets/img_small/test.txt")))



nd = NewsDataset("data/datasets/news-tiny/train.txt")
#print(nd.size())
#print(nd.get(1))

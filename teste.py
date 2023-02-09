from src.datasets.image_dataset import ImageDataset
from src.classifiers.knn_classifier import KnnClassifier
from src.datasets.news_dataset import NewsDataset

ds = ImageDataset("data/datasets/img_small/train.txt")
print(ds.size())
print(ds.get(0))

# knn = KnnClassifier()
# knn.train(ImageDataset("data/datasets/img_small/train.txt"))
# print(knn.predict(ImageDataset("data/datasets/img_small/test.txt")))



nd = NewsDataset("data/datasets/news-tiny/train.txt")
print(nd.size())
print(nd.get(0))
print(len(nd.get(0)[0]))
print((nd.get(1)))
print(len(nd.get(1)[0]))

knn = KnnClassifier()
knn.train(NewsDataset("data/datasets/news-small/train.txt"))
print(knn.predict(NewsDataset("data/datasets/news-small/test.txt")))
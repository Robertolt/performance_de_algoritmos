from src.datasets.image_dataset import ImageDataset

ds = ImageDataset("data/datasets/img_small/train.txt")
print(ds.size())

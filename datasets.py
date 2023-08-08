import glob
import random
import os

import numpy as np
from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import cv2


class ImageDataset(Dataset):
    def __init__(self, root, transforms_=None, unaligned=False, mode='train'):
        self.transform = transforms.Compose(transforms_)
        self.unaligned = unaligned

        self.files_A = sorted(glob.glob(os.path.join(root, '%s/A' % mode) + '/*.*'))  # { list: 1067 }
        self.files_B = sorted(glob.glob(os.path.join(root, '%s/B' % mode) + '/*.*'))

    def __getitem__(self, index):
        a_path = self.files_A[index % len(self.files_A)]
        a_img = cv2.imread(a_path, cv2.IMREAD_GRAYSCALE)
        item_A = self.transform(a_img)

        if self.unaligned:
            b_path = self.files_B[random.randint(0, len(self.files_B) - 1)]
            b_img = cv2.imread(b_path, cv2.IMREAD_GRAYSCALE)
            item_B = self.transform(b_img)

        else:
            b_path = self.files_B[index % len(self.files_B)]
            b_img = cv2.imread(b_path, cv2.IMREAD_GRAYSCALE)
            item_B = self.transform(b_img)

        return {'A': item_A, 'B': item_B}
        # return item_A, item_B

    def __len__(self):
        return max(len(self.files_A), len(self.files_B))


if __name__ == '__main__':
    transforms_ = [transforms.ToPILImage(),
                   transforms.Resize(int(256 * 1.12)),
                   transforms.RandomCrop(256),
                   transforms.RandomHorizontalFlip(),
                   transforms.ToTensor(),
                   transforms.Normalize(0.5, 0.5)]
    my_data = ImageDataset('datasets\horse2zebra', transforms_, unaligned=True)[0]

    dataloader = DataLoader(my_data, batch_size=1, num_workers=1)

    print(1)

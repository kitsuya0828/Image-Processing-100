import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image


def average_pooling(img: np.ndarray, kernel_size: int = 8):
    H, W, C = img.shape
    ks = kernel_size

    out = img.copy()

    for i in range(H // ks):
        for j in range(W // ks):
            for c in range(C):
                out[i*ks: (i+1)*ks, j*ks: (j+1)*ks, c] = np.mean(img[i*ks: (i+1)*ks, j*ks: (j+1)*ks, c]).astype(int)

    return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = average_pooling(img)

    dt_now = datetime.datetime.now()
    save_path = f"{dt_now.strftime('%Y-%m-%d_%H:%M:%S')}.jpg"
    cv2.imwrite(save_dir + save_path, img_result)
    return {"path": save_path}


if __name__ == "__main__":
    sample_path = "../../files/sample/imori.jpeg"
    save_dir = "../../files/"
    result_path = save_dir + solve(sample_path, save_dir)["path"]

    plt.figure(figsize=(12, 3))
    plt.subplot(1, 2, 1)
    plt.title('input')
    sample_image = Image.open(sample_path)
    sample_array = np.asarray(sample_image)
    plt.imshow(sample_array)

    plt.subplot(1, 2, 2)
    plt.title('output')
    result_image = Image.open(result_path)
    result_array = np.asarray(result_image)
    plt.imshow(result_array)
    plt.show()

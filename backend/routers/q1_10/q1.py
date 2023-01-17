import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import datetime


def rgb2bgr(img: np.ndarray):
    return img[..., [2, 1, 0]]


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = rgb2bgr(img)

    dt_now = datetime.datetime.now()
    save_path = f"{dt_now.strftime('%Y-%m-%d_%H:%M:%S')}.jpg"
    cv2.imwrite(save_dir + save_path, img_result)
    return {"path": save_path}


if __name__ == "__main__":
    sample_path = "../../files/sample/imori.png"
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

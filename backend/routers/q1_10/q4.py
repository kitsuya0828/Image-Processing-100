import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image


def bgr2gray(img: np.ndarray):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return y.astype(np.uint8)


def otsu_binarize(img: np.ndarray):
    max_sigma = 0
    max_threshold = 0

    for t in range(1, 255):
        v0 = img[np.where(img < t)]
        m0 = np.mean(v0) if len(v0) > 0 else 0
        w0 = len(v0) / img.size
        v1 = img[np.where(img >= t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0
        w1 = len(v1) / img.size
        sigma = w0 * w1 * ((m0 - m1) ** 2)
        if sigma > max_sigma:
            max_sigma = sigma
            max_threshold = t

    print("threshold : ", max_threshold)
    img[img < max_threshold] = 0
    img[img >= max_threshold] = 255
    
    return img


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = bgr2gray(img)
    img_result = otsu_binarize(img_result)

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
    plt.imshow(result_array, cmap="gray")
    plt.show()

import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image


def mean_filter(img: np.ndarray, kernel_size: int = 3):
    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    # ゼロ埋め
    pad = kernel_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float32)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float32)

    tmp_out = out.copy()

    # フィルタリング
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.mean(tmp_out[y: y + kernel_size, x: x + kernel_size, c])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = mean_filter(img)

    dt_now = datetime.datetime.now()
    save_path = f"{dt_now.strftime('%Y%m%d%H%M%S')}.jpg"
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

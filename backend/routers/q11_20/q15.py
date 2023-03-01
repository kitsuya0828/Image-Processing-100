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


def sobel_filter(img: np.ndarray, kernel_size: int = 3):
    H, W = img.shape

    # ゼロ埋め
    pad = kernel_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float32)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float32)

    out_v = out.copy()
    out_h = out.copy()

    # カーネル
    kernel_v = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)
    kernel_h = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)

    # フィルタリング
    for y in range(H):
        for x in range(W):
            out_v[pad + y, pad + x] = np.sum(kernel_v * out[y: y + kernel_size, x: x + kernel_size])
            out_h[pad + y, pad + x] = np.sum(kernel_h * out[y: y + kernel_size, x: x + kernel_size])

    out_v = np.clip(out_v, 0, 255)
    out_h = np.clip(out_h, 0, 255)

    out_v = out_v[pad: pad + H, pad: pad + W].astype(np.uint8)
    out_h = out_h[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out_v, out_h


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img = bgr2gray(img)
    img_result_v, img_result_h = sobel_filter(img)

    dt_now = datetime.datetime.now()
    save_path_v = f"{dt_now.strftime('%Y%m%d%H%M%S_v')}.jpg"
    cv2.imwrite(save_dir + save_path_v, img_result_v)
    save_path_h = f"{dt_now.strftime('%Y%m%d%H%M%S_h')}.jpg"
    cv2.imwrite(save_dir + save_path_h, img_result_h)
    return {"path": save_path_v}


if __name__ == "__main__":
    sample_path = "../../files/sample/imori.jpeg"
    save_dir = "../../files/"
    result_path_v = save_dir + solve(sample_path, save_dir)["path"]
    result_path_h = result_path_v.replace("_v", "_h")

    plt.figure(figsize=(12, 3))
    plt.subplot(1, 3, 1)
    plt.title('input')
    sample_image = Image.open(sample_path)
    sample_array = np.asarray(sample_image)
    plt.imshow(sample_array)

    plt.subplot(1, 3, 2)
    plt.title('output (Vertical)')
    result_image_v = Image.open(result_path_v)
    result_array_v = np.asarray(result_image_v)
    plt.imshow(result_array_v, cmap="gray")

    plt.subplot(1, 3, 3)
    plt.title('output (Horizontal)')
    result_image_h = Image.open(result_path_h)
    result_array_h = np.asarray(result_image_h)
    plt.imshow(result_array_h, cmap="gray")
    plt.show()

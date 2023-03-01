import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image

def hist_manipulate(img: np.ndarray, target_mean: int=128, target_std: int=52):
    img_mean = np.mean(img)
    img_std = np.std(img)

    out = img.copy()
    
    out = target_std / img_std * (img - img_mean) + target_mean
    out = np.clip(out, 0, 255)
    out = out.astype(np.uint8)
    
    return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = hist_manipulate(img)

    dt_now = datetime.datetime.now()
    save_path = f"{dt_now.strftime('%Y%m%d%H%M%S')}.jpg"
    cv2.imwrite(save_dir + save_path, img_result)
    hist_path = f"{dt_now.strftime('%Y%m%d%H%M%S_hist')}.jpg"
    plt.hist(img_result.ravel(), bins=255, rwidth=0.8, range=(0, 255))
    plt.savefig(save_dir + hist_path)
    return {"path": save_path}


if __name__ == "__main__":
    sample_path = "../../files/sample/imori_dark.jpeg"
    save_dir = "../../files/"
    result_path = save_dir + solve(sample_path, save_dir)["path"]
    hist_path = result_path.replace(".jpg", "_hist.jpg")

    plt.figure(figsize=(12, 3))
    plt.subplot(1, 3, 1)
    plt.title('input')
    sample_image = Image.open(sample_path)
    sample_array = np.asarray(sample_image)
    plt.imshow(sample_array)

    plt.subplot(1, 3, 2)
    plt.title('output')
    result_image = Image.open(result_path)
    result_array = np.asarray(result_image)
    plt.imshow(result_array)

    plt.subplot(1, 3, 3)
    plt.title('histogram')
    hist_image = Image.open(hist_path)
    hist_array = np.asarray(hist_image)
    plt.imshow(hist_array)
    plt.show()

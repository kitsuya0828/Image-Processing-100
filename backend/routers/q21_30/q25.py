import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image

def nearest_neighbor_interpolate(img: np.ndarray, ax: float=1.5, ay: float=1.5):
	H, W, C = img.shape

	aH = int(ay * H)
	aW = int(ax * W)

	# y軸、x軸の元画像インデックス
	y_index = np.round(np.repeat(np.arange(aH) / ay, aW)).astype(np.uint8)
	x_index = np.round(np.tile(np.arange(aW) / ax, aH)).astype(np.uint8)

	# ファンシーインデックスで選択
	out = img[y_index, x_index, :].reshape([aH, aW, -1])

	out = out.astype(np.uint8)

	return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = nearest_neighbor_interpolate(img)

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

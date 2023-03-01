import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image

def bi_linear_interpolate(img: np.ndarray, ax: float=1.5, ay: float=1.5):
	H, W, C = img.shape

	aH = int(ay * H)
	aW = int(ax * W)

	y = np.repeat(np.arange(aH) / ay, aW)
	x = np.tile(np.arange(aW) / ax, aH)

	# y軸、x軸の元画像インデックス（左上）
	y_index = np.floor(y).astype(np.uint8)
	x_index = np.floor(x).astype(np.uint8)

	# 最終行or最終列の場合、(x+1,y), (x, y+1),（x+1, y+1)は存在しない
	y_index[y_index >= H-1] = H-2
	x_index[x_index >= W-1] = W-2
 
	# 左上インデックスとの距離
	# ブロードキャストのため2次元配列に変換
	y_dist = (y - y_index).reshape(aH*aW, 1)
	x_dist = (x - x_index).reshape(aH*aW, 1)

	# ファンシーインデックスで選択
	out = (1 - x_dist) * (1 - y_dist) * img[y_index, x_index, :] \
    	+ x_dist * (1 - y_dist) * img[y_index, x_index + 1, :] \
        + (1 - x_dist) * y_dist * img[y_index + 1, x_index, :] \
        + x_dist * y_dist * img[y_index + 1, x_index + 1, :]

	out = out.reshape([aH, aW, -1])
	out = np.clip(out, 0, 255).astype(np.uint8)

	return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = bi_linear_interpolate(img)

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

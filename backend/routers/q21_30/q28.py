import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image

def affine(img: np.ndarray, a: float=1, b: float=0, c: float=0, d: float=1, tx: int = 0, ty: int = 0):
	H, W, C = img.shape

	# 外枠を黒で囲んだ元画像
	surrounded_img = np.zeros((H+2, W+2, C), dtype=np.float32)
	surrounded_img[1:H+1, 1:W+1, :] = img.copy()

	# out = np.zeros_like(surrounded_img)
	# print(out.shape)

	y = np.repeat(np.arange(1, H+1), W).astype(np.int8)
	x = np.tile(np.arange(1, W+1), H).astype(np.int8)

	# 逆変換で元画像のインデックスを求める
	adbc = a * d - b * c
	x_index = np.round((d * x  - b * y) / adbc).astype(np.int8) - tx
	y_index = np.round((-c * x + a * y) / adbc).astype(np.int8) - ty

	# 元画像の配列外を参照する場合は外枠（黒）とする
	x_index = np.minimum(np.maximum(x_index, 0), W)
	y_index = np.minimum(np.maximum(y_index, 0), H)

	# ファンシーインデックスで取得して3次元配列に変換
	out = surrounded_img[y_index, x_index, :].reshape(H, W, -1)
	
	return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = affine(img, a=1, b=0, c=0, d=1, tx=30, ty=-30)

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

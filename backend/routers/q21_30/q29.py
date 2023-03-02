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

	# 出力画像の高さ・幅
	H_out = np.round(H * d).astype(np.int32)
	W_out = np.round(W * a).astype(np.int32)
	# print(H_out, W_out)

	y = np.repeat(np.arange(1, H_out+1), W_out).astype(np.int32)
	x = np.tile(np.arange(1, W_out+1), H_out).astype(np.int32)

	# 逆変換で元画像のインデックスを求める
	adbc = a * d - b * c
	x_index = np.round((d * x  - b * y) / adbc).astype(np.int32) - tx
	y_index = np.round((-c * x + a * y) / adbc).astype(np.int32) - ty

	# 元画像の配列外を参照する場合は外枠（黒）とする
	x_index = np.minimum(np.maximum(x_index, 0), W+1)
	y_index = np.minimum(np.maximum(y_index, 0), H+1)

	# ファンシーインデックスで取得して3次元配列に変換
	out = surrounded_img[y_index, x_index, :].reshape(H_out, W_out, -1)
	
	return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result_1 = affine(img, a=1.3, b=0, c=0, d=0.8, tx=0, ty=0)

    img_result_2 = affine(img_result_1, a=1, b=0, c=0, d=1, tx=30, ty=-30)

    dt_now = datetime.datetime.now()
    save_path_1 = f"{dt_now.strftime('%Y%m%d%H%M%S_1')}.jpg"
    cv2.imwrite(save_dir + save_path_1, img_result_1)
    save_path_2 = f"{dt_now.strftime('%Y%m%d%H%M%S_2')}.jpg"
    cv2.imwrite(save_dir + save_path_2, img_result_2)
    return {"path": save_path_1}


if __name__ == "__main__":
	sample_path = "../../files/sample/imori.jpeg"
	save_dir = "../../files/"
	result_path_1 = save_dir + solve(sample_path, save_dir)["path"]
	result_path_2 = result_path_1.replace("_1", "_2")

	plt.figure(figsize=(12, 3))
	plt.subplot(1, 3, 1)
	plt.title('input')
	sample_image = Image.open(sample_path)
	sample_array = np.asarray(sample_image)
	plt.imshow(sample_array)

	plt.subplot(1, 3, 2)
	plt.title('output (1)')
	result_image_1 = Image.open(result_path_1)
	result_array_1 = np.asarray(result_image_1)
	plt.imshow(result_array_1)

	plt.subplot(1, 3, 3)
	plt.title('output (2)')
	result_image_2 = Image.open(result_path_2)
	result_array_2 = np.asarray(result_image_2)
	plt.imshow(result_array_2)

	plt.show()

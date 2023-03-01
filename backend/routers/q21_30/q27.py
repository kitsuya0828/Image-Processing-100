import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image

def bi_cubic_interpolate(img: np.ndarray, ax: float=1.5, ay: float=1.5):
	H, W, C = img.shape

	aH = int(ay * H)
	aW = int(ax * W)

	y = np.repeat(np.arange(aH) / ay, aW)
	x = np.tile(np.arange(aW) / ax, aH)

	# y軸、x軸の元画像インデックス（すぐ左上）
	y_index = np.floor(y).astype(np.uint8)
	x_index = np.floor(x).astype(np.uint8)
 
	# 元画像インデックスとの距離
	y_dist_2 = (y - y_index)	# すぐ上
	x_dist_2 = (x - x_index)	# すぐ左
	y_dist_1 = y_dist_2 + 1		# 1番上
	x_dist_1 = x_dist_2 + 1		# 1番左
	y_dist_3 = 1 - y_dist_2		# すぐ下
	x_dist_3 = 1 - x_dist_2		# すぐ右
	y_dist_4 = 1 + y_dist_3		# 1番下
	x_dist_4 = 1 + x_dist_3		# 1番右
	y_dist_list = [y_dist_1, y_dist_2, y_dist_3, y_dist_4]
	x_dist_list = [x_dist_1, x_dist_2, x_dist_3, x_dist_4]

	# 重み関数
	def weight(t: np.ndarray, a: int = -1):
		abs_t = np.abs(t)
		w = np.zeros_like(t)
		near_index = np.where(abs_t <= 1)
		w[near_index] = ((a + 2) * np.power(abs_t, 3) - (a + 3) * np.power(abs_t, 2) + 1)[near_index]
		far_index = np.where((1 < abs_t) & (abs_t <= 2))
		w[far_index] = (a * np.power(abs_t, 3) - 5 * a * np.power(abs_t, 2) + 8 * a * abs_t - 4 * a)[far_index]
		return w
	
	# 重みの和
	w_sum = np.zeros((aH, aW, C), dtype=np.float32)

	out = np.zeros((aH, aW, C), dtype=np.float32)

	for j in range(-1, 3):
		for i in range(-1, 3):
			# 最終2行or最終2列の場合に、周囲の画素が存在するように調整
			ind_x = np.minimum(np.maximum(x_index + i, 0), W-1)
			ind_y = np.minimum(np.maximum(y_index + j, 0), H-1)

			wx = weight(x_dist_list[i+1])
			wy = weight(y_dist_list[j+1])

			w_sum += (wx * wy).reshape([aH, aW, -1])
			out += ((wx * wy).reshape([aH * aW, -1]) * img[ind_y, ind_x, :]).reshape([aH, aW, -1])

	out = np.clip(out, 0, 255).astype(np.uint8)

	return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = bi_cubic_interpolate(img)

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

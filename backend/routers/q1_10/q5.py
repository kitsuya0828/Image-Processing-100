import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image

def BGR2HSV(_img: np.ndarray):
	img = _img.copy() / 255.

	hsv = np.zeros_like(img, dtype=np.float32)

	max_v = np.max(img, axis=2).copy()
	min_v = np.min(img, axis=2).copy()
	min_arg = np.argmin(img, axis=2)

	# Hue
	hsv[..., 0][np.where(max_v == min_v)]= 0
	# if min == B
	ind = np.where(min_arg == 0)
	hsv[..., 0][ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
	# if min == R
	ind = np.where(min_arg == 2)
	hsv[..., 0][ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
	# if min == G
	ind = np.where(min_arg == 1)
	hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300
		
	# Saturation
	hsv[..., 1] = max_v.copy() - min_v.copy()

	# Value
	hsv[..., 2] = max_v.copy()
	
	return hsv


def HSV2BGR(_img: np.ndarray, hsv: np.ndarray):
	img = _img.copy() / 255.

	max_v = np.max(img, axis=2).copy()
	min_v = np.min(img, axis=2).copy()

	out = np.zeros_like(img)

	H = hsv[..., 0]
	S = hsv[..., 1]
	V = hsv[..., 2]

	C = S
	H_ = H / 60.
	X = C * (1 - np.abs( H_ % 2 - 1))
	Z = np.zeros_like(H)

	vals = [[Z,X,C], [Z,C,X], [X,C,Z], [C,X,Z], [C,Z,X], [X,Z,C]]

	for i in range(6):
		ind = np.where((i <= H_) & (H_ < (i+1)))
		out[..., 0][ind] = (V - C)[ind] + vals[i][0][ind]
		out[..., 1][ind] = (V - C)[ind] + vals[i][1][ind]
		out[..., 2][ind] = (V - C)[ind] + vals[i][2][ind]

	out[np.where(max_v == min_v)] = 0
	out = np.clip(out, 0, 1)
	out = (out * 255).astype(np.uint8)

	return out

# 自分の解答（処理速度が遅い）
# def BGR2HSV(_img: np.ndarray):
# 	img = _img.copy() / 255.

# 	hsv = np.zeros_like(img, dtype=np.float32)
# 	H, W, C = img.shape
	
# 	for row in range(H):
# 		for column in range(W):
# 			b, g, r = img[row, column, :]
# 			maxi = max([b, g, r])
# 			mini = min([b, g, r])
# 			# Hue
# 			if maxi == mini:
# 				hue = 0
# 			elif mini == b:
# 				hue = 60 * (g - r) / (maxi - mini) + 60
# 			elif mini == r:
# 				hue = 60 * (b - g) / (maxi - mini) + 180
# 			elif mini == g:
# 				hue = 60 * (r - b) / (maxi - mini) + 300
# 			# Saturation
# 			saturation = maxi - mini
# 			# Value
# 			value = maxi
# 			hsv[row, column, :] = [hue, saturation, value]
# 	return hsv

# def HSV2BGR(_img: np.ndarray, hsv: np.ndarray):
# 	img = _img.copy() / 255.

# 	out = np.zeros_like(img)

# 	H, W, C = hsv.shape
	
# 	for row in range(H):
# 		for column in range(W):
# 			h, s, v = hsv[row, column, :]

# 			b, g, r = img[row, column, :]
# 			maxi = max([b, g, r])
# 			mini = min([b, g, r])

# 			c = s
# 			h_ = h / 60.
# 			x = c * (1 - np.abs(h_ % 2 - 1))
			
# 			if maxi == mini:
# 				out[row, column, :] = np.zeros(3)
# 			elif 0 <= h_ and h_ < 1:
# 				out[row, column, :] = (v - c) * np.ones(3) + np.array([0, x, c])
# 			elif 1 <= h_ and h_ < 2:
# 				out[row, column, :] = (v - c) * np.ones(3) + np.array([0, c, x])
# 			elif 2 <= h_ and h_ < 3:
# 				out[row, column, :] = (v - c) * np.ones(3) + np.array([x, c, 0])
# 			elif 3 <= h_ and h_ < 4:
# 				out[row, column, :] = (v - c) * np.ones(3) + np.array([c, x, 0])
# 			elif 4 <= h_ and h_ < 5:
# 				out[row, column, :] = (v - c) * np.ones(3) + np.array([c, 0, x])
# 			elif 5 <= h_ and h_ < 6:
# 				out[row, column, :] = (v - c) * np.ones(3) + np.array([x, 0, c])

# 	out = np.clip(out, 0, 1)
# 	out = (out * 255).astype(np.uint8)

# 	return out

def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_hsv = BGR2HSV(img)
    img_hsv[:, :, 0] = (img_hsv[:, :, 0] + 180) % 360
    img_result = HSV2BGR(img, img_hsv)

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
	plt.imshow(result_array)
	plt.show()

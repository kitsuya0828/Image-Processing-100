import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime
from PIL import Image

def gamma_correct(img: np.ndarray, c: int=1, g: float=2.2):
	out = img.copy() / 255

	out = (out / c)**(1 / g)
	out *= 255
	out = out.astype(np.uint8)
	
	return out


def solve(file_path: str, save_dir: str = "files/"):
    img = cv2.imread(file_path)

    img_result = gamma_correct(img)

    dt_now = datetime.datetime.now()
    save_path = f"{dt_now.strftime('%Y%m%d%H%M%S')}.jpg"
    cv2.imwrite(save_dir + save_path, img_result)
    return {"path": save_path}


if __name__ == "__main__":
	sample_path = "../../files/sample/imori_gamma.jpeg"
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

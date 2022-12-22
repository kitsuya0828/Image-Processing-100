import cv2

import matplotlib.pyplot as plt
import cv2
import datetime

sample_path = "../../../db/sample/imori_256x256.png"
db_path = "../../../db/"


def rgb2bgr(img):
    return img[..., ::-1]


def solve(file_path, save=True):
    img_orig = cv2.imread(file_path, cv2.COLOR_BGR2RGB)
    img_bgr = rgb2bgr(img_orig)

    if save:
        dt_now = datetime.datetime.now()
        save_path = f"{dt_now.strftime('%Y-%m-%d_%H:%M:%S')}.jpg"
        cv2.imwrite(db_path + save_path, img_bgr)
        return {"path": save_path}
    else:
        return [img_orig, img_bgr]


if __name__ == "__main__":
    img_orig, img_bgr = solve(sample_path, save=False)

    plt.figure(figsize=(12, 3))
    plt.subplot(1, 2, 1)
    plt.title('input')
    plt.imshow(img_orig)
    plt.subplot(1, 2, 2)
    plt.title('answer')
    plt.imshow(img_bgr)
    plt.show()

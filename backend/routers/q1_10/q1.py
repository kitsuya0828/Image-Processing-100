import cv2

import matplotlib.pyplot as plt
import cv2
import datetime

db_path = "../frontend/public/db/"


def rgb2bgr(img):
    return img[..., [2, 1, 0]]


def solve(file_path, save=True):
    img_cv2 = cv2.imread(file_path)
    img = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
    img_bgr = rgb2bgr(img)

    if save:
        dt_now = datetime.datetime.now()
        save_path = f"{dt_now.strftime('%Y-%m-%d_%H:%M:%S')}.jpg"
        cv2.imwrite(db_path + save_path, img_bgr)
        return {"path": save_path}
    else:
        return [img, img_bgr]


if __name__ == "__main__":
    img, img_bgr = solve(
        "../../../frontend/public/db/sample/imori.png", save=False)

    plt.figure(figsize=(12, 3))
    plt.subplot(1, 2, 1)
    plt.title('input')
    plt.imshow(img)
    plt.subplot(1, 2, 2)
    plt.title('output')
    plt.imshow(img_bgr)
    plt.show()

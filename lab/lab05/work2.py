import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

pts_src = np.array([
    [584, 257],   # 左上角
    [1240, 382],   # 右上角
    [912, 1373],  # 右下角
    [0, 944]    # 左下角
], dtype=np.float32)

width = 210 * 3
height = 297 * 3
pts_dst = np.array([
    [0, 0],
    [width - 1, 0],
    [width - 1, height - 1],
    [0, height - 1]
], dtype=np.float32)

M = cv2.getPerspectiveTransform(pts_src, pts_dst)
warped_img = cv2.warpPerspective(img, M, (width, height))

plt.imshow(cv2.cvtColor(warped_img, cv2.COLOR_BGR2RGB))
plt.show()
cv2.imwrite('work2_save.jpg', warped_img)
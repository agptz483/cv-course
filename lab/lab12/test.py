import cv2

image_path = "images/1.jpg"

img = cv2.imread(image_path)

if img is None:
    print("图片读取失败！")
else:
    height, width = img.shape[:2]
    print(f"图像分辨率：{width} × {height}")
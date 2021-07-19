import sys
import numpy as np
import cv2

img = cv2.imread('lenna.bmp')

if img is None:
    print("Image load failed")
    sys.exit()

cv2.namedWindow('img')
cv2.imshow('img', img)

while True:
    keycode = cv2.waitKey()
    # 키보드 i or I 를 입력하면 반전된 이미지를 보여줌
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('img', img)
    # 키보드 Esc or q or Q 를 입력하면 실행을 종료함
    elif keycode == 27 or keycode == ord('q') or keycode == ord('Q'):
        break

cv2.destroyAllWindows()
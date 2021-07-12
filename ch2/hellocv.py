import sys
import cv2

'''
opencv 를 통해 이미지를 불러오고 확인
'''

img = cv2.imread('lenna.bmp') # 불러올 이미지

if __name__ == '__main__':
    print('Hello OpenCV', cv2.__version__)

    if img is None:
        print('Image load failed!')
        sys.exit()

    cv2.namedWindow('image')    # 이미지 창 이름
    cv2.imshow('image', img)    # 창, 이미지 객체
    cv2.waitKey()               # 키 입력을 기다리는 대기함수
                                # imshow waitKey 같이 나옴 (why?)
    cv2.destroyAllWindows()     # 모든 윈도우 제거
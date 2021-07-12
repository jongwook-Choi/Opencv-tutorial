import numpy as np
import cv2

'''
이미지 데이터를 다루기 위해 알아둬야할 다양한 사항 확인 및 정리
'''

# 이미지 모양 확인, grayscale: 2, color: 3
def func1():
    img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Image load failed!")
        return

    print('type(img):', type(img))
    print('img.shape', img.shape)

    if len(img.shape) == 2:
        print('img is a grayscale image')
    elif len(img.shape) == 3:
        print('img is a true color image')

    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

# 행렬 초기화 및 요소접근 방법
# uint: 부호 없는(양수) 4바이트 정수
def func2():
    mat1 = np.empty((480, 640), np.uint8)       # grayscale image
    mat2 = np.zeros((480, 640, 3), np.uint8)    # color image
    mat3 = np.ones((480, 640), np.int32)        # 1's matrix
    mat4 = np.full((480, 640), 0, np.float32)   # Fill with 0.0
    mat5 = np.eye(3, k=0, dtype=int)            # identity matrix

    mat= np.array([[11, 12, 13, 14],
                     [21, 22, 23, 24],
                     [31, 32, 33, 34]]).astype(np.uint8)

    # 행렬 요소별 접근
    mat[0, 1] = 100    # element at x=0, y=1
    mat[2, :] = 200    # element at x=2

    print(mat)

# 얕은 복사, 깊은 복사의 차이 이해
def func3():
    img1 = cv2.imread('cat.bmp')

    img2 = img1                 # 얕은 복사
    img3 = img1.copy()          # 깊은 복사

    img1[:, :] = (0, 255, 255)  # yellow

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    cv2.waitKey()
    cv2.destroyAllWindows()

# 얕은 복사된 객체의 변화는 원본에도 영향을 줌을 보여줌
def func4():
    img1 = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    img2 = img1[200:400, 200:400]           # 얼굴부분 얕은 복사
    img3 = img1[200:400, 200:400].copy()    # 얼굴부분 깊은 복사

    # 얕은 복사를 한 이미지에 밝기 +20
    img2 += 20

    cv2.imshow('img1', img1)    # 얕은 복사 이미지에 적용해도 원본 변화
    cv2.imshow('img2', img2)    # 밝기 +20 한 얼굴 부분
    cv2.imshow('img3', img3)    # 밝기 그대로인 얼굴 부분
    cv2.waitKey()
    cv2.destroyAllWindows()

# 행과 열로 전체 접근
def func5():
    mat1 = np.array(np.arange(12)).reshape(3, 4)

    print(mat1.shape)
    print('mat1:')
    print(mat1)
    # h: row, w: col
    h, w = mat1.shape[:2]

    mat2 = np.zeros(mat1.shape, type(mat1))

    for j in range(h):
        for i in range(w):
            mat2[j, i] = mat1[j, i] + 10

    print('mat2:')
    print(mat2)

# 행렬 연산을 형태를 확인하는 함수
def func6():
    mat1 = np.ones((3, 4), np.int32)    # 1's matrix
    mat2 = np.arange(12).reshape(3, 4)
    mat3 = mat1 + mat2
    mat4 = mat2 * 2

    print("mat1:", mat1, sep='\n')
    print("mat2:", mat2, sep='\n')
    print("mat3:", mat3, sep='\n')
    print("mat4:", mat4, sep='\n')


if __name__ == '__main__':
    func1()
    #func2()
    #func3()
    #func4()
    #func5()
    #func6()
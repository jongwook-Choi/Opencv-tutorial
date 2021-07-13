import numpy as np
import cv2


def camera_in():
    """
    카메라 장치를 사용하는 함수
    카메라로부터 받아온 매 프레임에 대해 반전 영상 생성
    """
    cap = cv2.VideoCapture(0)   # 컴퓨터에 연결되어 있는 기본 카메라 사용: 0

    # 카메라 장치 사용 가능여부 확인
    if not cap.isOpened():
        print("Camera open failed")
        return
    # CAP_PROP_FRAME_WIDTH: 비디오 프레임의 가로 크기
    print("Frame width:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    #CAP_PROP_FRAME_HEIGHT: 비디오 프레임의 세로 크기
    print("Frame height", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    while True:
        ret, frame = cap.read() # 비디오의 한 프레임씩 읽기
        # ret: 프레임 읽기 성공(True) 실패(False)
        # frame: 읽은 프레임
        if not ret:
            break

        inversed = ~frame    # 프레임 반전

        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        # 10: 10초 동안 대기
        # 27: ESC
        if cv2.waitKey(10) == 27:
            break

    cv2.destroyAllWindows()

def video_in():
    """
    동영상을 입력으로 받아 반전해 출력하는 함수
    """
    cap = cv2.VideoCapture('stopwatch.avi')

    if not cap.isOpened():
        print("Video open failed")
        return

    print("Frame width:", int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print("Frame height:", int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # CAP_PROP_FRAME_COUNT: 비디오 파일의 전체 프레임 수
    print("Frame count:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    # CAP_PROP_FPS: 초당 프레임 수
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("FPS:", fps)

    # fps 값으로부터 각 프레임 사이의 시간 간격 delay(밀리초 단위)
    delay = round(1000 / fps)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        inversed = ~frame

        cv2.imshow('frame', frame)
        cv2.imshow('inverse', inversed)

        if cv2.waitKey(delay) == 27:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    #camera_in()
    video_in()

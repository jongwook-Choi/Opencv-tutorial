import numpy as np
import cv2

def drawLines():
    """
    영상에 선 그리기 함수 나열
    특징점을 표시할 때 자주 사용할 듯 -> drawMaker
    """

    img = np.full((400, 400, 3), 255, np.uint8)

    # 영상 위에 직선을 그리는 함수
    # cv2.line(img, pt1, p2, color, thickness, lineType, shift)
    # img: 입출력 영상
    # pt1: 시작점
    # pt2: 끝정
    # color: 선 색상(또는 밝기)
    # thickness: 선 두께
    cv2.line(img, (50, 50), (200, 50), (0, 0, 255))
    cv2.line(img, (50, 100), (200, 100), (255, 0, 255), 3)
    cv2.line(img, (50, 150), (200, 150), (255, 0, 0), 10)
    # lineType: 선 타입
    # LINE_4: 4방향 연결
    # LINE_8: 8방향 연결
    # LINE_AA: 안티에일리어싱(anti-aliasing) -> 직선을 부드럽게 그려줌
    # (shift: 그리기 좌표값의 축소 비율)
    cv2.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv2.LINE_4)
    cv2.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv2.LINE_8)
    cv2.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv2.LINE_AA)

    # 영상 위에 화살표를 그리는 함수
    # cv2.arrowedLine(img, pt1, pt2, color, thickness, line_type, shift, tipLength)
    # img, pt1, pt2,color, thickness, line_type shift 동일
    cv2.arrowedLine(img, (50, 200), (150, 200), (0, 0, 255), 1)
    cv2.arrowedLine(img, (50, 250), (350, 250), (255, 0, 255), 1)
    # tipLength: 전체 직선 길이에 대한 화살표 길이의 비율율
    cv2.arrowedLine(img, (50, 300), (350, 300), (255, 0, 0), 1, cv2.LINE_8, 0, 0.05)

    # 직선 그리기 함수를 이용하여 다양한 모양의 마커를 그리는 함수
    # cv2.drawMarker(img, position, color, markerType, markerSize, thickness, line_type)
    # img, color, thickness, line_type 동일
    # position: 마커 출력 위치
    # markerType: 마커 종류
    # cv2.MARKER_CROSS: 십자가 모양(+ 모양)
    cv2.drawMarker(img, (50, 350), (0, 0, 255), cv2.MARKER_CROSS)
    # cv2.MARKER_TILTED_CROSS: 45도 회전된 십자가 모양(x 모양)
    cv2.drawMarker(img, (100, 350), (0, 0, 255), cv2.MARKER_TILTED_CROSS)
    # cv2.MARKER_STAR: 위 두 모양이 합쳐진 모양
    cv2.drawMarker(img, (150, 350), (0, 0, 255), cv2.MARKER_STAR)
    # cv2.MARKER_DIAMOND: 마름모 모양
    cv2.drawMarker(img, (200, 350), (0, 0, 255), cv2.MARKER_DIAMOND)
    # cv2.MARKER_SQUARE: 정사각형 모양
    cv2.drawMarker(img, (250, 350), (0, 0, 255), cv2.MARKER_SQUARE)
    # cv2.MARKER_TRIANGLE_UP: 위로 뾰족한 삼각형
    cv2.drawMarker(img, (300, 350), (0, 0, 255), cv2.MARKER_TRIANGLE_UP)
    # cv2.MARKER_TRIANGLE_DOWN: 아래로 뾰족항 삼각형
    cv2.drawMarker(img, (350, 350), (0, 0, 255), cv2.MARKER_TRIANGLE_DOWN)

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def drawPolys():
    """
    영상에 도형을 그리는 함수 나열
    """
    img = np.full((400, 400, 3), 255, np.uint8)

    # 영상에서 사각형을 그리는 함수
    # cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
    # img, color, lineType, shift 동일
    # pt1: 사각형 꼭지점 좌표, point 객체
    # pt2: pt1과 대각 방향에 있는 사각형 꼭지점 좌표, point 객체
    # thickness: default=1, -1 이면 채움
    cv2.rectangle(img, (50, 50), (150, 100), (0, 0, 255), 2)
    cv2.rectangle(img, (50, 150), (150, 200), (0, 0, 128), -1)

    # 영상에 원을 그리는 함수
    # cv2.circle(img, center, radius, color, thickness, lineType, shift)
    # img, color, thickness, lineType, shift 동일
    # center: 원의 중심
    # radius: 원의 반지름
    cv2.circle(img, (300, 120), 30, (255, 255, 0), -1, cv2.LINE_AA)
    cv2.circle(img, (300, 120), 60, (255, 0, 0), 3, cv2.LINE_AA)

    # 영상에 타원을 그리는 함수
    # cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness, lineType, shift)
    # img, center, color, thickness, lineType, shift 동일
    # axes: 타원의 반지름, Size(x_축 반지름, y축 반지름)
    # startAngle: 타원 호의 시작 각도(x축 기준, 시계 방향)
    # endAngle: 타원 호의 끝 각도(x축 기준, 시계 방향)
    cv2.ellipse(img, (120, 300), (60, 30), 20, 0, 270, (255, 255, 0), cv2.FILLED, cv2.LINE_AA)
    cv2.ellipse(img, (120, 300), (100, 50), 20, 0, 360, (0, 255, 0), 2, cv2.LINE_AA)

    # pts: 다각형의 꼭짓점 좌표
    pts = np.array([[250, 250], [300, 250], [300, 300], [350, 300], [350, 350], [250, 350]])
    # cv2.polylines(img, pts, isClosed, color, thickness, lineType, shift)
    # img, color, thickness, lineType, shift 동일
    # pts: 다각형 외각 점들의 좌표 배열, 주로 vector<Point> 타입
    # isClose: 다각형이 닫혀 있는지를 나타내는 플래그
    cv2.polylines(img, [pts], True, (255, 0, 255), 2)

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def drawText1():
    """
    영상에 문자열을 출력하는 방법 나열
    """
    img = np.full((500, 800, 3), 255, np.uint8)
    # 영상에 정해진 폰트로 문자열을 출력하는 함수
    # cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
    # img, color, thickness, lineType 동일
    # text: 출력할 문자열
    # org: 영상에서 문자열을 출력할 위치의 좌측 하단 좌표
    # fontFace: 폰트 종류
    # fontScale: 폰트 크기 확대/축소 비율
    # bottomLeftOrigin: 이 값이 true이면 영상의 좌측 하단을 원점으로 간주, false일 경우 우측 하단이 원점
    cv2.putText(img, "FONT_HERSHEY_SIMPLEX", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_PLAIN", (20, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_DUPLEX", (20, 150), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_COMPLEX", (20, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))
    cv2.putText(img, "FONT_HERSHEY_TRIPLEX", (20, 250), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))
    cv2.putText(img, "FONT_HERSHEY_COMPLEX_SMALL", (20, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0))
    cv2.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (20, 350), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX", (20, 400), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 255))
    cv2.putText(img, "FONT_HERSHEY_COMPLEX | FONT_ITALIC", (20, 450), cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (255, 0, 0))

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def drawText2():
    """
    영상의 중앙에 문자열과 도형 출력하는 함수
    """
    img = np.full((200, 640, 3), 255, np.uint8)

    text = "Hello, OpenCV"
    fontFace = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 2.0
    thickness = 1

    sizeText, _ = cv2.getTextSize(text, fontFace, fontScale, thickness)

    org = ((img.shape[1] - sizeText[0]) // 2, (img.shape[0] + sizeText[1]) // 2)
    cv2.putText(img, text, org, fontFace, fontScale, (255, 0, 0), thickness)
    cv2.rectangle(img, org, (org[0] + sizeText[0], org[1] - sizeText[1]), (0, 255, 0), 1)

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    drawLines()
    #drawPolys()
    #drawText1()
    #drawText2()
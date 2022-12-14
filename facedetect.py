import cv2
def imgDetector(img, cascade):
    img = cv2.resize(img, dsize=None, fx=1.0, fy=1.0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    results = cascade.detectMultiScale(gray,  # 입력 이미지
                                       scaleFactor=1.5,  # 이미지 피라미드 스케일 factor
                                       minNeighbors=5,  # 인접 객체 최소 거리 픽셀
                                       minSize=(20, 20)  # 탐지 객체 최소 크기
                                       )
    for box in results:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=2)

    # 사진 출력
    cv2.imshow('facenet', img)
    cv2.waitKey(10000)

cascade_filename = 'haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_filename)
img = cv2.imread('mjf2.jpg')
imgDetector(img,cascade)

cv2.waitKey()
cv2.destroyAllWindows()

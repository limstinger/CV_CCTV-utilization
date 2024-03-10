import cv2

# 캡처 초기화
cap = cv2.VideoCapture('rtsp://210.99.70.120:1935/live/cctv005.stream')

# 코덱 정의 및 videoWriter 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# UI 컨트롤 플래그
start_recording = False
zoom_scale = 1.0 # 줌 스케일 확대 / 축소를 위한 초기값

# 이미지 서브트랙션을 위한 초기 설정
ret, frame = cap.read()
first_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
first_frame_gray = cv2.GaussianBlur(first_frame_gray, (21, 21), 0)

# 이전 프레임을 저장할 변수
img_prev = first_frame_gray.copy()

while True:
    # 프레임별 캡처
    ret, frame = cap.read()

    if not ret:
        print("프레임을 가져오지 못했습니다.")
        break

    # 현재 프레임을 회색조로 변환 및 블러 적용
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if img_prev is None:
        img_prev = gray.copy()
        continue

    # 이미지 차이 계산
    img_diff = cv2.absdiff(img_prev, gray)
    img_prev = gray.copy()

    # 줌 스케일에 따라 프레임의 ROI를 선택
    height, width = frame.shape[:2]
    centerX, centerY = int(width / 2), int(height / 2)
    radiusX, radiusY = int(centerX / zoom_scale), int(centerY / zoom_scale)
    minX, maxX = centerX - radiusX, centerX + radiusX
    minY, maxY = centerY - radiusY, centerY + radiusY

    # 프레임을 클리핑하여 ROI를 추출하고 확대
    cropped = frame[minY:maxY, minX:maxX]
    resized_cropped = cv2.resize(cropped, (width, height), interpolation=cv2.INTER_LINEAR)

    # 줌된 영상과 이미지 차이를 결합
    img_diff_bgr = cv2.cvtColor(img_diff, cv2.COLOR_GRAY2BGR)  # 서브트랙션 결과를 BGR로 변환
    img_diff_resized = cv2.resize(img_diff_bgr, (width, height), interpolation=cv2.INTER_LINEAR)  # 서브트랙션 결과의 크기 조정
    combined = cv2.hconcat([resized_cropped, img_diff_resized])  # 결합

    # 녹화 중 표시 추가
    if start_recording:
        # 녹화 중임을 나타내는 빨간색 원을 좌측 상단에 그립니다.
        cv2.circle(combined, (25, 25), 5, (0, 0, 255), -1)
        out.write(frame)

    # 조정된 프레임과 이미지 차이를 함께 표시
    cv2.imshow('CCTV and Image Subtraction', combined)

    # 키 입력을 위한 대기
    key = cv2.waitKey(1)

    # 확대
    if key == ord('['):
        zoom_scale = min(zoom_scale + 0.1, 4)   # 최대 4배까지 확대 가능하도록 설정

    # 축소
    if key == ord(']'):
        zoom_scale = max(zoom_scale - 0.1, 1)   # 최소 1배(원본 크기)로 축소 가능

    # 스페이스바가 눌리면 녹화 시작/중지
    if key == ord(' '):
        start_recording = not start_recording
        if start_recording:
            print("녹화 시작")
        else:
            print("녹화 중지")

    # ESC를 누르면 종료
    if key == 27:
        break

# 모든 작업 완료 후, 캡처 해제
cap.release()
out.release()
cv2.destroyAllWindows()













# CV_CCTV-utilization

<br>

 ## **Introduction**

CCTV의 영상을 CV를 활용하여 녹화 기능(Record)과 영상 확대와 축소, 이미지 서브트랙션(Image Subtraction)의 기능을 구현하고자 한다.

## **Developer**

* 임민규(Lim Mingyu)

## **Release**

[공공데이터포털](https://www.data.go.kr/data/15063717/fileData.do)를 통해 해당 CCTV 영상을 가져올 수 있는 IP주소(RTSP)를 가져온다.

* **CV**로 CCTV의 영상을 여러 형태로 편집

## **Set Up & Prerequisites**

* Python >= 3.9
* Install python pip.
  * You may need to install first:`python -m pip install opencv-python`
* Data(RTSP):
  * [공공데이터포털](https://www.data.go.kr/data/15063717/fileData.do)
 
## **Description**
 **코드에 대한 내용은 주석을 참고**

 * 영상 녹화
   * 영상 녹화를 위해 코덱 정의 및 videoWriter 객체를 생성
     ```bash
     fourcc = cv2.VideoWriter_fourcc(*'XVID')
     out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

   * 영상 녹화 중인지 확인하기 위해 체크할 위젯 생성
     ```bash
     if start_recording:
        cv2.circle(combined, (25, 25), 5, (0, 0, 255), -1)
        out.write(frame)
     
   * 스페이스바를 통해 영상 녹화 시작 / 종료 조절
     ```bash
      if key == ord(' '):
         start_recording = not start_recording
         if start_recording:
            print("녹화 시작")
         else:
             print("녹화 중지")

   <p align="center">
  <img src="https://github.com/limstinger/CV_CCTV-utilization/assets/113160281/ff84007e-6313-4390-a40c-a228addacf5a">
</p>
   
 * 영상 확대 / 축소
   * 영상의 중앙점을 기준으로 확대 또는 축소할 영역을 선택 후 영상 조정 시 사용할 보간 방법을 선택
     ```bash
     height, width = frame.shape[:2]
     centerX, centerY = int(width / 2), int(height / 2)
     radiusX, radiusY = int(centerX / zoom_scale), int(centerY / zoom_scale)
     minX, maxX = centerX - radiusX, centerX + radiusX
     minY, maxY = centerY - radiusY, centerY + radiusY

     cropped = frame[minY:maxY, minX:maxX]
     resized_cropped = cv2.resize(cropped, (width, height), interpolation=cv2.INTER_LINEAR)
     
   * '[' 눌렀을 때 확대, ']'를 누르면 축소
     ```bash
     if key == ord('['):
        zoom_scale = min(zoom_scale + 0.1, 4)   
     if key == ord(']'):
        zoom_scale = max(zoom_scale - 0.1, 1)   
     
   <p align="center">
  <img src="https://github.com/limstinger/CV_CCTV-utilization/assets/113160281/9e5fa3e5-3bea-4ebf-9cbf-01f4a0c072de">
</p>
   
 * 영상 Image subtraction
   * Image subtraction을 하기 위해 초기 설정
     ```bash
     ret, frame = cap.read()
     first_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     first_frame_gray = cv2.GaussianBlur(first_frame_gray, (21, 21), 0)

     img_prev = first_frame_gray.copy() # 이전 프레임을 저장하기 위해

   처리할 데이터를 줄이고 계산을 단순화하기 위해 cv2.COLOR_BGR2GRAY 사용

   * 이미지 차이 계산
     ```bash
     img_diff = cv2.absdiff(img_prev, gray)
     img_prev = gray.copy()
   
   * 기존 영상과 이미지 서브트랙션한 영상을 비교할 수 있도록 옆에 배치
     ```bash
     combined = cv2.hconcat([resized_cropped, img_diff_resized])  # 결합
     
   <p align="center">
  <img src="https://github.com/limstinger/CV_CCTV-utilization/assets/113160281/2beac98d-e019-4e8d-9990-c160ca919f5b">
</p>
   





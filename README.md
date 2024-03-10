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
   * 기존 영상과 이미지 서브트랙션한 영상을 비교할 수 있도록 옆에 배치
     ```bash
     combined = cv2.hconcat([resized_cropped, img_diff_resized])  # 결합
     
   <p align="center">
  <img src="https://github.com/limstinger/CV_CCTV-utilization/assets/113160281/2beac98d-e019-4e8d-9990-c160ca919f5b">
</p>
   





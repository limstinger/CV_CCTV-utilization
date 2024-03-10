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
* 녹화 기능
비디오를 녹화하기 위한 코덱 정의 및 videoWriter 객체 생성<br>
`fourcc = cv2.VideoWriter_fourcc(*'XVID')`<br>
`out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))`
 



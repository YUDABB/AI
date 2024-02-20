## 상세 내용

- 평소 수업을 들으며 출석을 하고 도망가는 학생, 대리 출석을 해주는 학생을 보았습니다.
- 하지만 교수님은 수업을 하시느라 그런 학생들을 전부 신경 써주지 못하셨고 저희는 수업에 도움이 되고자 출튀(출석 후 도망) 방지 시스템을 만들었습니다.
- **구성도**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/723aeb70-94d7-4deb-a98d-fc7f0d6611bb/e23e811c-057b-4180-a6d9-e84c063fce1f/Untitled.png)

- **실행 화면**

![                         아두이노](https://prod-files-secure.s3.us-west-2.amazonaws.com/723aeb70-94d7-4deb-a98d-fc7f0d6611bb/3f9ca449-5f17-4769-87fb-a854b90cf43b/Untitled.png)

                         아두이노

![                       AI 카메라](https://prod-files-secure.s3.us-west-2.amazonaws.com/723aeb70-94d7-4deb-a98d-fc7f0d6611bb/19bd225c-a8cb-4a86-a073-dcb3a00d1d86/Untitled.png)

                       AI 카메라

![                   라즈베리파이](https://prod-files-secure.s3.us-west-2.amazonaws.com/723aeb70-94d7-4deb-a98d-fc7f0d6611bb/849377f1-65c6-42b0-a99c-2469d5d37c9b/Untitled.png)

                   라즈베리파이

- **기능**
    - 학생이 AI 카메라에 다가오면 AI 카메라가 학생인지 아닌지 판단 후 출석 체크를 한다.
    - 정해진 시간에 AI 카메라에 얼굴 인식을 해야 출석으로 인정된다.
    - 수업이 끝난 후 정해진 시간에 얼굴 인식을 하고 나가야 완전한 출석으로 표시된다.
    - 수업 중간에 나갈 경우 얼굴 인식을 하고 나간 경우 외출로 표시되며 그 후 10분 안에 다시 들어와야 결석이 되지 않는다.
- **기대 효과**
    - 정해진 시간에 AI 카메라에 얼굴을 인식해야 하기 때문에 출석 후 도망 가는 걸 방지 할 수 있습니다.

## 🛠️ 기술 및 라이브러리

- Django
- Arduino
- HTML,CSS
- SQLite
- Raspberry pi

## 📱 구현한 기능

- 로그인/회원가입 페이지 구현
- 교수님 과목별 출석 체크를 확인, 수정 페이지 구현
- 출석 후 도망가는 학생 리스트 페이지 구현
- 학생 출석 체크 페이지 구현
- 게시판 기능 구현 - 공지사항 게시판

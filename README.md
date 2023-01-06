# 페이하이 과제 - 고객은 본인의 소비내역을 기록,관리하고 싶습니다.
## 개요
가계부를 만들어 수입과 소비내역을 관리(작성, 수정, 삭제)하는 어플리케이션입니다.
<br>
Python과 Django와 RDB를 이용하여 가계부 API를 만들었습니다.

- 개발기간: 2023.01.04 - 2023.01.07
- 개발인원: 박정용

# 사용 기술

<img src="https://img.shields.io/badge/Python-3.9-%233776AB?&logo=python&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/Django-4.0.5-%23092E20?&logo=Django&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/MySQL-5.7-%234479A1?&logo=MySQL&logoColor=white"/>&nbsp;

## 프로젝트 실행 방법

- 사전에 Git, Python, MySQL이 설치되어있어야 합니다.

```shell
# 레포지토리 클론
$ git clone https://github.com/WorkYong/WORK_EXAM.git

# 접속
$ cd WORK_EXAM

# 패키지 설치
$ pip install -r requirements.txt

# 데이터베이스 생성
mysql> create database 데이터베이스명 character set utf8mb4 collate utf8mb4_general_ci;

# 프로젝트 실행
$ python manage.py runserver 0:8000

# server start : http://localhost:8000
```

## 프로젝트 구조

### DB모델링

![Untitled](https://user-images.githubusercontent.com/102202607/210957341-85e6b6be-078d-49bd-8624-ec94a4c09cc8.png)

## 구현 기능에 대한 소개

1.  회원

    - 회원 가입하기
      ** 필수 요청값(이름, 이메일, 휴대폰번호, 비밀번호) 요청 값으로 받습니다.
      
      **※ 사용자의 이름의 경우**
      
      한글로 이루어져야만 하며 2~5장 이내로 설정했습니다.
      
      **※ 사용자의 email의 경우**

      "@" 가 포함되어 있어야 하며 "." 이 포함되어 있어야 하도록 설정했습니다.
      
      **※ 사용자의 핸드폰번호의 경우**

      "-"를 포함하고 요청을 보냅니다.
      앞자리는 3자리로 이루어져 있어야 하며 중간 자리는 3자리 또는 4자리 숫자 끝자리는 4자리 숫자로 설정해두었습니다.
      
      **사용자의 이메일, 전화번호는 에러 처리되어 있어 데이터가 중복되는 경우에는 가입할 수 없습니다.**
      
      **비밀번호는 bcrypt를 사용하여 암호화 처리하였습니다.**
      
      **요청한 값이 유효성검사를 끝내고 통과되면 회원가입 완료됩니다.**
      
      

    - 회원 로그인 하기
      ** 필수 요청값(이메일, 비밀번호) 요청 값으로 받습니다
      이메일과 비밀번호가 일치하게 되면 JWT 토큰을 발행합니다.
      틀리게 되면 INVAILD_USER라는 문구가 발생합니다.
    
    - 회원 로그아웃 하기(미구현)

    - 회원 탈퇴하기(로그인시만가능)
      ** 필수 요청값(user_id, is_active)**
      사용자의 ID번호와 
      

2.  가계부(로그인시만가능)

    - 가계부 생성하기

    - 가계부 내역 수정하기

    - 가계부 내역 삭제하기

    - 가계부 원하는내역 조회하기

3.  가계부 상세내역(로그인시만가능)

    - 가계부 상세내역 생성하기

    - 가계부 상세내역 수정하기

    - 가계부 상세내역 삭제하기

    - 가계부 상세내역 조회하기

    - 가계부 상세내역 공유해서 단축URL 만들기

    - 가계부 상세내역 복제하기

4.  테스트코드

---

       요청과 응답에 대한 자세한 결과, 데이터 타입은 API docs를 참고해 주십시오.

## API doc

박정용 - [https://documenter.getpostman.com/view/22727251/2s83zfQ5Ti]()

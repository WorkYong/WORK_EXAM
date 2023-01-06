# 페이하이 과제 - 고객은 본인의 소비내역을 기록/관리하고 싶습니다. 아래의 요구사항을 만족하는 DB 테이블과 REST API를 만들어주세요.

## 개요

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

![image]

## 구현 기능에 대한 소개

1.  회원

    - 회원 가입하기

    - 회원 로그인 하기

    - 회원 로그아웃 하기

    - 회원 탈퇴하기(로그인시)

2.  가계부(로그인시)

    - 가계부 생성하기

    - 가계부 내역 수정하기

    - 가계부 내역 삭제하기

    - 가계부 원하는내역 조회하기

3.  가계부 상세내역(로그인시)

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

# 페이하이 과제 - 고객은 본인의 소비내역을 기록,관리하고 싶습니다.
## 개요
가계부를 만들어 수입과 소비내역을 관리(작성, 수정, 삭제)하는 어플리케이션입니다.
<br>
Python과 Django와 RDB를 이용하여 가계부 API를 만들었습니다.

- 개발기간: 2023.01.04 - 2023.01.07
- 개발자: 박정용

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

# Starting development server at http://0:8000/
```

## 프로젝트 구조

### DB모델링

![Untitled](https://user-images.githubusercontent.com/102202607/210957341-85e6b6be-078d-49bd-8624-ec94a4c09cc8.png)

## 구현 기능에 대한 소개
<details>
<summary>1.  회원</summary>

    
- 회원 가입하기
```shell
※ 필수 요청값(이름, 이메일, 휴대폰번호, 비밀번호) 요청 값으로 받습니다.

※ 사용자의 이름의 경우**

한글로 이루어져야만 하며 2~5장 이내로 설정했습니다.

※ 사용자의 email의 경우**

"@" 가 포함되어 있어야 하며 "." 이 포함되어 있어야 하도록 설정했습니다.

※ 사용자의 핸드폰번호의 경우**

"-"를 포함하고 요청을 보냅니다.

앞자리는 3자리로 이루어져 있어야 하며 중간 자리는 3자리 또는 4자리 숫자 끝자리는 4자리 숫자로 설정해두었습니다.

※사용자의 이메일, 전화번호는 에러 처리되어 있어 데이터가 중복되는 경우에는 가입할 수 없습니다.**※

※비밀번호는 bcrypt를 사용하여 암호화 처리하였습니다.**※

※요청한 값이 유효성검사를 끝내고 통과되면 회원가입 완료됩니다.
```
      
- 회원 로그인 하기
```shell      
※ 필수 요청값(이메일, 비밀번호) 요청 값으로 받습니다.
  이메일과 비밀번호가 일치하게 되면 로그인이 완료되며 JWT 토큰을 발행합니다.
  이메일 혹은 비밀번호가 불일치시 INVAILD_USER라는 문구가 발생합니다.
```
- 회원 로그아웃 하기(미구현)

- 회원 탈퇴하기(로그인시만가능)
```shell
※ 필수 요청값(user_id) 요청 값으로 받습니다.
  사용자에서 요청한 user_id의 상태 값(is_active)가 0값으로 변환되며
  DELETE라는 메세지가 반한되며 탈퇴 처리 됩니다.(실제 탈퇴가 아닌 DB상의 상태 값의 변환처리 합니다.)
```
</details>

<details>
<summary>2. 가계부(로그인시만가능)</summary>

- 가계부 생성하기
```shell    
※ 필수 요청값(book_name) 요청 값으로 받습니다.
  한 아이디에 중복된 이름의 가계부를 만들 수는 없습니다(상세내역은 상관 없습니다.)
  ex)가계부의 이름이기 떄문에 user_id=1, book_name=절약하자, user_id=1, book_name=절약하자(중복이라 안댐) 
  (단,user_id=1 book_name=절약하자 , user_id=2 book_name=절약하자 일 시 가능합니다)
```
- 가계부 내역 수정하기
```shell
※ 필수 요청값(book_id, book_name) 요청 값으로 받습니다.
  book_id와 book_name이 수정이 완료되면 CHANGE라는 메시지와 함꼐 수정완료됩니다.
  요청된 book_id가 DB에 없는 번호라면 에러값(Book_DoesNotExist)을 반환합니다.
```
- 가계부 내역 삭제하기
```shell
※ 필수 요청값(book_id) 요청 값으로 받습니다.
  book_id의 값으로 요청할 시 요청된 book_id의 상태 값(is_deleted)가 0으로 변환되며
  삭제일자(deleted_at)가 현재 날짜와시간과 함께 기록됩니다.
  DELETE라느 메시지와 함께 삭제처리 됩니다.(실제 삭제가 아닌 DB상의 상태 값의 변환처리 합니다.)
  
```
    
- 가계부 원하는내역 조회하기       
```shell  
  자신이 로그인 된 Token정보로 로그인을 확인하고 user_id 정보를 통하여 조회시 가져옵니다.
  로그인이 안되어 있을시 조회가 불가능하며  에러 값(INVALID_TOKEN)을 반환합니다.
```
</details>

<details>
<summary>3. 가계부 상세내역(로그인시만 가능)</summary>

- 가계부 상세내역 생성하기
```shell
※필수 요청값(title, date, memo, description, amount, balance, book_id) 요청 값으로 받습니다.
  
  지정된 키 값(title, date, memo, description, amount, balance, book_id)이 아닌 다른 키
  
  값 이나 누락된 키 값이 있으면 에러 값(KEY_ERROR)를 발생 시킵니다.
  
  SUCCESS라는 메시지와 함께 생성됩니다.
```
    
- 가계부 상세내역 수정하기
```shell
  ※필수 요청값(record_id, amount, memo) 요청 값으로 받습니다.
  
    존재하지않는 record_id면 BookRecord_DoesNotExist 에러 값을 반환합니다.
  
    유효성검사가 다끝나면 CHANGE라는 메시지와 함꼐 (amount, memo) 값이 수정됩니다
```    
- 가계부 상세내역 삭제하기
```shell
※필수 요청값(record_id) 요청 값으로 받습니다.
  
  존재하지않는 record_id면 BookRecord_DoesNotExist 에러 값을 반환합니다.
  
  유효성검사가 다 끝나면 DELETE라는 메시지와 함께 요청된 record_id의 상태 값(is_delete)값이 0으로 바뀌며 동시에 삭제일자(deleted_at)에
  
  현재시간과 날짜가 기록되며 삭제처리 됩니다.((실제 삭제가 아닌 DB상의 상태 값의 변환처리 합니다.))
 
```  
- 가계부 상세내역 조회하기
```shell
※필수 요청값(book_id, is_deleted, serial_no) QueryStringParameter를 요청 값으로 받습니다.
  
  요청된 QueryStringParameter값의 따라 원하는 정보를 조회할 수 있습니다. 
  
  그리고 GET METHOD의 단점인 URL에 그대로 노출되어 무분별하게 URL값을 변경하여 조회할 수 있는 사항이 우려되어
  
  uuid라는 모듈을 통하여 serial_no를 생성하였습니다. uuid 모듈은 랜덤하게 16자리에 숫자가 랜덤하게 생성시킵니다. 
  
  QueryStringParameter 속에 앞서 설명한 serial_no를 넣어 보안적 측면을 고려하였습니다.
```
- 가계부 상세내역 공유해서 단축URL 만들기(단축시간 만료는 미구현)
```shell  
QueryStringParameter로 상세내역을 조회하게 되면 그 동시에 단축URL 결과 값을 반환합니다.
QueryStringParameter의 값이 변화하기 문에 URL이 겹치지 않습니다.
```  
- 가계부 상세내역 복제하기
</details>
<details>
<summary>4. 테스트 케이스에 따른 요청과 응답에 대한 결과</summary>
<div markdown="1">
<ul>
  <li>
    <p>회원가입</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005451-718c2c78-0803-42f0-9af3-bcbeb5be6700.png">
  </li>
  <li>
    <p>로그인</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005459-b0783501-cf81-48f4-bfe4-de6dd1e7cca0.png">
  </li>
  <li>
    <p>회원 탈퇴(soft delete)</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005465-aff65ff9-428b-4f70-97b7-b18b2c6e38a5.png">
  </li>
  <li>
    <p>가계부 생성</p>
    <img width="800" alt="image" src="https://user-images.githubusercontent.com/102202607/211005469-ff41cc63-ae6e-4f32-bd67-25ddd505683d.png">
  </li>
  <li>
    <p>가계부 조회</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005474-6446edc7-30ea-4485-b94f-7f957157daf7.png">
  </li>
  <li>
    <p>가계부 수정</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005478-cd58d795-cf0a-4e11-b229-8a9fbc334bca.png">
  </li>
  <li>
    <p>가계부 삭제(soft_delete)</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005481-61dec8aa-8a0c-4c44-97b3-37ac05a122be.png">
  </li>
  <li>
    <p>가계부 상세내역 생성</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005482-953ac4cf-b28b-40c9-9c8f-61c426de1df6.png">
  </li>
  <li>
    <p>가계부 상세내역 조회</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005488-e7d29739-913c-44d0-a9f5-35e767a25377.png">
  </li>
  <li>
    <p>가계부 상세내역 수정</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005490-78ee1c10-377f-4b74-bc08-dd929de303f5.png">
  </li>
  <li>
    <p>가계부 상세내역 삭제</p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211005491-92e17233-fc89-495a-969c-83318f90c403.png">
  </li>
  <li>
    <p>가계부 상세내역 복제하기 </p>
    <img width="800" alt="" src="https://user-images.githubusercontent.com/102202607/211076584-6891e9c7-ebf5-42d0-8e51-ed86783b077b.png">
  </li>
</ul>
</div>
</details>
<details>
<summary>5. API docs</summary>

## API doc
[https://repeated-cosmonaut-832.notion.site/payhere-AccountBook-78d0f08c042c42a1a7fb57353c9b0f73]
</details>

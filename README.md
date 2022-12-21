# django-vote-16th

## 파트장/데모데이 투표 사이트

### ERD 구성
![투표ERD](https://user-images.githubusercontent.com/56791347/208661842-6af9123e-e209-40d7-ba26-74b882cde3d7.png)

### 프로젝트 세팅

0. 폴더 구조
   ```
   django-vote-16th
   ├─account
   │  └─migrations
   ├─django_vote_16th
   │  └─settings
   └─users
      └─migrations
   ```
1. 가상환경에 패키지 설치
   ```shell
    pip install -r requirements.txt
   ```
2. env 파일 설정
   ```shell
   DJANGO_ALLOWED_HOSTS={호스트 주소}
   DJANGO_SECRET_KEY={시크릿키}

   DATABASE_NAME={DB 이름}
   DATABASE_USER={DB 유저}
   DATABASE_PASSWORD={비밀번호}
   DATABASE_HOST={호스트 주소}
   DATABASE_PORT={포트 번호}
   ```
3. DB 마이그레이션
   ```shell
   python manage.py migrate
   ```
4. 초기 데이터 삽입
   ```shell
   python manage.py loaddata init_data.yaml
   ```
   
### 회원가입/로그인

### 투표하기  
   * 후보는 득표 순으로 내림차순 정렬되어 보여진다.
   * 로그인하지 않은 사용자는 투표 페이지에 접근할 수는 있되, 투표는 불가능
   * 파트장 투표 : 본인의 파트에 해당하는 파트장 투표만 가능
   * 데모데이 투표 : 본인이 속한 팀을 제외하고 투표 가능

### 로그아웃

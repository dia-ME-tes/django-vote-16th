# django-vote-16th
## 파트장/데모데이 투표 사이트

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


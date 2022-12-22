# django-vote-16th

## 파트장/데모데이 투표 사이트

### ERD 구성
![투표ERD](https://user-images.githubusercontent.com/56791347/208661842-6af9123e-e209-40d7-ba26-74b882cde3d7.png)

### API 명세서  
 * account
   * https://documenter.getpostman.com/view/24886420/2s8Z6u4a1z
 * user
   * https://documenter.getpostman.com/view/24886420/2s8Z6u4a23
   
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

### 도커로 실행
```shell
docker-compose up
```
## 기능
### 로그인
   * 사용자 로그인 여부는 JWT를 통해 인증
   * 아이디 혹은 비밀번호가 틀렸을 시에는 에러를 반환

### 회원가입
- 회원가입에 필요한 필드는 **이메일(아이디)**, **비밀번호**, **파트, 이름, 팀**
- **이메일**은 중복될 수 없습니다. (이메일 중복 시 400 반환)
- **파트**는 (프론트엔드, 백엔드) 중 하나를 선택 가능
- **팀**은 (Teample, finble, Pre:folio, diaMEtes, recipeasy) 중 하나 선택 가능

### 투표하기  
   * 후보는 득표 순으로 내림차순 정렬되어 보여진다.
   * 로그인하지 않은 사용자는 투표 페이지에 접근할 수는 있되, 투표는 불가능
   * 파트장 투표 : 본인의 파트에 해당하는 파트장 투표만 가능
   * 데모데이 투표 : 본인이 속한 팀을 제외하고 투표 가능

### 로그아웃
- 로그아웃은 쿠키에 있는 토큰을 삭제하는 방식으로 구현

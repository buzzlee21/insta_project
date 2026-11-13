# 1단계 첫 테스트: DB 없이 돌아가는 가장 간단한 검사들
# 실행: uv run pytest -v

from fastapi.testclient import TestClient
from deps import password_hash
from main import app

client = TestClient(app)


# 테스트 함수 이름은 반드시 test_ 로 시작해야 pytest가 찾아요.
# assert 뒤의 조건이 True면 통과, False면 실패예요.

def test_password_is_hashed():
  # 암호화된 비밀번호는 원래 비밀번호와 달라야 한다
  hashed = password_hash.hash('mypassword')
  assert hashed != 'mypassword'


def test_password_verify_success():
  # 맞는 비밀번호는 검증을 통과해야 한다
  hashed = password_hash.hash('mypassword')
  assert password_hash.verify('mypassword', hashed) is True


def test_password_verify_fail():
  # 틀린 비밀번호는 검증에 실패해야 한다
  hashed = password_hash.hash('mypassword')
  assert password_hash.verify('wrongpassword', hashed) is False


def test_home_returns_200():
  # 홈 주소(/)에 접속하면 정상 응답(200)과 내용이 와야 한다
  response = client.get('/')
  assert response.status_code == 200
  assert response.json() == {'hi': 'hello'}

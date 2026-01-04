# test_app.py
import pytest
from app import app

# 픽스처: 테스트용 가짜 손님(client)을 준비합니다.
@pytest.fixture
def client():
    # Flask에서 제공하는 테스트용 도구를 가져옵니다.
    with app.test_client() as client:
        yield client  # 테스트 함수에 가짜 손님을 빌려줍니다.

# 1. 홈페이지가 잘 나오는지 테스트
def test_home_page(client):
    # 가짜 손님이 홈페이지('/')에 접속합니다.
    response = client.get('/')
    
    # 결과가 200(성공)인지 확인합니다.
    assert response.status_code == 200
    # 화면에 "Hello, World!"라는 글자가 있는지 확인합니다.
    assert response.data.decode('utf-8') == "Hello, World!"

# 2. 정보 주소(/info)가 올바른 데이터를 주는지 테스트
def test_info_api(client):
    response = client.get('/info')
    
    # 결과가 성공인지 확인
    assert response.status_code == 200
    
    # 받은 데이터가 우리가 정한 내용과 맞는지 확인
    data = response.get_json()
    assert data['name'] == "Gemini"
    assert data['status'] == "Happy"


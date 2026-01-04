# test_main.py
import pytest, json
from main import sumx, addx
# 1. json 파일을 읽어서 데이터 배달
def json_data():
    # 'data.json' 파일을 읽기 모드(r)로 엽니다.
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)  # json 파일을 파이썬 데이터(딕셔너리)로 변환
    print("\n[알림] 외부 JSON 파일에서 데이터를 성공적으로 가져왔습니다!")
    return data["test_cases"]   # json 데이터 이름 test_cases를 사용하여 전달
# @pytest.mark.parametrize를 사용하여 파일 데이터를 하나씩 주입합니다.
@pytest.mark.parametrize("case", json_data())  # json_data() 뭉치에서 문제 한 장(case)를 꺼내서 전달
def test_addx_independent(case):
    quest = case["input"]
    answ = tuple(case["expected"])   # json 파일에서 list로 저장된 결과값을 tuple로 형변환
    result = addx(*quest)            # tuple 가변인자 이용한 함수 호출
    assert result == answ            # 튜플 끼리 비교
    #assert sumx(num) == expected
    print(f"\n지금 테스트 중인 숫자: {quest}")
    print(f"테스트 {quest}의 코드실행 결과는 {result}이고, ground-truth는 {answ}임")

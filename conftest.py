# conftest.py
import pytest

# 1. 가짜 이메일 전송 함수 (실제로는 터미널에 출력)
def send_notification(message):
    print(f"\n[이메일 발송 중...]")
    print(f"보낼 내용: {message}")
    print("[발송 완료!]")

# 2. 테스트가 끝날 때마다 자동으로 실행되는 '훅(Hook)' 함수
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 테스트 결과를 가져오기 위한 준비 과정입니다.
    outcome = yield
    report = outcome.get_result()

    # 테스트가 실제로 '실행(call)'된 단계의 결과만 확인합니다.
    if report.when == 'call':
        if report.passed:
            # 테스트가 성공했을 때
            send_notification(f"✅ 축하합니다! '{item.name}' 테스트가 성공했습니다.")
        elif report.failed:
            # 테스트가 실패했을 때
            send_notification(f"❌ 경고! '{item.name}' 테스트가 실패했습니다. 코드를 확인하세요!")
# main.py
def sumx(num):   # 함수 생성
    if num == 1:
        return 1   # 기존 1을 0으로 변경하여 고의로 오류 발생시킴
    else:
        return sumx(num-1) + num  # 재귀함수 활용
# 복수 입력/출력 함수 추가
def addx (num1, num2):   # 함수생성
    c= num1+num2
    return num1, num2, c    # 복수 3 개 값 반환 ( 다중반환문 , tuple 로 반환 )

def main():
    b = sumx(5)      # 재귀 함수 이용 (결과: 15)
    print(f"sumx(5)의 결과: {b}")
    c = addx(5,10)     # 투플 반환
    print(f"addx(5,10)의 결과: {c}")   # 튜플 인쇄
    #print(f"{c[0], c[1], c[2]}")

if __name__ == "__main__":
    main()
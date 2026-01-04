def   addx(x,*y):      # 위치인자 x, 가변인자 *y
    print(y)    # tuple 인쇄
    total = x
    for num in y:
        total = total + num
    return total

def  main():
    result1 = addx(10,2,3)            #   단순 2,3 전달
    #result1 = addx(10,*(2,3))      #   튜플 (2,3) 전달 
    #result1 = addx(10,*[2,3])      #   리스트 [2,3] 전달
    print( result1 )  # 15  
    result2 = addx(10,2,3,4)            #   단순 2,3,4 전달
    #result2 = addx(10,*(2,3,4))      #   튜플 (2,3,4) 전달
    #result2 = addx(10,*[2,3,4])      #   리스트 [2,3,4] 전달
    print( result2 )  # 19
    y=[2,3,4]
    result3 = addx(10,*y)      #   리스트 [2,3,4] 전달
    print( result3 )  # 19

if __name__ == "__main__":           # 커맨드라인/인터페이스를 통해 직접 실행했을 때만 아래 코드를 실행
    main()
    input()

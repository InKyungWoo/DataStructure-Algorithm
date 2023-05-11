
while True:
    num = int(input('단 입력(종료:0) '))
    if num == 0:
        print('구구단 프로그램 종료')
        break
    else:
        i = 1
        while i <= 9:
            print(f'{num} x {i} = {num * i}')
            i += 1

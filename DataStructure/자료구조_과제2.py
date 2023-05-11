import random

answer = random.randint(10, 99)


def compare_answer(answer, guess):

    if answer == guess:
        return 0
    elif answer < guess:
        return 1
    elif answer > guess:
        return -1


cnt = 1

for i in range(10):
    guess = int(input("두자리 정수 입력: "))

    if compare_answer(answer, guess) == 0:
        print(f"정답입니다. {cnt}번 만에 맞추셨습니다.")
        print("게임 끝!!!")
        break
    elif compare_answer(answer, guess) == 1:
        print("아닙니다. 더 작은 숫자입니다!")
        cnt += 1
    elif compare_answer(answer, guess) == -1:
        print("아닙니다. 더 큰 숫자입니다!")
        cnt += 1

    if cnt == 11: #횟수 10회 소진시 
        print("정답을 맞추지 못했습니다.")
        print("게임 끝!!!")
        break

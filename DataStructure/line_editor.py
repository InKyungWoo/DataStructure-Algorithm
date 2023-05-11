from ArrayList import *

listA = ArrayList()

while True:
    command = input('i-입력 d-삭제 r-변경 p-출력 l-파일읽기 s-파일저장 q-종료 : ')

    if command == 'q':
        break
    
    elif command == 'i':
        num = int(input('입력할 행번호 : '))
        str1 = input('입력 내용 : ')
        listA.insert(num, str1)

    elif command == 'd':
        num = int(input('삭제할 행번호 : '))
        listA.delete(num)

    elif command == 'r':
        num = int(input('수정할 행번호 : '))
        str1 = input('수정 내용 : ')
        listA.replace(num, str1)

    elif command == 'p':
        print('Line Editor')
        for i in range(listA.size()):
            print('[{:2d}] '.format(i), end = "")
            print(listA.getEntry(i))

    elif command == 'l':
        infile = open('linetest.txt', 'r')
        lines = infile.readlines()
        for line in lines:
            listA.insert(listA.size(), line.rstrip('\n'))
        infile.close()

    elif command == 's':
        outfile = open('linetest.txt', 'w')
        for i in range(listA.size()):
            outfile.write(listA.getEntry(i)+'\n')
        outfile.close()

print('종료되었습니다.')

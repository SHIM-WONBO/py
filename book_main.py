import os
from book_management import BM

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'input.txt')

f = open(my_file,'r')
book_list = []
while True:
    tmpbl = f.readline().split()
    book_list.append(tmpbl)
    if not tmpbl: break
f.close()

while True:
    bm = BM(book_list)
    print('\n====== 메뉴 번호를 입력하세요 ======')
    number = input("1. 도서 추가 \n2. 도서 검색 \n3. 도서 정보 수정 \n4. 도서 삭제 \n5. 현재 총 도서 목록 출력 \n6. 저장 \n7. 프로그램 나가기 \n입력 : ")
    if number == '1':
        bm.menu1(book_list)
    elif number == '2':
        bm.menu2(book_list)
    elif number == '3':
        bm.menu3(book_list)
    elif number == '4':
        bm.menu4(book_list)
    elif number == '5':
        bm.menu5(book_list)
    elif number == '6':
        bm.menu6(book_list)
    elif number == '7':
        with open('input.txt', 'w') as file:    
            file.writelines(book_list)
        print('프로그램을 종료합니다.')
        break
    else:
        print('없는 메뉴 번호입니다.')


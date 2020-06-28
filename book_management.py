import os

class BM:
    def __init__(self, book_list):
        self.book_list = book_list
    
    def menu1(self,book_list):
        newbook_list = list(input("도서명, 저자, 출판연도, 출판사명, 장르 입력(빈칸으로 구분)\n").split())
        book_list.append(newbook_list)
        # 1 도서 추가

    def menu2(self,book_list):
        searchbook_list = str(input("찾고자하는 도서명, 저자, 출판연도, 출판사명, 장르 중 하나를 입력하세요\n"))
        for i in range(0,len(book_list),1):
            if searchbook_list in book_list[i]:
                print(book_list[i])
        print("검색완료")
        # 2 도서 개별검색

    def menu3(self,book_list):
        i = 0
        while i < (len(book_list)-1):
            a,b,c,d,e = book_list[i]
            print(i+1,end='.')
            print(a,b,c,d,e)
            i += 1
        num = int(input('수정할 도서의 목록번호를 입력하세요 : '))
        mdy_list = list(input('도서명, 저자, 출판연도, 출판사명, 장르 입력(빈칸으로 구분)\n').split())
        book_list[num-1] = mdy_list.copy()
        # 3 도서 수정

    def menu4(self,book_list):
        i = 0
        while i < (len(book_list)-1):
            a,b,c,d,e = book_list[i]
            print(i+1,end='.')
            print(a,b,c,d,e)
            i += 1
        num = int(input('삭제할 도서의 목록번호를 입력하세요 : '))
        book_list.pop(num-1)
        # 4 도서 수정

    def menu5(self,book_list):
        i = 0
        while i < (len(book_list)-1):
            a,b,c,d,e = book_list[i]
            print(i+1,end='.')
            print(a,b,c,d,e)
            i += 1
        # 5 도서 목록 보기

    def menu6(self,book_list):
        with open('input.txt', 'w') as file:    
            file.writelines(book_list)
        # 6 도서목록 저장
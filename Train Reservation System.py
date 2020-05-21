import copy

f = open("C:/Users/user/Desktop/경기대학교/eon/TrainList.txt", 'r')          #TrainList.txt 경로 "" 사이에 입력
TL=[]
indlist = []
while True:
    tl = f.readline().split()
    TL.append(tl)
    if not tl: break
f.close()                       # TL은 ':,-,>' 포함한 리스트.
del TL[0]
del TL[len(TL)-1]

modyTL = copy.deepcopy(TL)
reservation_list = []
ind = None

for i in range(20):             # modyTL 은 ':,-,>' 제거하고 첫항 정수형으로 바꿔준 리스트.
    del modyTL[i][2]
    modyTL[i][0] = modyTL[i][0].replace(":","")
    modyTL[i][0] = int(modyTL[i][0])

def close_time(mytime, time_list):  #근접한 값 찾는 함수
    a = mytime
    b = time_list.copy()
    real_time_list = [605,635,715,842]
    abs_list = []
    for i in range(len(b)):
        abs_list.append(abs(a-b[i]))
    ind = abs_list.index(min(abs_list))
    return real_time_list[ind]

class TRAIN:
    def menu1(self): #빠른시간 기차 검색 및 예매
        des_train = list(input("\n====== 원하는 시간(YY:MM), 출발역, 도착역, 열차종류 입력 ('빈칸'으로 구분) ======\n※ 뒤로가기 : 아무키나 입력 ※\n※ 경고 : 입력이 잘못되면 뒤로갑니다 ※\n입력 : ").split())
        tmp_TL = copy.deepcopy(modyTL)          #tmp_TL 은 menu1 안에서만 쓸 modyTL이라고 보면 됨.

        for i in range(20):
            tmp_TL[i].pop()

        time_list = [365,395,435,522]
        tmp_mytime = int(des_train[0].replace(":",""))
        a, b = divmod(tmp_mytime, 100)
        mytime = a*60+b
        des_train[0] = close_time(mytime, time_list)
        closed_T = []

        for i in range(20):
            if tmp_TL[i] == des_train:
                closed_T = tmp_TL[i].copy()
                closed_T.append(TL[i][5])
                ind = i
                print('\n===== 가장 가까운 시간의 기차 정보 =====\n|  시간  | 출발 | 도착 | 열차종류 | 잔여석 수 |')
        a, b = divmod(closed_T[0], 100)
        a = str(a)
        b = str(b)
        if int(b)//10 == 0:
            closed_T[0] = ''.join(['0', a, ':','0', b])
        else:
            closed_T[0] = ''.join(['0', a, ':', b])
        print('|', end=' ')
        for a in closed_T:
            print(a,end = ' | ')


        while True:
            reservation = input('\n해당 기차표를 예매하시겠습니까? [Y/N]\n입력 : ')
            if reservation == 'Y':
                if TL[ind][5] != '매진':
                    reservation_list.append(TL[ind])
                    TL[ind][5] = int(TL[ind][5])-1
                    print('예매가 완료되었습니다.')
                    indlist.append(ind)
                    if TL[ind][5] == 0:
                        TL[ind][5] = '매진'
                    break
                else:
                    print('\n해당 기차표는 매진되었습니다. 초기메뉴로 돌아갑니다.')
                    break
            elif reservation == 'N':
                print('\n처음 화면으로 돌아갑니다.')
                break
            else:
                print('Y 또는 N을 입력해주세요.')
        return ind

    def menu2(self):  #전체 기차리스트 출력
        print('\n========== 기차 시간표 ==========','시간_출발_도착_열차종류_잔여좌석수','-------------------------------',sep='\n')
        i = 0
        while i < len(TL):
            a,b,c,d,e,f = TL[i]
            print(a,b,c,d,e,f)
            i += 1

    def menu3(self):
        if ind == None:
            print('\n예매된 기차가 없습니다.')
        elif reservation_list == []:
            print('\n예매된 기차가 없습니다.')
        else:
            print('\n       [ 예매 완료 ]\n','======== 기차 정보 ========',sep='\n')
            i = 0
            while i < len(reservation_list):  # 반복할 때 리스트의 크기 활용(세로 크기)
                a,b,c,d,e,f = reservation_list[i]  # 요소 두 개를 한꺼번에 가져오기
                print(a,b,c,d,e)
                i += 1
            cancle = input('\n예매를 취소하시겠습니까? [Y/N]\n※ 뒤로가기 : 아무키나 입력 ※\n입력 : ')
            if cancle == 'Y':
                if TL[indlist[len(indlist)-1]][5] == '매진':
                    TL[indlist[len(indlist)-1]][5] = 1
                    reservation_list.pop()
                else:
                    TL[indlist[len(indlist)-1]][5] = TL[indlist[len(indlist)-1]][5] + 1
                    reservation_list.pop()
                indlist.pop()
                print('\n취소가 완료되었습니다.')
            else:
                print('\n처음 화면으로 돌아갑니다.')

while True:
    print('\n====== 메뉴 번호를 입력하세요 ======')
    number = input("1. 빠른시간 기차 검색 및 예매 \n2. 전체 기차 리스트 출력 \n3. 나의 예매 현황 출력 및 예매 취소 \n4. 프로그램 종료 \n입력 : ")
    train = TRAIN()
    try:
        if number == '1':
            ind = train.menu1()
        elif number == '2':
            train.menu2()
        elif number == '3':
            train.menu3()
        elif number == '4':
            print('프로그램을 종료합니다.')
            break
        elif number == '5':
            number = 5
            print('최상위 메뉴입니다.')
        else:
            print('없는 메뉴 번호입니다.')
    except:
        print('처음 화면으로 돌아갑니다.')
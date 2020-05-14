n, m = list(map(int, input("작업 수 / 작업 번호 : ").split()))
joblist = list(map(int, input("작업 우선순위 : ").split()))
tstlist = joblist.copy()
minute = 0
largest = max(joblist)                # 입력된 리스트의 최대값 변수
tst_largest = max(tstlist)            # 큐 작업을 수행할 리스트의 최대값 변수

while joblist[m] < tst_largest:     # 입력받은 값이 큐의 최대값보다 작을때
    if tstlist[0] == tst_largest:   # 큐의 첫번째 값이 최대값이면 빼고 1분 추가
        tstlist.pop(0)
        minute += 1
    elif tstlist[0] < tst_largest:  # 큐의 첫번째 값이 최대값보다 작으면 그 값을 맨 뒤로 보냄
        tstlist.append(tstlist[0])
        tstlist.pop(0)

    tst_largest = max(tstlist)

while True:
    if joblist[len(joblist)-1] == joblist[m]:
        minute += 1
        joblist.pop()
    elif joblist[len(joblist)-1] < joblist[m]:
        joblist.pop()
    elif joblist[len(joblist)-1] > joblist[m]:
        break

for i in range(0,m+1):
    if joblist[i] == joblist[m]:
        minute += 1

print(minute,'분')







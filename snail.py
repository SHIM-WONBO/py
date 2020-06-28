num = int(input('수입력 : '))
snail_array = [[0] * num for i in range(num)] 
i = 0; j = -1; 
n = 0; s = 1; k = num; 

def snail():
    global i,j,n,s,k
    for p in range(1,k+1): 
        n = n + 1 
        j = j + s 
        snail_array[i][j] = n 
    
    k = k - 1 
    for p in range(1,k+1): 
        n = n + 1 
        i = i + s 
        snail_array[i][j] = n 
        
    s = s * -1 
    if k > 0 : 
        snail()
    else:
        pass
snail()

for i in range(len(snail_array)) : 
    for j in range(len(snail_array[0])): 
        print('%3d ' % snail_array[i][j],end='') 
    print()
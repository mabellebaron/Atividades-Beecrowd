A = int(input())
B = int(input())
cont = 0
for x in range(A , B + 1):
    if x % 4 == 0 and x % 100 != 0 or x % 400 ==0:
        print(x)
        cont += 1
print (f'bissextos: {cont}')
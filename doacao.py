n = c = s = 0
n = float(input())
while n != (-1.0):
    s += n
    c += 1
    n = float(input())
print('VC$ {:.2f}'.format(s))
print('R$ {:.2f}'.format(s * float(2.50)))
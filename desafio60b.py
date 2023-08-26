#fatorial usando for
n = int(input('digite um número para calcular seu fatorial: '))
c = n
f =1
for n in range(c, 0, -1):
    f = f *n
    print(n , end=' ' 'x' if n > 1 else '=')
print('{}'.format(f))

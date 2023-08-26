def area(lar, com):
    total = lar * com
    print(f'a area de u terreno {lar}x{com} é de {total}m2.')

l = float(input('qual a largura do terreno: '))
c = float(input('qual o comprimento do terreno: '))
area(l, c)
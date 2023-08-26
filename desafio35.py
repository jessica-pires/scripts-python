#analisando e constuindo  um triangulo
#leia tres retas e diga ao usuario se elas
# podem formar ou nao um triangulo
a = int(input('qual o primeiro segmento:'))
b = int(input('qual o segundo segmento: '))
c = int(input('qual o terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('é possivel formar um \033[0;30;45mtriangulo\033[m')
else:
    print('\033[04;30;31mnao\033[m é possivel fazer um \033[4;30;31mtriangulo!')
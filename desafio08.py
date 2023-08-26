#----------DEFAFIO----------
#Escreva um programa que leia um valor em metros e o
# exiba convertido em centimetros e milimetros

m = float(input('quantos metros:'))

print('{} metros é {} centimetros e {} milimetros'.format(m, m * 100, m * 1000))

#---------Outro Exemplo---------------

a = float(input('qual sua altura?: '))
print('Você tem {} cm e {} mm'.format(int(a*100), int(a*1000)))
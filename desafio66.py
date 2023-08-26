#progrma q leia varios programas so parar no 999
# mostre na tela a soma e quando numeros foram digitados

n = s = v = 0
while True:
    n = int(input('digite um numero [999] para parar:'))
    if n == 999:
        break
    s = s + n
    v = v + 1
print(f'a soma dos {v} valores foi {s} ')

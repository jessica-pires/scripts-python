def escreva(txt):
    tam = len(txt) + 4 #tamanho do sublinhado comforme a msg
    print('-' *tam)
    print(txt.center(tam))
    print('_'* tam)


escreva('OLA, MUNDO')
escreva('CURSO EM VÍDEO')
escreva('EU CONSIGO')
escreva('oi')


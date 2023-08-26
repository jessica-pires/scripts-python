#mostar o tipo primitivo e informaçoes

u = input('digite algo: ')
print(u,'é do tipo primitivo' , type(u))
print(u,'possui letra maiuscula?' , u.isupper())
print(u,'possui letra minuscula?', u.islower())
print(u, 'é alfanumerico?', u.isalnum())
print(u,'é alfabetico?' , u.isalpha())
print(u,'é um numero?', u.isnumeric())

print(u,'só tem espaços' , u.isspace())
print(u, 'esta capitalizada' , u.istitle())
#o termo capitalizada é: nem maiuscula e nem minuscula
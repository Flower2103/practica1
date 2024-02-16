import json

with open('p1/nombre.json', 'r') as myfile:
    
    data = myfile.read()

    for caracter in data:
        if caracter == '\n':
            print('[ENTER]')
        elif caracter == ' ':
            print('[ESPACIO]')
        else:
            print(caracter)

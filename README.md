# Lenguajes y Autómatas I

------------


## Práctica 1

Programa que lee un archivo JSON. 
Se imprimen los caracteres por separado.

- Lenguaje de programación: Python 3.11.5
- Editor utilizado: Visual Studio Code 1.86.2



------------


### Documentación

`<link>` : <https://www.json.org/json-en.html>


------------


### Code Blocks 

#### Python



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
Importamos el *modulo json* para poder trabajar con los datos del archivo .json.
Se implementa la estructura *with*  en conjunto de *open()* que contiene la ruta del archivo en cuestión para poder abrirlo y asignarse a la variable *myfile*.
Se crea una una nueva variable *data* y se asigna la lectura del archivo en en formato *str*.
Por ultimo, con el ciclo for se itera sobre cada caracter de la variable data y se condiciona para imprimir en pantalla los saltos de linea y espacios que se puediesen encontrar.



#### JSON　

```javascript
{
    "nombre":"Flor:"
}


```
Estructura basica de un archivo JSON delimitado con "{ }" y clave-valor.

------------

###### Contacto
al22760045@ite.edu.mx

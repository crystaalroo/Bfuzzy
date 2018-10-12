# Biblioteca BFuzzy

Biblioteca realizada para la clase de Inteligencia Artificial I. 
Permite obtener los resultados para un U dado de las funciones de pertenencia:

*Función de Trapecio abierto Derecho

*Función de Trapecio abierto Izquierdo

*Función Triangular

*Función Trapezoidal

*Función curva S

*Función curva Z

*Función triangular suave

*Función trapezoidal suave
  
Operadores de logica difusa:

*Minimo

*Maximo

*AND

*OR

*NOT

*Implica Zadeh

*Implica Mamdani

*Implica Godel
  
# CÓMO FUNCIONA?
1. El proyecto despliega una interfaz grafica, en donde es posible elegir alguna de las funciones de pertenecia a la vez.

2. Una vez que se seleccióna, el programa selecciona 4 variables random.

3. Se le asignan esas variables a A,B,C,D, que son los paramentros necesarios para las funciones de pertenencia.

4. Se dibuja una grafica que tiene como dominio los numeros de 0-100 para la U. Y como sabemos, las funciones de pertencia tienen como rango [0,1]

5. Se dibujan en color rojo, los valores de A,B,C,D. Que permiten visualizar porque ocurrren los cambios en la función. Si no necesita alguno de los parametros, igual se pinta, pero para la función es irrelevante.

6. Se grafican los resultados de la función elegida.

7. Si presionas en "limpiar", se reinicia el proceso.

# IMPORTANTE!!

En la terminal de processing, se pueden ver los valores exactos para cada punto del [0,100].

La función que se modela, presenta una función discreta. PERO LAS FUNCIONES DE PERTENENCIA SON FUNCIONES CONTINUAS.
Solo que por motivos de modelación, se presentan valores enteros para graficar.

Cuidar que no se cumpla la división sobre 0.

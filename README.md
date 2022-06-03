# PRIMOS-DE-3-4-5-CIFRAS


En el presente Repositorio se nos pidio crear numeros primos de 3, 4 y 5 cifras; donde utilizamos tres algoritmos que nos ayudaran para crear estos números un EXPMOD, COMPUESTO, MILLER_RABIN.

EXPMOD:La exponenciación modular para hallar el residuo de algun número de una gran cantidad de cifras (caso de 16bits a más), donde "y" toma el valor de exponente (donde su valor es p-1), "a" como base y "p" el número que comprobaremos durante el proceso de compuesto o no.

COMPUESTO:Para comprobar si el número es compuesto (valor false) mediante el residuo obtenido en caso que sea 1 o el numero que se comprueba menos 1 entonces descimos que es pseudo primo, luego comprueba si ese número lo divide en n-1 se considera pseudo. (ojo a tomara el valor de la base para residuo que tomara valores desde 2 ya que utilizar 0 o 1 nos daría 1 o el mismo número y así el  EXPMOD no funcionaria)

MILLER:Utilizando el compuesto halla la fidelidad si el número es primo o no (teniendo en cuenta a los pseudoprimos) 

FINALIZANDO:
"for n in range(100,1000)" --> Es un bucle que recorre los números de 3 cifras

"for n in range(1000,10000)" --> Es un bucle que recorre los números de 4 cifras

"for n in range(10000,100000)" --> Es un bucle que recorre los números de 5 cifras

Luego con "if (Miller(b, s))" se comprueba que si es primo con un seguridad dependiendo de S (En nuestro caso utilizamos 5 porque el tiempo empleado es más eficiente que utilizando uno mayor, además que si utilizamos uno menor el test de miller no seria tan efectivo), teniendo encuenta que debemos mostrar todos los números dentro del rango. Posteriormente si da true el test ese valor lo imprime.

Este proceso se repite para 4 y 5 bits.

# Cifrador de Bits

## Objetivo

El objetivo de este ejercicio es aplicar una secuencia de operaciones a nivel de bits sobre un carácter secreto. Si implementas correctamente las funciones, podrás "descifrar" el carácter secreto.

Este ejercicio cubre:

* Funciones que retornan valores (`int`) y programación modular básica
* Operaciones bit a bit: desplazamiento a la izquierda (`<<`), desplazamiento a la derecha (`>>`), NOT (`~`), XOR (`^`)
* Variables locales para almacenar bits (MSB/LSB)
* Macros
* Expresiones booleanas simples para validación

## Instrucciones

1. Se te da un carácter secreto `?` (código ASCII 63).

2. Debes aplicar los siguientes pasos **dentro de las funciones del programa**:

   1. Desplazamiento circular a la izquierda
   2. Inversión de bits
   3. Desplazamiento circular a la derecha
   4. XOR con la máscara `129` (decimal) para obtener el carácter final

3. Implementa las funciones:

   * `ShiftLeftCircular(int value)`
   * `InvertBits(int value)`
   * `ShiftRightCircular(int value)`
   * `ApplyMask(int value)`
   * `EncryptValue(int value)`

4. Modifica la función `main()` para que solicite al usuario un carácter de entrada y use ese valor como carácter secreto a procesar.

5. Al ejecutar correctamente tu programa, el carácter secreto `?` se transformará en el carácter final esperado.

## Ejemplo

Entrada esperada del programa:

```
Ingrese el caracter a encriptar: ?
```

Salida esperada del programa:

```
? -> A
```

Carácter secreto inicial: `?`

Carácter esperado al final después de ejecutar el programa: `A`

Si tus funciones son correctas, el programa transformará `?` en `A`.

## Notas

* Trabaja solo con tipos `int`.
* No uses arreglos, cadenas de texto ni punteros.
* Utiliza únicamente las operaciones descritas.
* Los pasos son una guía; las manipulaciones a nivel de bits transformarán `?` en `A`.

## Metas de Aprendizaje

* Entender y manipular bits individuales en un número.
* Practicar el uso de funciones y retorno de valores.
* Aprender el efecto de las operaciones bit a bit sobre caracteres.
* Seguir una secuencia clara de operaciones para obtener un resultado específico.

Al completar el ejercicio, deberías ser capaz de explicar cómo cada paso modifica los bits y por qué el carácter final es `A`.


---

## Archivos esperados

* `main.c`: Todo el código del programa debe estar contenido en este archivo.

---

## Compilación y ejecución

Usa las macros de Visual Studio Code.

```
CTRL + SHIFT + B
```

---

**Autor:** Jesús Salvador López Ortega
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)

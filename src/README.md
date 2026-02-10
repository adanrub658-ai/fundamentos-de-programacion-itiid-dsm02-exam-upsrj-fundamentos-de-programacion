# Sistema de Acceso

## Objetivo

El objetivo de este ejercicio es reforzar el uso de **estructuras de control repetitivas** y el **manejo básico de cadenas de caracteres en lenguaje C**, mediante la simulación de un sistema simple de inicio de sesión.

Este ejercicio cubre:

* Uso de ciclos `for`, `while` y `do/while`
* Uso de las palabras clave `break` y `continue`
* Manejo básico de cadenas de caracteres (`char`)
* Validación de entrada del usuario
* Control de flujo en programas secuenciales
* Comparación de caracteres usando rangos ASCII

---

## Instrucciones

1. El programa debe solicitar al usuario un **nombre de usuario**.

2. El nombre de usuario debe cumplir las siguientes condiciones:
   * Tener una longitud mínima de **5 caracteres**
   * No estar vacío

3. La validación del nombre de usuario debe realizarse usando un ciclo `do/while`.

4. Una vez ingresado un nombre de usuario válido, el programa debe:
   * Recorrer el nombre carácter por carácter usando un ciclo `for`
   * Contar cuántos caracteres **no son espacios**
   * Usar la palabra clave `continue` para ignorar los espacios

5. Posteriormente, el sistema debe solicitar una **contraseña**, considerando:
   * Máximo **3 intentos**
   * El control de intentos debe realizarse con un ciclo `while`

6. Antes de validar la contraseña, el programa debe:
   * Recorrer la contraseña con un ciclo `for`
   * Verificar que contenga **al menos un número**
   * Si no contiene números, el intento se considera fallido

7. Si la contraseña ingresada coincide con la contraseña correcta:
   * Mostrar el mensaje `"Access granted."`
   * Salir inmediatamente del ciclo usando `break`

8. Si se alcanzan los 3 intentos fallidos:
   * Mostrar el mensaje `"Account locked."`

---

## Ejemplo

Entrada esperada del programa:

```

Enter username (minimum 5 characters): student01
Enter password: admin123

```

Salida esperada del programa:

```

Username has 9 non-space characters.
Access granted.

```

Ejemplo de intento fallido:

```

Enter password: test
Password must contain at least one number.
Enter password: 123
Incorrect password.
Enter password: pass1
Incorrect password.
Account locked.

```

---

## Notas

* Todo el programa debe implementarse **dentro de la función `main`**.
* No se permite el uso de funciones definidas por el usuario.
* No se permite el uso de punteros explícitos.
* El uso de arreglos está limitado únicamente al almacenamiento de las cadenas de entrada.
* No se deben utilizar estructuras, memoria dinámica ni librerías avanzadas.
* El objetivo es reforzar **control de flujo**, no seguridad real.

---

## Metas de Aprendizaje

* Comprender cuándo y por qué usar `for`, `while` y `do/while`.
* Aplicar correctamente `break` para salir de un ciclo.
* Aplicar correctamente `continue` para saltar iteraciones.
* Manipular cadenas de caracteres básicas en C.
* Analizar y validar datos ingresados por el usuario.
* Desarrollar programas con flujo lógico claro y legible.

Al finalizar el ejercicio, el estudiante debe ser capaz de **explicar el comportamiento de cada ciclo** y **justificar el uso de `break` y `continue`** dentro del programa.

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
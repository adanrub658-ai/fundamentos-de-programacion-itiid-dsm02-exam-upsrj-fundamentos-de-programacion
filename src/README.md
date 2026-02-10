# Área y Volumen de un Cuadrado

## Objetivos

* Calcular el área de un cuadrado dado el valor de la longitud de su lado.
* Calcular el volumen de un cubo dado el valor de la longitud de su lado.

Este ejercicio ayuda a practicar:

* Entrada y salida estándar en C (`scanf`, `printf`).
* Variables y operaciones aritméticas.
* Organización básica de un programa.

---

## Instrucciones

1. Crea un archivo llamado `main.c` en la carpeta del ejercicio.

2. Escribe un programa en C que:

* Pida al usuario la longitud del lado en formato `int`.
* Calcule el área del cuadrado en una función `get_area` y reciba como parámetro de entrada un `int`.
* Calcule el volumen del cubo en una función `get_volume` y reciba como parámetro de entrada un `int`.

* Imprima ambos resultados en pantalla.

---

## Archivos esperados

* `main.c`: Todo el código del programa debe estar contenido en este archivo.

---

## Ejemplo de uso

### Entrada

```
Introduzca la longitud del lado: 5
```

### Salida

```
Area del cuadrado: 25
Volumen del cubo: 125
```

---

## Compilación y ejecución

Usa las macros de Visual Studio Code.

```
CTRL + SHIFT + B
```

---

## Diagrama simple

Cuadrado (2D)              Cubo (3D)

```
+---------+              +---------+
|         |             /         /|
|         |            +---------+ |
|         |            |         | +
+---------+            |         |/
                       +---------+
```

---

## Preguntas de reflexión

1. ¿Qué sucede si el usuario introduce un número decimal en lugar de un número entero?
2. ¿Cómo debería comportarse el programa si la longitud del lado es negativa?
3. ¿Por qué `float` o `double` podrían ser más útiles que `int` para este programa?

---

**Autor:** Jesús Salvador López Ortega
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)

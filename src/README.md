# Reloj Digital por Consola – Lista de Requerimientos

## Objetivo

El objetivo de este ejercicio es reforzar el uso de:

* Variables y tipos de datos básicos  
* Manejo de cadenas (`char[]`)  
* Lectura de datos con `scanf`  
* Conversión de cadenas a valores numéricos (`sscanf`)  
* Estructuras de control (`if`, `while`)  
* Modularización de la lógica en funciones  
* Razonamiento secuencial del tiempo  

El programa debe implementar la lógica completa de un reloj digital que **avance manualmente el tiempo**, sin utilizar la hora real del sistema, y respetando las funciones obligatorias.

---

## Nota sobre `main.c`

En el archivo `main.c` se incluye:

```c
#include "./clock.h"

#ifndef UNIT_TEST
int main() {
    printf("Hello World!\n");
    return 0;
}
#endif /* UNIT_TEST */
```

- **`#include "./clock.h"`**: este archivo contiene las **declaraciones** de las funciones obligatorias. Garantiza que las firmas sean consistentes y que el compilador pueda verificar que las funciones existen.  
- **`#ifndef UNIT_TEST`**: este bloque evita que el `main()` se compile cuando se ejecutan las pruebas automáticas. El tester define la macro `UNIT_TEST` al compilar, lo que desactiva el `main()` y permite probar directamente las funciones. En compilación normal, el `main()` sí se incluye y el programa corre en consola.

---

## Nota sobre `clock_stubs.c`

Existe un archivo auxiliar llamado `clock_stubs.c` que define **implementaciones débiles (stubs)** de las funciones obligatorias.  
- Si las funciones no están implementadas en `main.c`, el linker usa los stubs y el tester marca `[FAIL]`.  
- Si las funciones sí están implementadas, las definiciones reales reemplazan a los stubs y el tester valida con `assert` y marca `[PASS]`.  

Esto asegura que las pruebas siempre se puedan ejecutar y que el feedback sea claro:  
- `[FAIL] función not implemented` → aún falta implementarla.  
- `[PASS]` → la función está correcta.

---

## Funciones obligatorias

El alumno debe implementar **exactamente** las siguientes funciones en `main.c`.  
Cada sección explica lo que se espera de la función.

---

### 1. `parse_time`

```c
int parse_time(const char *time_str, int *h, int *m, int *s);
```

**Responsabilidad:**  
- Recibir la cadena ingresada por el usuario en formato `HH:MM:SS`.  
- Convertirla a valores numéricos (`hour`, `minute`, `second`) usando `sscanf`.  
- Retornar el número de conversiones exitosas (debe ser 3 si el formato es correcto).  

**Prueba esperada:**  
- `parse_time("12:34:56", &h, &m, &s)` debe asignar `h=12, m=34, s=56` y retornar `3`.

---

### 2. `validate_time`

```c
int validate_time(int h, int m, int s);
```

**Responsabilidad:**  
- Verificar que los valores estén dentro de los rangos válidos:  
  - `hour` entre 0 y 23  
  - `minute` entre 0 y 59  
  - `second` entre 0 y 59  
- Retornar `1` si son válidos, `0` si no lo son.  

**Prueba esperada:**  
- `validate_time(23,59,59)` → `1`  
- `validate_time(25,10,10)` → `0`

---

### 3. `print_time`

```c
void print_time(int h, int m, int s);
```

**Responsabilidad:**  
- Imprimir la hora en consola con el formato:  

```
Hora actual: HH:MM:SS
```

- Usar `\r` para sobrescribir la misma línea.  
- Usar `fflush(stdout)` para forzar la salida inmediata.  

**Prueba esperada:**  
- `print_time(9,5,3)` debe mostrar `Hora actual: 09:05:03`.

---

### 4. `next_second`

```c
int next_second(int s);
```

**Responsabilidad:**  
- Incrementar los segundos en 1.  
- Si llega a 60, reiniciar a 0.  
- Retornar el nuevo valor de segundos.  

**Prueba esperada:**  
- `next_second(58)` → `59`  
- `next_second(59)` → `0`

---

### 5. `next_minute`

```c
int next_minute(int m, int s);
```

**Responsabilidad:**  
- Incrementar los minutos **solo cuando los segundos vuelven a 0**.  
- Si llega a 60, reiniciar a 0.  
- Retornar el nuevo valor de minutos.  

**Prueba esperada:**  
- `next_minute(10,0)` → `11`  
- `next_minute(59,0)` → `0`  
- `next_minute(10,5)` → `10` (no cambia porque segundos ≠ 0)

---

### 6. `next_hour`

```c
int next_hour(int h, int m, int s);
```

**Responsabilidad:**  
- Incrementar las horas **solo cuando minutos y segundos vuelven a 0**.  
- Si llega a 24, reiniciar a 0.  
- Retornar el nuevo valor de horas.  

**Prueba esperada:**  
- `next_hour(10,0,0)` → `11`  
- `next_hour(23,0,0)` → `0`  
- `next_hour(10,5,0)` → `10` (no cambia porque minutos ≠ 0)

---

## Librerías obligatorias

```c
#include <stdio.h>
#include <unistd.h>
```

---

## Defines obligatorios

```c
#define MAX_HOUR    23
#define MAX_MINUTE 59
#define MAX_SECOND 59

#define TIME_STR_LEN 9
```

---

## Variables obligatorias

```c
int hour;
int minute;
int second;

char time_str[TIME_STR_LEN];
```

---

## Flujo General del Programa

1. Solicitar la hora inicial al usuario  
2. Validar formato y rango de valores con `parse_time()` y `validate_time()`  
3. Mostrar la hora actual con `print_time()`  
4. Esperar un segundo con `sleep(1)`  
5. Actualizar el tiempo con `next_second()`, `next_minute()`, `next_hour()`  
6. Repetir indefinidamente  

---

## Entradas y Salidas Esperadas

### Interfaz del Programa
- **Formato:** mensaje de explicación de uso para el usuario `Introduzca la hora en formato HH:MM:SS`.

### Entrada del Programa
- **Formato:** cadena en consola con la hora inicial en formato `HH:MM:SS`.
- **Ejemplo válido:**  
  ```
  12:34:56
  ```
- **Ejemplo inválido:**  
  ```
  99:12:00
  ```

### Salida del Programa
- **Formato:** impresión continua en consola de la hora actual, actualizada cada segundo.  
- **Ejemplo:**  
  ```
  Hora actual: 12:34:56
  Hora actual: 12:34:57
  Hora actual: 12:34:58
  ...
  ```

---

### Entradas y Salidas por Función

| Función | Entrada | Salida esperada |
|---------|---------|-----------------|
| `parse_time(const char *time_str, int *h, int *m, int *s)` | `"12:34:56"` | Retorna `3`, asigna `h=12, m=34, s=56` |
| `validate_time(int h, int m, int s)` | `(23,59,59)` | `1` (válido) |
| | `(25,10,10)` | `0` (inválido) |
| `print_time(int h, int m, int s)` | `(9,5,3)` | Imprime `Hora actual: 09:05:03` |
| `next_second(int s)` | `58` | `59` |
| | `59` | `0` |
| `next_minute(int m, int s)` | `(10,59)` | `11` |
| | `(59,59)` | `0` |
| | `(10,5)` | `10` (sin cambio) |
| `next_hour(int h, int m, int s)` | `(10,59,59)` | `11` |
| | `(23,59,59)` | `0` |
| | `(10,5,0)` | `10` (sin cambio) |

---

## Restricciones Generales

* Todo el código debe estar en `main.c`  
* No se permite usar punteros en la lógica del reloj (solo en `parse_time`)  
* No se permite usar arreglos dinámicos  
* No se permite obtener la hora del sistema  
* No se permite usar librerías adicionales  

---

## Nota Final

Este ejercicio no busca crear un reloj preciso, sino desarrollar la capacidad de **razonar sistemas secuenciales**, practicar el manejo de strings y comprender el control del tiempo en C.  

---

**Autor:** Jesús Salvador López Ortega  
[LinkedIn](https://www.linkedin.com/in/jesus-salvador-lopez-ortega/) | [GitHub](https://github.com/chucholoport) | [Correo Institucional](mailto:jlopez@upsrj.edu.mx)
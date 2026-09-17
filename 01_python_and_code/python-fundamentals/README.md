# Python Fundamentals & Algorithmic Problem Solving

Este repositorio reúne implementaciones canónicas de algoritmos fundamentales, manejo de estructuras de datos nativas (str, list, dict, set, tuple) y operaciones matriciales en Python puro, sin dependencias externas para la lógica de negocio.

Cada módulo incluye pruebas unitarias automatizadas con pytest que verifican tanto los casos nominales como los casos límite (edge cases).

---

## Índice de Módulos

1. 01. Secuencias y Cadenas (01_sequences_and_strings)
   - maximo_clientes_concurrencia
   - racha_maxima_positiva
2. 02. Estructuras de Datos y Agregación (02_data_structures)
   - compilar_censo_coral
   - es_obra_representable
3. 03. Recorrido e Indexación de Matrices (03_matrices_and_grids)
   - buscar_coordenadas_multiples
4. 04. Matemáticas y Simulaciones Discretas (04_math_and_simulations)
   - tiempo_desintegracion_cafeina
   - validar_dni & filtrar_dnis_invalidos

---

## 1. Secuencias y Cadenas

Ubicación: 01_sequences_and_strings/time_series_streaks.py

### maximo_clientes_concurrencia(registro: str) -> int

* Objetivo: Calcular el pico máximo de personas presentes de forma simultánea en un recinto a lo largo de un historial cronológico de entradas y salidas.
* Entrada: registro (cadena de texto compuesta por caracteres 'e' o 'E' para entrada, y 's' o 'S' para salida).
* Salida: int representando la cantidad máxima de personas que coincidieron al mismo tiempo.
* Cómo funciona:
  1. Mantiene dos contadores en memoria: actual (ocupación en el instante t) y pico_maximo (el récord histórico alcanzado).
  2. Itera secuencialmente por cada carácter:
     - Si es 'e': incrementa actual en 1. Si actual > pico_maximo, actualiza el récord.
     - Si es 's': decrementa actual en 1 usando max(0, actual - 1) para evitar aforos negativos si los datos de entrada traen registros inconsistentes.
  3. Al terminar la secuencia, retorna pico_maximo.
* Ejemplo:
  maximo_clientes_concurrencia("eeseeessss") # Retorna: 4
* Complejidad: Tiempo: O(n) | Espacio auxiliar: O(1).

---

### racha_maxima_positiva(secuencia: str) -> int

* Objetivo: Identificar la racha consecutiva más larga de periodos con balance positivo dentro de una serie temporal.
* Entrada: secuencia (cadena donde '+' indica balance positivo y '-' balance negativo).
* Salida: int con el número máximo de periodos positivos ininterrumpidos.
* Cómo funciona:
  1. Utiliza dos variables: racha_actual (longitud de la racha positiva en curso) y record_racha (la racha máxima registrada).
  2. Recorre la cadena:
     - Si encuentra '+': suma 1 a racha_actual y evalúa si supera record_racha.
     - Si encuentra '-': rompe la continuidad y resetea racha_actual = 0.
  3. Retorna record_racha.
* Ejemplo:
  racha_maxima_positiva("+-++---++++-++") # Retorna: 4
* Complejidad: Tiempo: O(n) | Espacio auxiliar: O(1).

---

## 2. Estructuras de Datos y Agregación

Ubicación: 02_data_structures/choir_resource_allocator.py

### compilar_censo_coral(cantantes: list) -> dict

* Objetivo: Transformar un listado desestructurado de integrantes en un inventario estandarizado por cuerda vocal, contabilizando tanto el volumen total como los solistas disponibles.
* Entrada: Lista de tuplas con el formato [(nombre, cuerda, es_solista), ...].
  Ejemplo: [("María", "soprano", True), ("Carlos", "tenor", False)].
* Salida: Diccionario donde cada cuerda vocal contiene una lista de dos enteros: {"cuerda": [total_cantantes, total_solistas]}.
* Cómo funciona:
  1. Inicializa un diccionario con las 4 cuerdas estándar ("soprano", "contralto", "tenor", "bajo") con valores base [0, 0]. Esto garantiza consistencia de claves incluso si alguna cuerda no tiene integrantes.
  2. Itera sobre la lista de cantantes; si la cuerda es válida:
     - Incrementa el índice 0 (total de integrantes de esa voz).
     - Si el flag es_solista es True, incrementa el índice 1 (solistas calificados).
* Ejemplo:
  cantantes = [("Ana", "soprano", True), ("Luis", "soprano", False)]
  compilar_censo_coral(cantantes)
  # Retorna: {'soprano': [2, 1], 'contralto': [0, 0], 'tenor': [0, 0], 'bajo': [0, 0]}
* Complejidad: Tiempo: O(n) | Espacio auxiliar: O(1) (diccionario de tamaño fijo).

---

### es_obra_representable(censo_disponible: dict, requisitos_obra: dict) -> bool

* Objetivo: Validar si un censo de personal cubre los requerimientos mínimos de una partitura u obra musical.
* Entrada:
  * censo_disponible: Diccionario con el formato {"cuerda": [total_disp, solistas_disp]}.
  * requisitos_obra: Diccionario con los mínimos exigidos {"cuerda": [total_req, solistas_req]}.
* Salida: bool (True si se cumplen todos los mínimos, False si hay déficit en algún rol).
* Cómo funciona:
  1. Aplica un patrón de salida temprana (fail-fast): recorre cada cuerda exigida en requisitos_obra.
  2. Si la cuerda requerida no existe en el censo disponible, retorna False de inmediato.
  3. Si la cantidad disponible es menor a la requerida (en total o en solistas), retorna False.
  4. Si todas las condiciones se satisfacen para todas las cuerdas, retorna True.
* Complejidad: Tiempo: O(k) donde k es el número de requisitos | Espacio auxiliar: O(1).

---

## 3. Recorrido e Indexación de Matrices

Ubicación: 03_matrices_and_grids/manual_matrix_search.py

### buscar_coordenadas_multiples(matriz: list, elementos_busqueda: list) -> dict

* Objetivo: Localizar todas las posiciones espaciales (fila, columna) de uno o varios elementos dentro de una cuadrícula 2D regular.
* Entrada:
  * matriz: Lista de listas que representa una matriz bidimensional de dimensiones R x C.
  * elementos_busqueda: Lista con los valores objetivo a localizar.
* Salida: Diccionario donde cada elemento buscado apunta a una lista de tuplas con sus coordenadas: {elemento: [(fila, col), ...]}. Si un elemento no existe en la matriz, su lista asociada retorna vacía [].
* Cómo funciona:
  1. Inicializa el diccionario de resultados mapeando cada elemento de búsqueda a una lista vacía.
  2. Recorre la matriz celda a celda mediante bucles anidados con índices (i para filas, j para columnas).
  3. En cada celda, evalúa si matriz[i][j] coincide con alguno de los elementos en el diccionario de resultados. De ser así, añade la tupla (i, j).
* Ejemplo:
  grid = [
      [1, 2, 3],
      [5, 6, 3],
      [9, 7, 3]
  ]
  buscar_coordenadas_multiples(grid, [3, 6, 99])
  # Retorna: {3: [(0, 2), (1, 2), (2, 2)], 6: [(1, 1)], 99: []}
* Complejidad: Tiempo: O(R x C) | Espacio auxiliar: O(M) donde M es el número de coincidencias encontradas.

---

## 4. Matemáticas y Simulaciones Discretas

Ubicación: 04_math_and_simulations/

### tiempo_desintegracion_cafeina(tazas: int, umbral_mg: float = 10.0, mg_por_taza: float = 98.0) -> int
Archivo: caffeine_decay.py

* Objetivo: Simular la eliminación metabólica de cafeína en el cuerpo humano bajo un modelo discreto de vida media (t_1/2 = 5 h).
* Entrada: tazas ingeridas, umbral_mg (concentración residual objetivo, por defecto 10 mg) y mg_por_taza (dosis base, por defecto 98 mg).
* Salida: int con el total de horas acumuladas para que la concentración decaiga por debajo del umbral.
* Cómo funciona:
  1. Calcula la dosis inicial: cafeina_restante = tazas * mg_por_taza.
  2. Ejecuta un bucle while cafeina_restante > umbral_mg:
     - Reduce la concentración a la mitad (cafeina_restante /= 2.0).
     - Suma 5 horas al contador de tiempo transcurrido.
  3. Retorna las horas totales.
* Complejidad: Tiempo: O(log(dosis total)) | Espacio auxiliar: O(1).

---

### validar_dni(dni: str) -> bool
Archivo: dni_validator.py

* Objetivo: Verificar la validez de un Documento Nacional de Identidad (DNI español) mediante el algoritmo oficial de control aritmético.
* Entrada: dni en formato cadena (ej. "12345678Z").
* Salida: bool (True si cumple formato y letra de control, False en caso contrario).
* Cómo funciona:
  1. Control de longitud: Comprueba que la cadena tenga exactamente 9 caracteres.
  2. Control de formato: Extrae los primeros 8 caracteres (num_str) y el último carácter (letra). Valida que num_str.isdigit() sea verdadero.
  3. Cálculo de residuo (Módulo 23): Convierte los 8 dígitos a entero y calcula numero % 23.
  4. Verificación de letra: Comprueba si la letra ingresada coincide con la posición del residuo en la secuencia oficial "TRWAGMYFPDXBNJZSQVHLCKE".
* Complejidad: Tiempo: O(1) | Espacio auxiliar: O(1).

---

### filtrar_dnis_invalidos(lista_dnis: list) -> list
Archivo: dni_validator.py

* Objetivo: Filtrar una lista de documentos y aislar aquellos que presenten errores de formato o discordancia en el dígito de control.
* Entrada: Lista de cadenas ["12345678Z", "00000000T", "14879544S"].
* Salida: Lista únicamente con los elementos que resultaron inválidos.
* Cómo funciona: Utiliza una lista por comprensión invocando a validar_dni(dni) como predicado de filtrado: [dni for dni in lista_dnis if not validar_dni(dni)].
* Complejidad: Tiempo: O(N) donde N es la cantidad de DNIs en la lista.

---

## Ejecución de Pruebas Automatizadas

El proyecto utiliza pytest para la ejecución y reporte de pruebas.

```bash
# 1. Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# 2. Ejecutar todas las suites de prueba en modo detallado
python -m pytest -v

# 3. Generar un archivo de auditoría con los resultados
python -m pytest -v > test_report.txt
# Personal Finance Tracker (CLI)

> **Contexto de aprendizaje:** Proyecto de práctica desarrollado siguiendo el tutorial de [Tech With Tim](https://www.youtube.com/@TechWithTim). Orientado a la ejercitación de lógica de consola, validaciones de entrada, persistencia local con archivos planos y visualización de series temporales.

---

## 📌 Descripción del Proyecto

Aplicación interactiva por línea de comandos (CLI) que permite gestionar un registro personal de ingresos y gastos. Entre sus funcionalidades se encuentran:

* Registro de transacciones con fecha, monto, categoría (`Income` / `Expense`) y descripción.
* Validación estricta de datos ingresados por consola (formatos de fecha y valores numéricos).
* Consulta y filtrado de transacciones dentro de rangos temporales determinados.
* Resumen financiero automático (ingresos totales, gastos totales y ahorro neto).
* Generación de gráficos comparativos de ingresos y gastos a lo largo del tiempo con `matplotlib`.

---

## 🛠️ Tecnologías Empleadas

* **Python 3.x**
* **Pandas**: Filtrado condicional, conversiones de fecha y agregación temporal (`resample`).
* **Matplotlib**: Visualización gráfica de series temporales.
* **Módulo nativo `csv`**: Escritura y persistencia de filas transaccionales.

---

## ⚙️ Notas Técnicas y Resolución de Problemas

Durante el desarrollo de esta práctica sobre versiones modernas del ecosistema de Python (Python 3.12+ y versiones recientes de Pandas), se identificaron y solucionaron inconsistencias respecto al tutorial original:

### 1. Incompatibilidad de tipos en `reindex(fill_value=0)`
* **Problema:** En el código original del tutorial, se aplica `.reindex(..., fill_value=0)` sobre un DataFrame completo que conserva columnas de tipo texto/objeto (`category`, `description`). En versiones recientes de Pandas (con tipado estricto para strings), esta operación produce el siguiente error:
  ```text
  TypeError: Invalid value '0' for dtype 'str'. Value should be a string or missing value, got 'int' instead.
  ```
* **Solución técnica:** Se aisló la columna numérica `amount` antes de ejecutar la agregación y el remuestreo (`resample("D").sum()`). Al transformar la serie de valores estrictamente numéricos antes de invocar `.reindex()`, se evita que Pandas intente insertar ceros enteros en columnas de texto.

### 2. Comportamiento en consola y persistencia
* Al invocar la inicialización (`CSV.initialize_csv()`), la biblioteca no imprime mensajes a menos que se indiquen de forma explícita. El archivo `finance_data.csv` se genera en el directorio de trabajo activo con sus cabeceras base (`date,amount,category,description`).

---

## 📂 Estructura de Archivos

```text
python_personal_finance_tracker/
│
├── main.py              # Clase CSV, menú principal y visualización con matplotlib
├── data_entry.py        # Funciones auxiliares para captura y validación de inputs
├── finance_data.csv     # Archivo local de persistencia de transacciones
└── README.md            # Documentación y notas de aprendizaje
```

---

## 🚀 Instalación y Ejecución

1. **Clonar o descargar el repositorio:**
   ```powershell
   cd python_personal_finance_tracker
   ```

2. **Instalar dependencias necesarias:**
   ```powershell
   pip install pandas matplotlib
   ```

3. **Ejecutar el programa:**
   ```powershell
   py main.py
   ```

---

## 📖 Créditos

* Concepto y estructura didáctica original: **Tech With Tim** ([YouTube](https://www.youtube.com/@TechWithTim)).
* Ajustes de compatibilidad, resolución de excepciones de tipado en Pandas y notas técnicas: Implementación personal de estudio.
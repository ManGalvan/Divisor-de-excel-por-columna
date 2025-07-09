# 🧾 Divisor_excel_por_columna

Este script permite dividir un archivo de Excel (.xlsx) en múltiples archivos, agrupando los datos según una columna específica.

---

## 📌 Descripción

El script tiene como objetivo leer un archivo de Excel, agrupar los datos en función de una columna específica, y generar archivos separados por cada grupo encontrado. Es útil para tareas de segmentación de datos y distribución automatizada de reportes por cliente, categoría, grupo, etc.

---

## 📥 Requisitos

- Python 3.7+
- Librerías:
  - `pandas`
  - `openpyxl`

Instalación:

```bash
pip install pandas openpyxl
```

---

## 🧠 Uso

```python
from script import dividir_excel_por_columna

resultado = dividir_excel_por_columna("clientes.xlsx", "Cliente")

print("Archivos generados:", resultado["archivos_creados"])
print("Errores:", resultado["errores"])
```

---

## 🧪 Ejemplo de entrada

**clientes.xlsx:**

| Cliente  | Monto |
|----------|--------|
| Juan     | 100    |
| Ana      | 200    |
| Juan     | 300    |

---

## 📤 Salida esperada

En la carpeta `archivos_individuales/`:

```
├── Juan.xlsx
└── Ana.xlsx
```

---

## ✅ Validaciones implementadas

- Archivo existe y es legible.
- La columna agrupadora existe.
- La columna contiene al menos un valor válido.
- Se limpian caracteres inválidos en los nombres de archivo.

---

## 📋 Retorno

Un diccionario:

```python
{
  "archivos_creados": ["Juan.xlsx", "Ana.xlsx"],
  "errores": []
}
```

---

## 🔧 Ampliaciones recomendadas

- Exportación a CSV.
- Log en archivo TXT.
- Interfaz gráfica con Tkinter.
- Integración con APIs para envío automático.

---

## 📄 Licencia

MIT

import pandas as pd
import os
import re
 
def dividir_excel_por_columna(archivo_entrada, columna_agrupadora, carpeta_salida="archivos_individuales"):
    resultados = {"archivos_creados": [], "errores": []}
    try:
        if not os.path.isfile(archivo_entrada):
            raise FileNotFoundError(f"El archivo '{archivo_entrada}' no existe.")
        
        os.makedirs(carpeta_salida, exist_ok=True)
 
        try:
            df = pd.read_excel(archivo_entrada)
        except Exception as e:
            raise ValueError(f"Error al leer el archivo: {e}")
 
        if columna_agrupadora not in df.columns:
            raise KeyError(f"La columna '{columna_agrupadora}' no existe en el archivo.")
 
        if df[columna_agrupadora].dropna().empty:
            raise ValueError(f"La columna '{columna_agrupadora}' no contiene valores válidos.")
 
        grupos = df.groupby(columna_agrupadora)
 
        for nombre_grupo, datos_grupo in grupos:
            if pd.isna(nombre_grupo):
                continue
            nombre_archivo = re.sub(r'[<>:"/\\|?*]', '-', str(nombre_grupo).strip())
            nombre_archivo = f"{nombre_archivo}.xlsx"
            ruta_salida = os.path.join(carpeta_salida, nombre_archivo)
 
            try:
                datos_grupo.to_excel(ruta_salida, index=False)
                resultados["archivos_creados"].append(nombre_archivo)
            except Exception as e:
                resultados["errores"].append((nombre_archivo, str(e)))
 
        return resultados
 
    except Exception as e:
        resultados["errores"].append(("global", str(e)))
        return resultados
    
if __name__ == "__main__":
    archivo = "nombre_del_archivo.xlsx" # Remplazar con el nombre correcto del archivo
    columna = "Columna divisora"    # Remplazar con el nombre correcto de la columna presente en el archivo
    print(dividir_excel_por_columna(archivo, columna))
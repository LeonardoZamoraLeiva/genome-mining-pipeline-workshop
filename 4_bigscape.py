#!/usr/bin/env python3
import os
import sys
import subprocess

input_dir = sys.argv[1]
output_dir = sys.argv[2]
os.makedirs(output_dir, exist_ok=True)

print("🕸️ Generando redes de similitud con BiG-SCAPE...")

# Comando de BiG-SCAPE. 
# Usamos --include_singletons para que los nodos aparezcan en el HTML aunque no formen familias.
# Usamos --mix para que compare todas las clases de BGCs entre sí.
comando = f"bigscape -i {input_dir} -o {output_dir} --mix --hybrids-off --mode auto --cutoff 0.6 --include_singletons --mix --cores 2"

print(f"   ▶️ Ejecutando: {comando} (Esto tomará un momento...)")

# Ejecutamos ocultando la salida excesiva de texto para mantener la terminal limpia
subprocess.run(comando, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"✅ ¡Redes generadas! Revisa la carpeta: {output_dir}")
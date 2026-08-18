#!/usr/bin/env python3
import os
import sys
import glob
import subprocess
import shutil

input_dir = sys.argv[1]
output_dir = sys.argv[2]
os.makedirs(output_dir, exist_ok=True)

# Buscar los archivos GBK generados por Prokka en las subcarpetas
gbks = glob.glob(f"{input_dir}/*/*.gbk")
print(f"🔍 Ejecutando antiSMASH real en {len(gbks)} secuencias...")

for gbk in gbks:
    # Obtenemos el nombre base sin la extensión
    nombre = os.path.basename(gbk).replace(".gbk", "")
    
    # antiSMASH requiere una carpeta de salida específica para cada corrida
    out_antismash = os.path.join(output_dir, f"{nombre}_asmash")
    
    # Armamos el comando de antiSMASH. 
    # Agregamos --minimal para que sea más rápido durante la clase.
    comando = f"antismash {gbk} --output-dir {out_antismash} --taxon bacteria --minimal"
    
    print(f"   ▶️ Analizando: {nombre} (Esto puede tomar un minuto...)")
    
    # Ejecutamos el comando en la terminal
    subprocess.run(comando, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Al terminar, antiSMASH generó archivos que terminan en ".region001.gbk".
    # Vamos a buscar esos archivos específicos y los copiaremos a la raíz de la carpeta 3_bgcs
    # para que el script 4_clinker.py los encuentre fácilmente.
    regiones = glob.glob(f"{out_antismash}/*.region*.gbk")
    
    for region in regiones:
        nombre_region = os.path.basename(region)
        destino = os.path.join(output_dir, nombre_region)
        shutil.copy(region, destino)
        print(f"   ✅ BGC detectado y extraído: {nombre_region}")

print("✅ Todos los análisis de antiSMASH han finalizado.")
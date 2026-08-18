#!/usr/bin/env python3
import os
import sys
import subprocess

input_dir = sys.argv[1]
output_html = sys.argv[2]

print("📊 Generando red de sintenia con Clinker...")

# Comando Clinker: Toma todos los GBK de la carpeta de entrada
comando = f"clinker {input_dir}/*.gbk -p {output_html}"
subprocess.run(comando, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"✅ ¡Pipeline finalizado! Abre este archivo en tu navegador: {output_html}")
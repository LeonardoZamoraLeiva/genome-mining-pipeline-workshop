#!/usr/bin/env python3
import os
import sys
import subprocess
import glob

input_dir = sys.argv[1]
output_dir = sys.argv[2]
os.makedirs(output_dir, exist_ok=True)

fastas = glob.glob(f"{input_dir}/*.fasta")
print(f"🧬 Anotando {len(fastas)} secuencias con Prokka...")

for fasta in fastas:
    nombre = os.path.basename(fasta).replace(".fasta", "")
    out_prokka = os.path.join(output_dir, f"{nombre}_prokka")
    
    # Comando de Prokka optimizado para bacterias
    comando = f"prokka --prefix {nombre} --outdir {out_prokka} --kingdom Bacteria --cpus 2 {fasta}"
    
    subprocess.run(comando, shell=True)
    print(f"   - Anotado: {nombre}")
#!/usr/bin/env python3
import urllib.request
import sys
import os

# sys.argv[1] lee la carpeta que le pasemos desde la terminal
out_dir = sys.argv[1]
os.makedirs(out_dir, exist_ok=True)

# Diccionario con las URLs exactas y pre-validadas de MIBiG
bgc_urls = {
    "BGC0000852": "https://mibig.secondarymetabolites.org/repository/BGC0000852.5/BGC0000852.gbk",
    "BGC0000853": "https://mibig.secondarymetabolites.org/repository/BGC0000853.3/BGC0000853.gbk",
    "BGC0000854": "https://mibig.secondarymetabolites.org/repository/BGC0000854.3/BGC0000854.gbk"
}

#bgc_urls = {
#    "BGC0000852": "https://mibig.secondarymetabolites.org/repository/BGC0000836.5/BGC0000336.gbk",
#    "BGC0000853": "https://mibig.secondarymetabolites.org/repository/BGC0000291.5/BGC0000291.gbk",
#    "BGC0000854": "https://mibig.secondarymetabolites.org/repository/BGC0000315.5/BGC0000315.gbk"
#}

print(f"📥 Descargando {len(bgc_urls)} clústeres desde MIBiG...")

for bgc_id, url in bgc_urls.items():
    gbk_path = os.path.join(out_dir, f"{bgc_id}.gbk")
    fasta_path = os.path.join(out_dir, f"{bgc_id}.fasta")
    
    # 1. Descargamos el archivo GBK original
    try:
        urllib.request.urlretrieve(url, gbk_path)
    except Exception as e:
        print(f"Error descargando {bgc_id}: {e}")
        continue
    
    # 2. Extraemos solo el ADN y lo guardamos como FASTA
    with open(gbk_path, 'r') as gbk, open(fasta_path, 'w') as fasta:
        seq = ""
        in_origin = False
        for line in gbk:
            if line.startswith("ORIGIN"):
                in_origin = True
                continue
            if in_origin:
                if line.strip() == "//":
                    break
                # Limpiar números y espacios de la secuencia de ADN
                clean_line = ''.join([c for c in line if c.isalpha()])
                seq += clean_line.upper()
        
        # Formatear como FASTA estándar
        fasta.write(f">{bgc_id} secuencia_cruda\n")
        for i in range(0, len(seq), 80):
            fasta.write(seq[i:i+80] + "\n")
            
    # Borramos el GBK original para obligar a los alumnos a usar Prokka
    os.remove(gbk_path)
    print(f"   ✅ {bgc_id} descargado y convertido a FASTA.")
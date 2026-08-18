#!/bin/bash

echo "========================================"
echo "🚀 PIPELINE AUTOMATIZADO DE MINERÍA"
echo "========================================"

# Habilitar el uso de 'conda activate' dentro del script
source /miniconda3/etc/profile.d/conda.sh

# Definimos los nombres de las carpetas y archivos
DATA_DIR="1_raw_data"
PROKKA_DIR="2_annotated"
BGC_DIR="3_bgcs"
BIGSCAPE_DIR="4_bigscape_results"
CLINKER_OUT="5_sintenia_ectoina.html"

# Limpiamos ejecuciones previas (incluyendo el nuevo archivo de Clinker)
rm -rf $DATA_DIR $PROKKA_DIR $BGC_DIR $BIGSCAPE_DIR $CLINKER_OUT

echo "🔄 Activando entorno de Anotación (Prokka_Global)..."
conda activate /miniconda3/envs/Prokka_Global

# Paso 1: Descargar (Genera FASTA)
python3 1_download.py $DATA_DIR

# Paso 2: Anotar (Genera GBKs completos)
python3 2_annotate.py $DATA_DIR $PROKKA_DIR

echo "🔄 Cambiando a entorno de Minería Genómica (GenomeMining_Global)..."
conda activate /miniconda3/envs/GenomeMining_Global

# Paso 3: Minería (antiSMASH y extracción de las regiones BGC)
python3 3_antismash.py $PROKKA_DIR $BGC_DIR

echo "🔄 Cambiando a entorno de Topología (bigscape)..."
conda activate /miniconda3/envs/bigscape/

# Paso 4: Construir la red de BGCs con BiG-SCAPE
python3 4_bigscape.py $BGC_DIR $BIGSCAPE_DIR

echo "🔄 Cambiando a entorno de Sintenia (clinker_env)..."
# OJO: Ajusta esta ruta si el ambiente clinker_env queda instalado en otra dirección
conda activate /miniconda3/envs/clinker_env

# Paso 5: Generar visualización con Clinker
# Clinker lee los mismos archivos GBK extraídos en el Paso 3
python3 5_clinker.py $BGC_DIR $CLINKER_OUT

echo "========================================"
echo "🎉 TALLER COMPLETADO EXITOSAMENTE"
echo "========================================"
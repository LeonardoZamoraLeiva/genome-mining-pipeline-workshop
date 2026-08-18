<img width="228" height="147" alt="logo" src="https://github.com/user-attachments/assets/4de329ff-cfa9-422b-97fa-0d595a0f1fec" />
# Taller de Minería Genómica: Automatización y visualización (Sesión C9)

Bienvenido al repositorio oficial de la sesión **C9 - Other Tools**. En este taller práctico aprenderás los conceptos básicos de diseñar, estructurar y ejecutar un pipeline bioinformático automatizado utilizando la terminal de Linux, Python y Bash para procesar BGCs.

---

## 1. ¿Qué es un Pipeline Bioinformático y por qué se utiliza?

Un **pipeline bioinformático** es una serie de programas o herramientas de software organizadas secuencialmente y en un orden específico, donde la salida (*output*) de un paso se convierte automáticamente en la entrada (*input*) del siguiente paso.

<img width="1625" height="480" alt="Presentación1" src="https://github.com/user-attachments/assets/c1878ae7-e598-4315-a2d5-0534a297cca9" />

### ¿Para qué sirve y por qué se utiliza?
* **Manejo de Big Data:** Analizar un genoma a mano es viable. Analizar cientos de genomas requiere una inversión de tiempo mayor. Adicionalmente, permite eliminar tiempos muertos ya que software puede trabajar solo.
* **Reproducibilidad:** Permite que cualquier investigador en el mundo corra exactamente el mismo análisis con los mismos parámetros y obtenga el mismo resultado.
* **Eficiencia y Tiempo:** Los análisis repetitivos suelen ser tediosos, lo cual aumenta progresivamente la probabilidad de errores humanos. La automatización reduce drásticamente elimina los errores asociados a tener que tipear comandos repetitivos cientos de veces.
* **Control de errores:** Si un análisis masivo se interrumpe en el genoma número 90, un pipeline bien estructurado puede reanudarse desde el punto de falla sin tener que empezar desde cero.

---

## 2. Pasos Comunes en un Pipeline Bioinformático

A grandes rasgos, la mayoría de los flujos de trabajo en bioinformática siguen una estructura lógica de cuatro etapas esenciales:

1. **Recolección/Descarga de Datos:** Obtención de datos crudos (FASTQ de secuenciación, FASTAs de NCBI, BGCs de bases de datos como MIBiG, etc.).
2. **Pre-procesamiento y Control de Calidad:** Filtrado de lecturas de baja calidad, remoción de adaptadores o eliminación de genomas muy fragmentados, etc.
3. **Análisis Central:** El procesamiento biológico pesado (ensamblaje, anotación de genes, alineamientos, o predicción metabólica).
4. **Interpretación y Visualización:** Conversión de tablas densas de datos en gráficos interactivos, árboles filogenéticos/filogenómicos o redes visuales.

---

## 3. Tres Formas de Crear o Unir un Pipeline Bioinformático

Dependiendo del nivel de personalización necesario y las habilidades de programación, existen tres aproximaciones comunes:

### A. Encadenamiento de Códigos (Linking Scripts)
Consiste en escribir scripts individuales (en Python, R o cualquier lenguaje) para cada tarea. Luego, un archivo de ejecución contiene los scripts individuales y los dispara uno a uno.
* **Ventajas:** Excelente para aprender; aprovecha las habilidades básicas de programación que ya posees sin necesidad de instalar software complejo. Además, el control del proceso es total, ya que es el mismo usuario quien escribe cada paso del código, conoce los outputs de cada software y los resultados de cada paso.
* **Desventajas:** Es frágil a gran escala. Si un paso intermedio falla, el script central puede continuar corriendo a ciegas, arrastrando el error. Requiere una gran planificación en cada paso.

### B. Sistemas de Gestión de Flujos de Trabajo (Workflow Management Systems)
Herramientas avanzadas construidas específicamente para bioinformática, como **Snakemake** o **Nextflow**.
* **Ventajas:** Ecosistemas robustos, manejan de forma nativa la paralelización (uso de múltiples núcleos del servidor), gestionan entornos virtuales automáticamente y permiten reanudar procesos caídos. Además, suelen poseer herramientas que monitorean el uso de RAM o CPU en cada paso del pipeline.
* **Desventajas:** Curva de aprendizaje empinada y sintaxis abstracta al inicio.
  
<img width="614" height="103" alt="{45AE9C8B-E478-412A-92D4-C2E2DE55FFF7}" src="https://github.com/user-attachments/assets/2f02299c-7efd-4ddf-90e0-1f34a5f421fa" />
<img width="614" height="103" alt="image" src="https://github.com/user-attachments/assets/28918a95-3802-46dc-aa80-d83fd7d73f58" />

### C. Interfaces Gráficas de Usuario (GUI)
Plataformas web o de escritorio como **Galaxy**.
* **Ventajas:** Ideal para biólogos de laboratorio húmedo (*wet-lab*) que no saben programar. Permite arrastrar y soltar herramientas visualmente.
* **Desventajas:** Poca flexibilidad para análisis altamente personalizados y dependencia total de la capacidad de servidores públicos compartidos.
* 
<img width="1088" height="604" alt="{F4A44E74-1CD0-4F23-BF67-9B9AB4339654}" src="https://github.com/user-attachments/assets/67878f5a-e9e1-40ff-b628-fb943ae5e3b1" />

---

## 4. Nuestro Objetivo: El Flujo Lógico de Minería Genómica

En este taller replicaremos el diseño de un flujo de trabajo típico para descubrir metabolitos secundarios a partir de datos genómicos crudos. Los pasos lógicos que automatizaremos son:

[1. Descarga] ➔ [2. Anotación] ➔ [3. Minería BGC] ➔ [4. Redes de Correlación] ➔ [5. Comparación de BGCs]
(MIBiG)         (Prokka)        (antiSMASH)          (BiG-SCAPE)         (Clinker)

1. **Buscar y descargar:** Obtener las secuencias de nucleótidos de las regiones de interés.
2. **Anotar y evaluar:** Identificar las coordenadas de las regiones codificantes (CDS) en el ADN crudo.
3. **Minar con antiSMASH:** Detectar los clústeres de genes responsables de producir metabolitos secundarios.
4. **Generar redes con BiG-SCAPE:** Agrupar los BGCs detectados en Familias de Clústeres Génicos (GCFs) según su distancia evolutiva.
5. **Comparar con Clinker:** Alinear gen a gen los BGCs de interés para evaluar visualmente inserciones, deleciones o rearreglos.

---

## 5. ¿Qué es Clinker?

**Clinker** es una herramienta bioinformática de última generación diseñada para visualizar de manera interactiva la **sintenia** de clústeres de genes. 

A diferencia de los alineamientos globales de genomas, Clinker se enfoca en regiones específicas (como los BGCs). Lee archivos anotados (GenBank), traduce las secuencias a proteínas, realiza alineamientos locales por parejas y genera un mapa lineal interactivo en formato HTML. Los usuarios pueden arrastrar clústeres, cambiar colores de genes y analizar dinámicamente la arquitectura de los operones directamente en el navegador web sin instalar visores locales.

---

## 6. Guía de los Scripts de Muestra del Repositorio

Para el ejercicio práctico, contamos con 5 scripts modulares coordinados por un archivo maestro de Bash. Esta es la función general de cada bloque:

### 📑 `1_download.py`
**Propósito:** Interfaz de adquisición de datos.
* **Qué hace:** Se conecta a la base de datos MIBiG de forma remota y descarga archivos GenBank de tres variantes evolutivas conocidas del operón de la ectoína. Para hacer el ejercicio realista, el script extrae el ADN crudo de la sección `ORIGIN`, borra las anotaciones previas y guarda archivos `.fasta` limpios.

### 🧬 `2_annotate.py`
**Propósito:** Anotación e identificación de características genómicas.
* **Qué hace:** Escanea la carpeta de datos crudos y lanza de manera secuencial la herramienta `Prokka`. Traduce el ADN crudo y genera nuevos archivos enriquecidos en formato GenBank (`.gbk`), que contienen las posiciones exactas de las proteínas predichas.

### 🔍 `3_antismash.py`
**Propósito:** Delimitación de regiones biosintéticas (Minería).
* **Qué hace:** Ejecuta `antiSMASH` con parámetros mínimos optimizados para el taller. Identifica los dominios centrales del BGC de la ectoína y extrae quirúrgicamente el archivo comprimido final de la región (`.region001.gbk`), descartando las zonas del genoma que no son de interés.

### 🕸️ `4_bigscape.py`
**Propósito:** Análisis de redes y relaciones topológicas.
* **Qué hace:** Ejecuta `BiG-SCAPE` utilizando las regiones purificadas del paso anterior. Compara las familias de genes y genera archivos de nodos y bordes en un reporte interactivo interactivo para explorar agrupamientos biológicos.

### 📊 `5_clinker.py`
**Propósito:** Visualización de sintenia de alta resolución.
* **Qué hace:** Toma las mismas regiones aisladas por antiSMASH, ejecuta alineamientos locales de proteínas y exporta el archivo interactivo final `5_sintenia_ectoina.html`.

### 🚀 `run_pipeline.sh` (El Orquestador Maestro)
**Propósito:** El cerebro del pipeline.
* **Qué hace:** Define las variables de entorno de las carpetas, borra rastros de ejecuciones erróneas del pasado para asegurar un entorno limpio, e inicializa Conda en el *subshell*. Conforme avanza, activa dinámicamente los entornos del servidor: `Prokka_Global`, `GenomeMining_Global`, `bigscape`, y finalmente `clinker_env`, logrando procesar todo el flujo de trabajo con un único comando.

---

## 🚀 Cómo Ejecutar el Taller Practico

Una vez ubicado en la terminal de tu servidor, simplemente ejecuta el comando maestro:

```bash
bash run_pipeline.sh

# Taller de Minería Genómica Avanzada: Automatización y Sintenia (Sesión C9)

Bienvenido al repositorio oficial de la sesión **C9 - Other Tools**. En este taller práctico aprenderás a diseñar, estructurar y ejecutar un pipeline bioinformático automatizado utilizando la terminal de Linux, Python y Bash para procesar clústeres de genes biosintéticos (BGCs).

---

## 1. ¿Qué es un Pipeline Bioinformático y por qué se utiliza?

Un **pipeline bioinformático** es una serie de programas o herramientas de software orquestadas en un orden específico, donde la salida (*output*) de un paso se convierte automáticamente en la entrada (*input*) del siguiente paso.

<img width="853" height="480" alt="ezgif com-gif-maker" src="https://github.com/user-attachments/assets/ae99e0be-6ab5-49f7-8504-2f272d13b974" />


### ¿Para qué sirve y por qué se utiliza?
* **Manejo de Big Data:** Analizar un genoma a mano es viable. Analizar 500 genomas requiere automatización masiva.
* **Reproducibilidad:** Permite que cualquier investigador en el mundo corra exactamente el mismo análisis con los mismos parámetros y obtenga el mismo resultado.
* **Eficiencia y Tiempo:** Reduce drásticamente el error humano al evitar tener que tipear comandos repetitivos cientos de veces.
* **Control de errores:** Si un análisis masivo se interrumpe en el genoma número 90, un pipeline bien estructurado puede reanudarse desde el punto de falla sin tener que empezar desde cero.

---

## 2. Pasos Comunes en un Pipeline Bioinformático

A grandes rasgos, la mayoría de los flujos de trabajo en bioinformática siguen una estructura lógica de cuatro etapas esenciales:

1. **Recolección/Descarga de Datos:** Obtención de datos crudos (FASTQ de secuenciación, FASTAs de NCBI, archivos de MIBiG, etc.).
2. **Pre-procesamiento y Control de Calidad:** Filtrado de lecturas de baja calidad, remoción de adaptadores o eliminación de contigs problemáticos.
3. **Análisis Central:** El procesamiento biológico pesado (ensamblaje, anotación de genes, alineamientos, o predicción metabólica).
4. **Interpretación y Visualización:** Conversión de tablas densas de datos en gráficos interactivos, mapas filogenéticos o redes visuales aptas para su publicación.

---

## 3. Tres Formas de Crear o Unir un Pipeline Bioinformático

Dependiendo del nivel de personalización necesario y las habilidades de programación, existen tres aproximaciones estándar en la industria:

### A. Encadenamiento de Códigos (Linking Scripts)
Consiste en escribir scripts individuales (en Python, R o Perl) para cada tarea y unirlos todos dentro de un archivo maestro de Bash (`.sh`).
* **Ventajas:** Excelente para aprender; aprovecha las habilidades básicas de programación que ya posees sin necesidad de instalar software complejo.
* **Desventajas:** Es frágil a gran escala. Si un paso intermedio falla, el script de Bash puede continuar corriendo a ciegas, arrastrando el error.

### B. Sistemas de Gestión de Flujos de Trabajo (Workflow Management Systems)
Herramientas avanzadas construidas específicamente para bioinformática, como **Snakemake** o **Nextflow**.
* **Ventajas:** Ultra robustos, manejan de forma nativa la paralelización (uso de múltiples núcleos del servidor), gestionan entornos virtuales automáticamente y permiten reanudar procesos caídos.
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

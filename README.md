# Práctica de MTs

![Máquina de Turing Misteriosa](assets/maquina_misteriosa.svg)

## Enunciado

Representar la máquina de Turing Misteriosa utilizando la librería automata para Python. Verificar que corran los tests y estén todos verdes.

En el archivo maquina.py hay un ejemplo de una MT implementada.

Siguiendo el diagrama de transición y completando la definición de la MT, adaptar la la_maquina_turing.

Para eso debemos:

- completar las transiciones como están en el gráfico
- agregar los estados faltantes en el set states
- adaptar los símbolos del alfabeto Sigma
- adaptar los símbolos del alfabeto de cinta
- corregir si fuera necesario el estado de aceptación

## Instrucciones

Instalar:

- python 3.9
- pip
- virtualenv

La primera vez:

```bash
python -m venv venv
``` 

## Para ejecutar

Antes de arrancar a trabajar hay que activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
pip install -r requirements.txt
```

En Linux:

```bash
. venv/bin/activate
pip install -r requirements.txt
```

Una vez activado el entorno virtual corremos los tests:

```
python -m pytest
```

## La tarea

El trabajo está completo cuando hayamos implementado la MT misteriosa en el archivo maquina.py y todos los tests den verde.

¡Éxitos!

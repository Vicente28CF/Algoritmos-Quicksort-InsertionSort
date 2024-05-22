# Algoritmos paralelos con MPI.

Este repositorio contiene una colección de algoritmos paralelos implementados en Python, utilizando MPI (Message Passing Interface) con mpi4py.

## Instalación

Para ejecutar los algoritmos en un entorno de Google COLAB, asegúrate de tener instaladas las siguientes dependencias, ademas de crear un archivo dentro de la carpeta sample:

- mpi4py

Puedes instalar las dependencias utilizando pip:

```bash
pip install mpi4py
```
Para ejecutar el algoritmo de Quicksort debes de correr este comando:
```bash
!mpiexec --oversubscribe --allow-run-as-root -np 4 python /content/sample(ruta de tu archivo)
```
Para ejecutar el algoritmo de Insertion sort debes de seguir los mismos pasos anteriores y correr este comando:
```bash
!mpiexec --oversubscribe --allow-run-as-root -np 5 python /content/sample(ruta de tu archivo)
```

## Integrantes del Equipo:

- Dante Adair Santillan Gonzalez
- Victor Alfredo Villegas Navarro
- Vicente Cayetano Flores



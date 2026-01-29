

#Sino esta creado, en Python es recomendable crear un entorno virtual
#la directiva de Bash es: python3 -m venv env

#Para activar el entorno virtual en Bash: source env/bin/activate

#Para entorno virtual vamos a Construir, Establecer comados de construc
# y reemplazamos python3 "%f" por 
# ./env/bin/python3 "%f"

#Para desactivar el entorno virtual en Bash (terminal de Linux)
#El comando es: deactivate

import sys

print("Hola Mundo, soy Horacio desde mi Raspberry Pi 500!")
print("Ejecutando desde: ", sys.executable)

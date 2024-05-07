from cx_Freeze import setup, Executable

setup(
    name="Trabajo Estrucutras de Datos",
    version="1.0",
    description="Comparador de algoritmos de ordenamiento",
    executables=[Executable("main.py", base="Win32GUI")]
)

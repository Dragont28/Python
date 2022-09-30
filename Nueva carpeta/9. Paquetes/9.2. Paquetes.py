from setuptools import setup


setup(
    
    name="operaciones_matematicas",
    decription="Operaciones matematicas",
    author="dragont28",
    version="1.0",
    author_email="",
    url="",
    packages=["paquetes","paquetes.p2"]

    )

# Abro el directorio en el cmd y ejecuto un >python setup.py sdist
# En el directorio dist que se crea lo abrimos en el cmd y ejecuto un >pip3 install "nombre del archivo"
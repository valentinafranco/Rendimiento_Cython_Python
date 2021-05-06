"""
    UNIVERSIDAD SERGIO ARBOLEDA

    Nombre: Valentina Del Pilar Franco Suárez

    Correo: valentina.franco01@correo.usa.edu.co

    Docente: Jonh Jairo Corredor

    Fecha: 05 de mayo del 2021

    Ciudad: Bogotá D.C.

    TALLER RENDIMIENTO CYTHON/PYTHON
"""
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

exts=(cythonize('cyfunctionE.pyx'))
setup(ext_modules=exts, 
      include_dirs=[numpy.get_include()])

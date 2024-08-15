<img src="https://raw.githubusercontent.com/LeoMorales/isonymic-package/main/static/images/simple-image.jpg"><br>

--------------------------------------

isonymic: estructura demográfica a partir de apellidos
=======================================

El paquete `isonymic` contiene las funciones básicas para realizar estudios isonímicos a partir de los apellidos de las personas.

Permite calcular rápidamente indicadores isonímicos tales como el coeficiente de endogamia, alpha de Fisher, indicador A, indicador B, etc.

También permite obtener frecuencias de apellidos y generar gráficos log-log fácilmente.


Modo de uso
-------------

Debe pasar una Serie de pandas con los apellidos de la población:

    >>> import pandas
    >>> import isonymic

    >>> surnames = pandas.Series(["Gonzalez", "Gonzalez", "Gonzalez", "Gonzalez", "Gonzalez"])
    
    >>> print(isonymic.get_isonymy(surnames))

        1.0


Documentation
-------------

La documentación en línea se encuentra disponible en [Isonymic Package en Read the Docs](https://isonymic-package.readthedocs.io/en/latest/).


Dependencies
------------

Isonymic soporta Python 3.6+.

Su instalación requiere [numpy](https://numpy.org/), [pandas](https://pandas.pydata.org/), y [matplotlib](https://matplotlib.org/). Algunas funcionalidades avanzadas necesitan  [esda](https://pysal.org/esda/).

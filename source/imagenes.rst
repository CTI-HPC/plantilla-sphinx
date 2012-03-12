Ejemplo de uso de imágenes
==========================

Para agregar una imagen
como parte del repositorio,
basta con dejar la imagen en alguna parte
e incluirla a través de su ruta relativa.
Una opción es crear un directorio con imágenes,
pero también se puede usar el directorio ``_static``:

.. image:: _static/kitten.jpg
   :scale: 150
   :alt: Gato volador

Para agregar un diagrama hecho en TikZ,
hay que dejar un ``.tex`` en el directorio ``tikz``
siguiendo la estructura del ejemplo.
Al compilar el sitio
será creada la imagen con extensión ``.png``:

.. image:: tikz/circ.png


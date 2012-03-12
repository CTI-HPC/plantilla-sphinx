Ejemplos de ecuaciones
======================

Para escribir ecuaciones en el documento,
hay que activar en el archivo ``conf.py``
una de las dos extensiones que permiten incluir código LaTeX en Sphinx:

* ``pngmath`` (que incluye ecuaciones como imágenes PNG), o
* ``mathjax`` (que formatea dinámicamente las ecuaciones al cargar la página).

Las ecuaciones dentro del texto, como `\forall\theta\in\mathbb{R}\; {-1}\le\sin\theta\le 1`,
pueden ser escritas entre comillas simples invertidas.

(Esto funciona porque en ``conf.py`` se ha indicado que
el ``default_role`` es ``'math'``.)

Para incluir ecuaciones por sí solas,
hay que usar la directiva ``math``:

.. math::

    e^x = \frac{1  }{0!} +
          \frac{x  }{1!} +
          \frac{x^2}{2!} +
          \frac{x^3}{3!} +
          \cdots


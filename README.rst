Plantilla Sphinx para cursos del CTI-HPC
========================================

Cómo usar la plantilla
----------------------
Supongamos que queremos crear un repo llamado ``mi-curso`` basado en la plantilla,
y que alojaremos en el servidor del CTI-HPC. ::

    $ git clone -o ght https://github.com/CTI-HPC/plantilla-sphinx mi-curso
    $ cd mi-curso
    $ git checkout -b master
    $ git remote add origin git@git.hpc.cl/mi-curso.git
    $ git push origin master
    $ git push origin template

Configuración inicial
---------------------
Abra el archivo ``source/conf.py``
y modifíquelo de acuerdo a su proyecto
(como el nombre del proyecto y el autor).
Las variables más importantes están comentadas
para que sepa a qué se refieren.

Edite el archivo ``source/index.rst``
y modifique el nombre del proyecto y los instructores.

En el ``Makefile``,
modifique la variable ``DEPLOYDIR``
para indicar en qué servidor y en qué directorio
será publicado el apunte.

Preparación del apunte
----------------------
Para crear nuevas secciones,
debe crear un archivo con extensión ``.rst``,
y agregarlo al ``toctree`` que está en ``source/index.rst``.

Si lo desea, elimine del repositorio las secciones de ejemplo
(como ``imagenes`` y ``ecuaciones``).

Puede redactar secciones sin agregarlas al ``doctree``
(por ejemplo, material para clases futuras).
Estas secciones no aparecerán en el apunte.

Cómo crear el apunte
--------------------
Compilar sitio web::

    $ make

Abrir sitio web compilado en el navegador::

    $ make open

Copiar el sitio web al servidor indicado en el ``Makefile``::

    $ make deploy


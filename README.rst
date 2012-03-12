Plantilla Sphinx para cursos del CTI-HPC
========================================

Cómo usar la plantilla
----------------------
Supongamos que queremos crear un repo llamado ``mi-curso`` basado en la plantilla,
y que alojaremos en el servidor del CTI-HPC. ::

    $ git clone -o template https://github.com/rbonvall/plantilla-sphinx-cti-hpc mi-curso
    $ cd mi-curso
    $ git checkout -b master
    $ git remote add origin git@git.hpc.cl/mi-curso.git

Cómo crear el apunte
--------------------

Compilar sitio web::

    $ make

Abrir sitio web compilado en el navegador::

    $ make open

Copiar el sitio web al servidor::

    $ make deploy

Esto requiere haber asignado correctamente
la variable ``DEPLOYDIR`` en el Makefile.

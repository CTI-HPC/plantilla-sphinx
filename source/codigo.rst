Ejemplo de uso de código
========================

Se puede incluir código desde un archivo
usando la directiva ``literalinclude``:

.. literalinclude:: codigo/hola.c
   :language: c

A veces es útil que las líneas estén numeradas:

.. literalinclude:: codigo/hola.c
   :language: c
   :linenos:

Es buena idea tener el código en archivos externos,
pues de este modo se puede compilarlos y probarlos por separado.
Así uno se asegura de que todo el código incluido en el apunte
funciona correctamente.

También se puede incluir código directamente en el archivo ``.rst``
usando la notación de doble dos puntos::

    while (1) {
        printf("Hola %s\n", "mundo");
        break;
    }

En este caso,
el código será interpretado como el lenguaje indicado
en la variable ``highlight_language`` del archivo ``conf.py``.

Para incluir código indicando explícitamente el lenguaje,
se usa la directiva ``code-block``:

.. code-block:: fortran

    function contar_letras(s) result(frecs)
        character(len=*), intent(in) :: s
        character :: c
        integer, dimension(26) :: frecs
        integer :: i, ord

        frecs = 0
        do i = 1, len(s)
            c = s(i:i)
            if (es_letra(c)) then
                ord = orden(c)
                frecs(ord) = frecs(ord) + 1
            end if
        end do
    end function

También sirve para sesiones de consola:

.. code-block:: console

    $ mkdir proyecto
    $ ls
    proyecto
    $ cd proyecto
    $ pwd
    /tmp/proyecto



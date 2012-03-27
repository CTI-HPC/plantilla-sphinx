# Este es un Makefile "delegador",
# para poder hacer make desde el directorio source.
# Para configurar la construcción del sitio,
# modifique el Makefile que está en la raíz del proyecto.

.PHONY: all
all: html
%:
	@make -C .. $@


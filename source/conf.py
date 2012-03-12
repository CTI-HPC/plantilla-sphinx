# coding: utf-8
import sys, os
from os.path import abspath

#sys.path.insert(0, os.path.abspath('.'))
#sys.path.insert(0, os.path.abspath('_modules'))

# Dejar a lo más una de las extensiones para mostrar ecuaciones.
extensions = [
#  'sphinx.ext.pngmath',   # ecuaciones como imágenes
  'sphinx.ext.mathjax'    # ecuaciones como texto
]

# Cambiar a 'en' si el contenido está en inglés.
language = 'es'

# Poner el título del proyecto y el verdadero autor.
project = u'Plantilla Sphinx CTI-HPC'
author = u'Roberto Bonvallet'

# Incluir aquí cualquier archivo (o patrón de archivos)
# que deba ser ignorado por Sphinx.
exclude_patterns = []

# Lenguaje que se usará la mayor parte del tiempo
# para mostrar código.
highlight_language = 'c'

copyright = u'2012, ' + author
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
default_role = 'math'
pygments_style = 'sphinx'
version = ''
release = ''


# -- Options for HTML output --------------------------------------------------

html_theme = 'sphinxdoc'
html_theme_options = {
  'nosidebar': False,
}
#html_theme_path = []
#html_title = None
#html_short_title = None
html_logo = '_static/cti200.png'
#html_favicon = None
html_static_path = ['_static']
#html_last_updated_fmt = '%b %d, %Y'
#html_sidebars = {}
#html_additional_pages = {}
#html_domain_indices = True
#html_use_index = True
#html_split_index = False
#html_show_sourcelink = True
#html_show_sphinx = True
#html_show_copyright = True
#html_use_opensearch = ''
#html_file_suffix = None


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
 'papersize': 'letterpaper',
 'pointsize': '12pt',
 'preamble': '',
}

# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'plantilla.tex', project, author, 'manual'),
]

#latex_logo = None
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False
#latex_appendices = []
#latex_domain_indices = True


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = 'CTI-HPC'
epub_copyright = copyright


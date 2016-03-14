import sys, os

sys.path.append(os.path.abspath('_exts'))

extensions = [
    # 'matplotlib.sphinxext.mathmpl',
    # 'matplotlib.sphinxext.only_directives',
    # 'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.pngmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    # "sphinxcontrib.blockdiag",
    # "sphinxcontrib.seqdiag",
]


# 'ipython_console_highlighting',
# 'inheritance_diagram',
# 'numpydoc', 'lily',

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Linux und Open Source'
html_short_title = 'Linux und Open Source'
htmlhelp_basename = 'Linux und Open Source'
copyright = '2011-2016, Bernhard Grotz'
version = '0.2.3c'
release = '0.2.3c'
language = 'de'
spelling_lang = 'de_DE'
exclude_patterns = ["notes.rst", "*/notes.rst",
                    "**/notes.rst","todos.rst","README.rst"]
pygments_style = 'sphinx'
html_theme = 'sphinxdoc'
html_logo = "logo.png"
html_favicon = "favicon.ico"
html_static_path = ['_static']
html_last_updated_fmt = '%d.%b.%Y'
html_use_smartypants = True
html_additional_pages = {'home': 'home.html'}
html_domain_indices = False
html_use_index = True

html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = False
html_last_updated_fmt = '%d. %b %Y'
html_search_language = 'en'
html_search_options = {'type': 'default'}

trim_footnote_reference_space = True
#todo_include_todos = True



# latex_logo = "logo.png"

# latex_show_pagerefs = True

latex_preamble = r'''
\usepackage[version=3]{mhchem}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb}
\usepackage{nicefrac,marvosym,mathtools,wasysym}
\setcounter{secnumdepth}{-1}
\setlength{\headheight}{15pt}
\setcounter{tocdepth}{2}
\clubpenalty  = 10000 % Disable single lines at the start of a page ("Schusterjungen")
\widowpenalty = 10000 % Disable single lines at the end   of a page ("Hurenkinder")
\displaywidowpenalty = 10000
'''

pngmath_latex_preamble = latex_preamble
latex_elements = {
    "preamble": latex_preamble,
    "babel":        "\\usepackage[ngerman]{babel}",
    "classoptions": 'oneside,openany',
    "papersize": 'a4paper',
    "pointsize": '12pt',
    "fontpkg": '',
    "fncychap": ''
}

latex_domain_indices = False

latex_documents = [
   ('index', 'grundkurs-linux.tex', 'Grundkurs Linux',
   'Bernhard Grotz', 'manual'),
]

intersphinx_mapping = {
    'sphinx': ('http://sphinx-doc.org', None),
    'gw': ('http://grund-wissen.de', None),
    'gwe': ('http://grund-wissen.de/elektronik', None),
    'gwm': ('http://grund-wissen.de/mathematik', None),
    'gwp': ('http://grund-wissen.de/physik', None),
    'gwic': ('http://grund-wissen.de/informatik/c', None),
    'gwil': ('http://grund-wissen.de/informatik/latex', None),
    'gwip': ('http://grund-wissen.de/informatik/python', None),
}


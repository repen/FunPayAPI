# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys, os


sys.path.insert(0, os.path.abspath('../..'))


project = 'FunPayAPI'
copyright = '2023, Woopertail'
author = 'Woopertail'
release = '1.0.6'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.duration',
              'sphinx.ext.doctest',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.napoleon',
              'sphinx.ext.intersphinx', ]

autodoc_member_order = 'bysource'
intersphinx_mapping = {'python': ('https://docs.python.org/3.11', None)}

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "light_logo": "FunPayAPI.png",
    "dark_logo": "FunPayAPI_darkmode.png",
}

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'impactdb-api'
copyright = '2023, Garrett Roell, Haodong Ding'
author = 'Garrett Roell, Haodong Ding'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['nbsphinx', 'myst_nb']
source_suffix = ['.rst', '.ipynb', '.html', '.md']

templates_path = ['_templates']
exclude_patterns = ['_build', '**.ipynb_checkpoints']

autodoc_mock_imports = ['matplotlib']

language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

master_doc = 'index'
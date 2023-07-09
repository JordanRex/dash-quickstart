# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import sphinx_pdj_theme

project = 'dashquick'
copyright = '2023, Varun Rajan'
author = 'Varun Rajan'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',  # pip install sphinx_autodoc_typehints
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_pdj_theme'
html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'

html_theme_options = {
    'logo': 'logo.png',
    'github_user': 'Jordan Rex',
    'github_repo': 'later!',
    'github_button': True,
}

html_static_path = ['_static']

# Insert the project root dir as the first element in the PYTHONPATH.
# This lets Sphinx find the modules to be documented.
sys.path.insert(0, os.path.abspath('..'))

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

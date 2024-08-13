# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'isonymic'
copyright = '2024, Leo Morales, Pablo Navarro, Pablo Toledo, Virginia Ramallo y Claudio Delrieux'
author = 'Leo Morales, Pablo Navarro, Pablo Toledo, Virginia Ramallo y Claudio Delrieux'

import os
import sys
sys.path.insert(0, os.path.abspath('/home/lmorales/work/pipelines/package_surnames/isonymic_package/app/isonymic/src'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
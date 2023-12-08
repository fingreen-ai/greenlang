# pylint: skip-file
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "Fingreen AI Greenlang"
copyright = "2023, Fingreen AI"
author = "Fingreen AI"
release = "0.0.1"

import os
import sys

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("."))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.graphviz",
    "sphinx.ext.githubpages",
    "myst_parser",
]

templates_path = ["templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
suppress_warnings = ["myst.xref_missing", "myst.header"]
autodoc_mock_imports = ["django", "fingreen_web", "crispy_forms", ]

html_baseurl = "https://greenlang.fingreen.ai/"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "press"

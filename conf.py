# pylint: skip-file
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "Fingreen AI Greenlang"
copyright = "2024, Fingreen AI"
author = "Fingreen AI"
release = "0.0.2"

import os
import sys

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("."))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "myst_parser",
    "sphinxext.opengraph",
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
html_static_path = ["_static"]
html_logo = "_static/logo.svg"
html_css_files = ['custom.css',]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "press"

ogp_site_url = "https://greenlang.fingreen.ai/"
ogp_type = "website"
ogp_title = "Greenlang by Fingreen AI"
ogp_url = "https://greenlang.fingreen.ai/"
ogp_image = "https://fingreen.ai/static/web_landing/img/fingreen/about/greenlang_2.png"
ogp_description = "Greenlang is the first open-source component promoting transparency, interoperability, and collaboration in the ESG reporting domain."
ogp_enable_meta_description = True
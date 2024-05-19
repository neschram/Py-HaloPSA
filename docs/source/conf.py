# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath("../../"))
import halo_api

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project: str = "Py-HaloPSA"
copyright: str = "2024, Nathaniel Schram"
author: str = "Nathaniel Schram"
release: str = "0.0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions: list[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.coverage",
]

templates_path: list[str] = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme: str = "sphinx_rtd_theme"
html_static_path: list[str] = ["_static"]


# -- Napoleon Settings -------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html


napoleon_google_docstring: bool = True
napoleon_numpy_docstring: bool = True
napoleon_include_init_with_doc: bool = True
napoleon_include_private_with_doc: bool = False
napoleon_include_special_with_doc: bool = False
napoleon_use_admonition_for_examples: bool = False
napoleon_use_admonition_for_notes: bool = False
napoleon_use_admonition_for_references: bool = False
napoleon_use_ivar: bool = False
napoleon_use_param: bool = False
napoleon_use_rtype: bool = False
napoleon_preprocess_types: bool = True
napoleon_type_aliases: bool = None
napoleon_attr_annotations: bool = True


# -- Python Options
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-python-domain

python_display_short_literal_types = True
python_maximum_signature_line_length = 80

# -- autodoc Options
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autoclass_content = "both"
autodoc_inherit_docstrings = True

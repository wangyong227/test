# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import textwrap

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = "Holoscan Sensor Bridge Software"
copyright = "2022-2024, NVIDIA"
author = "NVIDIA"

# The full version, including alpha/beta/rc tags
with open("../../VERSION") as f:
    version_long = f.readline().strip()

release = version_long

title = "Holoscan Sensor Bridge User Guide"

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    #   'numpydoc',
    "sphinx.ext.autosectionlabel",  # https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html#automatically-label-sections
    "sphinx.ext.autodoc",  # needed for Python API docs (provides automodule)
    "sphinx.ext.autosummary",  # needed for Python API docs (provides autosummary)
    "sphinxcontrib.mermaid",  # https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/
    "sphinx_design",  # https://sphinx-design.readthedocs.io/en/latest/
]

# Make sure the target is unique
autosectionlabel_prefix_document = True
# Set the maximum depth of the section label
autosectionlabel_maxdepth = 5

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Enabling to be consistent with prior documentation
numfig = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# This option hides the "show source" link on each page.
# Leave it false otherwise internal documentation will show up in the source as well...
html_show_sourcelink = False
html_copy_source = False

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "collapse_navigation": False,
    "display_version": True,
    "navigation_depth": 5,
    "sticky_navigation": True,  # Set to False to disable the sticky nav while scrolling.
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_style = "css/isaac_custom.css"
html_logo = "_static/logo.png"
html_favicon = "_static/nvidia.ico"

# -- Options for Latex output --------------------------------------------------

latex_logo = "images/nvidia.png"

latex_engine = "pdflatex"

# with open("clara_preamble.tex", "r") as r:
#   clara_preamble_tex = r.read()

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    "papersize": "a4paper",
    # The font size ('10pt', '11pt' or '12pt').
    #
    "pointsize": "11pt",
    # Override default 'twoside' LaTex option so that even pages aren't blank
    "extraclassoptions": "openany,oneside",
    # Additional stuff for the LaTeX preamble.
    #
    #   'preamble': clara_preamble_tex,
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    "fncychap": "\\usepackage{fncychap}",
    #'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_file_name = f"{title.replace(' ', '_')}_{release}.tex"
latex_documents = [
    (master_doc, latex_file_name, title, "NVIDIA Corporation", "manual", True),
]

# Disable Index generation.
# It is not very helpful and fails to display properly with some of our terms
# being larger than a page width (e.g. C++ classes in nested namespaces.).
latex_elements = {
    "makeindex": "",
    "printindex": "",
    "maxlistdepth": "10",
}

latex_toplevel_sectioning = None

# -- Options for numpydoc ------------------------------------------------------

# https://numpydoc.readthedocs.io/en/latest/install.html#configuration
numpydoc_class_members_toctree = False
numpydoc_show_inherited_class_members = True
numpydoc_attributes_as_param_list = False

# -- Options for autodoc -------------------------------------------------------

autodoc_default_options = {
    # Make sure that any autodoc declarations show the right members
    "members": True,
    "inherited-members": True,
    "private-members": False,
    "show-inheritance": True,
}

# -- Options for autosummary ---------------------------------------------------

autosummary_generate = False

# -- Options for sphinx-mermaid ------------------------------------------------
#   Reference: https://github.com/mgaitan/sphinxcontrib-mermaid/issues/44
#              (we eventually use mmdc's PDF generation capability instead)

mermaid_version = "9.2.2"

# Use PDF diagram for latex PDF generation (with cropping the generated PDF)
if tags.has("noapi"):
    mermaid_cmd = "/usr/bin/mmdc"
    # 'docker/docs-builder/Dockerfile' creates 'puppeteer-config.json'
    mermaid_params = ["-p", "/usr/bin/puppeteer-config.json"]
    # pdfcrop is installed in the docker image (by 'texlive-extra-utils')
    mermaid_pdfcrop = "pdfcrop"
    mermaid_output_format = "pdf"

# -- Options for Sphinx --------------------------------------------------------

# Tell sphinx what the primary language being documented is.
primary_domain = "cpp"

# Tell sphinx what the pygments highlight language should be.
highlight_language = "cpp"

# -- Options for myst_parser

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    # "linkify",  # disable linkify to not confuse with the file name such as `app.py`
    "replacements",
    # "smartquotes",
    "substitution",
    "tasklist",
]
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-header-anchors
myst_heading_anchors = 5

numfig = True

# Configure Python API docs to include the __init__ methods


def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)

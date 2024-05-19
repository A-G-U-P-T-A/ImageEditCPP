# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars

html_theme_options = {
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'dark_mode': True,  # Enable the dark mode toggle
}

html_static_path = ['_static']
html_css_files = ['custom.css']
# Include all your settings here
html_theme = 'sphinx_rtd_theme'
"""Configuration for {{ cookiecutter.project_name }}."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '{{ cookiecutter.description }}',
    'author': '{{ cookiecutter.author }}',
    'url': '{{ cookiecutter.url }}',
    'download_url': '{{ cookiecutter.download_url }}',
    'author_email': '{{ cookiecutter.author_email }}',
    'version': '0.1.0',
    'install_requires': ['nose'],
    'packages': ['{{ cookiecutter.project_name }}'],
    'scripts': [],
    'name': '{{ cookiecutter.project_name }}'
}

setup(**config)

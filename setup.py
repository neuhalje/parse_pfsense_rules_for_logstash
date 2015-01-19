try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'Parse pfSense firewall rules',
    'author': 'Jens Neuhalfen',
    'url': 'TODO',
    'download_url': 'TODO',
    'author_email': 'TODO',
    'version': '0.1',
    'install_requires': ['unittest'],
    'packages': ['pfsense_parser'],
    'scripts': [],
    'name': 'pfsenseparser'
    }

setup(**config)

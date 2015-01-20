try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'Parse pfSense firewall rules. Supported: pfSense 2.1',
    'author': 'Jens Neuhalfen',
    'url': 'TODO',
    'download_url': 'TODO',
    'author_email': 'TODO',
    'version': '0.1',
    'install_requires': [],
    'packages': ['pfsense_parser', 'main'],
    'name': 'pfsenseparser',
    'license': 'BSD',
    'classifiers': [
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
                   ],
    'entry_points':{
             'console_scripts': [
                   'pfSense2Logstash=main.cli:main',
                                ],
             'gui_scripts': [ ]
                   }
    }

setup(**config)

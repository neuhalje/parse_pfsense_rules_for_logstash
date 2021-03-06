try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'Parse pfSense firewall rules. Supported: pfSense 2.1',
    'author': 'Jens Neuhalfen',
    'url': 'https://github.com:neuhalje/parse_pfsense_rules_for_logstash',
    'download_url': 'https://github.com/neuhalje/parse_pfsense_rules_for_logstash/zipball/master',
    'version': '0.1',
    'install_requires': ['argparse', 'nose'],
    'packages': ['pfsense_parser', 'cli'],
    'name': 'pfsenseparser',
    'license': 'BSD',
    'classifiers': [ "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License", ],
    'entry_points':{ 'console_scripts': [ 'pfSense2Logstash=cli.cli:main', ],
             'gui_scripts': [ ] }
    }

setup(**config)

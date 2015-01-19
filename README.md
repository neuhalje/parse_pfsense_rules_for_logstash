Parsing pfSense 2.1 rules for logstash
===========================================

This script parses the firewall rules from [pfSense](https://www.pfsense.org/) and emits them in a format suitable for [logstash PLUGIN](TODO).

Installing
------------
* local installation: `python setup.py  install`

Usage
---------

1) Export the rulesets on pfSense with `pfctl -vvvsr`. This can be done via SSH, or in the TODO part of the WebUI.
2) Run `pfSense2Logstash rules.txt > rule_id_to_tag.dict`
3) Include the file in the logstash PLUGIN rule

Example Result
----------------

```text
TODO
```

Example Logstash Config
-----------------------
```text
TODO
```

Development
=============

Test
-----
`nosetests`

Building the package
----------------------
* local installation: `python setup.py  install`
* Build .egg: `python setup.py  bdist`

License
========

BSD 3-Clause

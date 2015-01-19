Parsing pfSense 2.1 rules for logstash
===========================================

This script parses the firewall rules from [pfSense](TODO) and emits them in a format suitable for [logstash PLUGIN](TODO).

Installing
------------
TODO

Usage
---------

1) Export the rulesets on pfSense with `pfctl -vvvsr`. This can be done via SSH, or in the TODO part of the WebUI.
2) Run `pfSense2Logstash rules.txt > rule_id_to_tag.dict`
3) Include the file in the logstash PLUGIN rule
```json
TODO
```

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
TODO

License
========

TODO

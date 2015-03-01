Parsing pfSense 2.1 rules for logstash
===========================================

This script parses the firewall rules from [pfSense](https://www.pfsense.org/) and emits them in a format suitable for [logstash translate plugin](http://logstash.net/docs/1.4.2/filters/translate).

Installing
------------
* From GitHub: `pip install https://github.com/neuhalje/parse_pfsense_rules_for_logstash/zipball/master`
* local installation: `python setup.py  install`
* directly call `./pfSense2Logstash`

Usage
---------

1. Export the rulesets on pfSense with `pfctl -vvvsr`. This can be done via SSH, or in the "Diagnostics/Command Prompt" part of the WebUI.
2. Run `pfSense2Logstash rules.txt > rule_id_to_tag.dict`
3. Include the file in the logstash PLUGIN rule

Example Result
----------------

### Input file

```text
@0 scrub on vr2 all fragment reassemble
 [ Evaluations: 12882073  Packets: 5093291   Bytes: 1673472449  States: 0     ]
 [ Inserted: uid 0 pid 51319 ]
@0 anchor "relayd/*" all
 [ Evaluations: 120503    Packets: 0         Bytes: 0           States: 0     ]
 [ Inserted: uid 0 pid 51319 ]
@1 anchor "openvpn/*" all
 [ Evaluations: 120503    Packets: 0         Bytes: 0           States: 0     ]
 [ Inserted: uid 0 pid 51319 ]
@3 block drop in log quick inet6 all label "Block all IPv6"
 [ Evaluations: 120503    Packets: 1170      Bytes: 84240       States: 0     ]
 [ Inserted: uid 0 pid 51319 ]
@120 block return in quick on vr1 all label "USER_RULE"
 [ Evaluations: 29        Packets: 29        Bytes: 1273        States: 0     ]
 [ Inserted: uid 0 pid 51319 ]
@121 anchor "tftp-proxy/*" all
 [ Evaluations: 27765     Packets: 0         Bytes: 0           States: 0     ]
 [ Inserted: uid 0 pid 51319 ]
```

### Output

```text
'0':'"relayd/*" all'
'1':'"openvpn/*" all'
'3':'Block all IPv6drop in log quick inet6 all'
'120':'USER_RULEreturn in quick on vr1 all'
'121':'"tftp-proxy/*" all'
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

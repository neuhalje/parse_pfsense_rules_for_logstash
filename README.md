Parsing pfSense 2.1 rules for logstash
===========================================

This script parses the firewall rules from [pfSense](https://www.pfsense.org/) and emits them in a format suitable for [logstash translate plugin](http://logstash.net/docs/1.4.2/filters/translate).

Installing
------------
* From GitHub: `pip install https://github.com/neuhalje/parse_pfsense_rules_for_logstash/zipball/master`
* local installation: `python setup.py  install`

Usage
---------

1. Export the rulesets on pfSense with `pfctl -vvvsr`. This can be done via SSH, or in the "Diagnostics/Command Prompt" part of the WebUI.
2. Run `pfSense2Logstash rules.txt > rule_id_to_tag.dict`
3. Include the file in the logstash PLUGIN rule

Example Result
----------------

```text
...
"0": "relayd/*" all (anchor)
"1": "openvpn/*" all (anchor)
"2": "ipsec/*" all (anchor)
"3": Block all IPv6 (block)
"4": Block all IPv6 (block)
"5": Default deny rule IPv4 (block)
"6": Default deny rule IPv4 (block)
"7": Default deny rule IPv6 (block)
"8": Default deny rule IPv6 (block)
...
"84": on vr2 proto tcp from any to any port 5899 >< 5931 flags S/SA label "USER_RULE: m_Other VNC outbound" queue (qOthersHigh, qACK) (match)
...
"110": USER_RULE: dmz: allow outbound smtp from mail (pass)
"111": USER_RULE: dmz: allow outbound git (pass)
"112": USER_RULE: dmz: allow outbound https (pass)
"113": USER_RULE: dmz: allow outbound http (pass)
...
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

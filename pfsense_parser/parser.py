import re

class Parser(object):
    def parse(self, input):
        self.result = []

        if isinstance(input, basestring):
            self._parse_line(input)
        else:
            for line in input:
                self._parse_line(line)

        return self.result

    def _parse_line(self, line):
        #@0 scrub on vr2 all fragment reassemble
        #@8 block drop out log inet6 all label "Default deny rule IPv6"
        match = re.match('^@(\d+)\s+(\w+)\s+(.*?)(?:\s+label\s+"(.+)")?$', line)
        if match:
            id = int(match.group(1))
            type = match.group(2)
            msg = match.group(3)
            label =  match.group(4)

            rule = {"id": id, "type": type, "msg": msg }
            if label:
                rule['label'] = label

            self.result.append(rule)

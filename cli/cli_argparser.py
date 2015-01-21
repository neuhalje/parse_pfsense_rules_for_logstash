import argparse


def comma_separated(v):
    import re
    try:
        return re.match("^\w+(?:,\w+)*$", v).group(0)
    except:
        raise ArgumentTypeError("%s' needs to be  a list type1[,type2]*"%(v,))
    return v

class CliArgParser(object):
    def __init__(self, argv):
        self.argv = argv
        self.has_parse_error = True
        self.script_name = None
        self.data_file = None
        self.format_string = None
        self.filter_for_types = None

    def parse(self):
        self.script_name = self.argv.pop(0)
        parser = argparse.ArgumentParser(prog=self.script_name, description = 'pfSense firewall rule parser')

        parser.add_argument("--filter", 
                            help="Only export the mentioned types (e.g. block or anchor,block,pass). Comma separated", 
                            type=comma_separated, 
                            nargs=1,
                            dest='filter_for_types',
                            default="anchor,block,pass")

        parser.add_argument("--format", 
                            help="Format string for pythons '%' operator with a dictionary. Allowed fileds: id,type,label,msg", 
                            nargs=1,
                            dest='format_string',
                            default="'%(id)i':'%(label)s%(msg)s'")

        parser.add_argument("data_file", help="An export of pfctl -vvvsr")

        try:
            args = parser.parse_args(self.argv)

            self.data_file = args.data_file
            self.format_string = _strip_list(args.format_string)
            self.filter_for_types = _strip_list(args.filter_for_types).split(",")

            self.has_parse_error = False
        except SystemExit as se:
            # argparse is rather fast at System.exiting ..
            self.has_parse_error = True
            #print(se)
        except Exception as e:
            self.has_parse_error = True
            #print(e)

def _strip_list(v):
            if isinstance(v, basestring):
                return v
            else:
                return v[0]

def from_argv(argv):
    ret = CliArgParser(argv)
    ret.parse()
    return ret

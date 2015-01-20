#!/usr/bin/env python

import sys
import cli_argparser
import pfsense_parser

def main():
    args = cli_argparser.from_argv(sys.argv)
    if args.has_parse_error:
        # print "Usage: script /path/to/inputfile"
        return

    parser = pfsense_parser.Parser()

    data_file = args.data_file

    with open(data_file) as f:
        items = parser.parse(f.readlines())
        for item in items:
            if item:
                id = item['id'] 
                type = item['type'] 

                if item.has_key('label'):
                    columns = (id, item['label'], type )
                else:
                    columns = (id, item['msg'], type )

                if type in args.filter_for_types:
                    print('"{0}": {1} ({2})'.format(*columns))

if __name__ == '__main__':
    main()


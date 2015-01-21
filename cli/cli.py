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
    format_string = args.format_string

    with open(data_file) as f:
        items = parser.parse(f.readlines())
        for item in items:
            if item:
                if item['type'] in args.filter_for_types:
                    if not 'label' in item:
                        item['label'] = '' # item['msg']

                    print(format_string % item)

if __name__ == '__main__':
    main()


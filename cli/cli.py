#!/usr/bin/env python

import sys
import cli_argparser
import pfsense_parser


def parser(version):
    if version == "2.1":
        return pfsense_parser.Parser21()
    elif version == "2.2":
        parser = pfsense_parser.Parser22()
    else:
        # Should have been handled in the arg parser
        return None



def main():
    args = cli_argparser.from_argv(sys.argv)
    if args.has_parse_error:
        return


    data_file = args.data_file
    format_string = args.format_string
    pfsense_version = args.pfsense_version

    parser = parser(pfsense_version)

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


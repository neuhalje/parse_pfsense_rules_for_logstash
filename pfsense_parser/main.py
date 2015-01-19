#!/usr/bin/env python

import sys
import pfsense_parser

def main():
    if len(sys.argv) != 2:
        print "Usage: script /path/to/inputfile"
        return

    fname = sys.argv[1]

    parser = pfsense_parser.Parser()

    with open(fname) as f:
        items = parser.parse(f.readlines())
        for item in items:
            if item:
                id = item['id'] 
                type = item['type'] 

                if item.has_key('label'):
                    columns = (id, item['label'] )
                else:
                    columns = (id, item['msg'])

                if type == 'block':
                    print("%s:%s" % columns)

if __name__ == '__main__':
    main()

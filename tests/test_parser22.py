import unittest
import pfsense_parser

class ParserTest(unittest.TestCase):

    def create_sut(self):
        return pfsense_parser.Parser22()

    def test_empty_string__parses_to__empty_list(self):
        sut = self.create_sut()
        self.assertEquals([], sut.parse(""))

    def test_empty_lines__parses_to__empty_list(self):
        sut = self.create_sut()
        self.assertEquals([], sut.parse("\n\n\n"))

    def test_empty_lines_as_list__parses_to__empty_list(self):
        sut = self.create_sut()
        self.assertEquals([], sut.parse(["\n","\n"]))

    def test_garbage_string__parses_to__empty_list(self):
        sut = self.create_sut()
        self.assertEquals([], sut.parse(" [ Evaluations: 7788788   Packets: 6477312   Bytes: 1941991782  States: 0     ]"))

    def test_parse_string__parses_to__list_with_parsed_entry(self):
        sut = self.create_sut()
        self.assertEquals([{"id":0, "type": "scrub", "msg":"on vr2 all fragment reassemble"}], sut.parse("@0(0) scrub on vr2 all fragment reassemble"))

    def test_two_calls__parses_to__one_result(self):
        sut = self.create_sut()
        sut.parse(["@2(0) scrub on vr1 all fragment reassemble"])
        self.assertEquals([{"id":2, "type": "scrub", "msg":"on vr1 all fragment reassemble"}], sut.parse(["@2(0) scrub on vr1 all fragment reassemble"]))

    def test_line_with_tag__parses_to__list_with_parsed_entry_with_tag(self):
        sut = self.create_sut()
        self.assertEquals([{"id":11, "type": "block", "msg":"drop in log inet6 all", "label": "Default deny rule IPv6"}], sut.parse(['@11(1000105595) block drop in log inet6 all label "Default deny rule IPv6"']))

if __name__ == '__main__':
    unittest.main()


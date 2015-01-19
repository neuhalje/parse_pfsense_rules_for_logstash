import unittest
import pfsense_parser

class ParserTest(unittest.TestCase):

    def create_sut(self):
        #return pfsense_parser.parser.Parser()
        return pfsense_parser.Parser()

    def test_empty_string__parses_to__empty_list(self):
        sut = self.create_sut()
        self.assertEquals([], sut.parse(""))

    def test_empty_lines__parses_to__empty_list(self):
        sut = self.create_sut()
        self.assertEquals([], sut.parse("\n\n\n"))


if __name__ == '__main__':
    unittest.main()


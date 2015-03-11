import unittest
import cli
from cli import cli_argparser

class CliArgParser_Test(unittest.TestCase):

    def create_sut(self, argv):
        return cli.from_argv(argv)

    def test_version_string_recognizes_2_1(self):
        self.assertEquals(cli_argparser.version_string("2.1"),"2.1")

    def test_version_string_recognizes_2_2(self):
        self.assertEquals(cli_argparser.version_string("2.2"),"2.2")

    def test_version_string_rejects_2_3(self):
        try:
            cli_argparser.version_string("2.3")
            self.assertTrue(false)
        except Exception:
            pass

    def test_version_string_rejects_empty_version(self):
        try:
            cli_argparser.version_string("")
            self.assertTrue(false)
        except Exception:
            pass


    def test_no_args__parses_to__error(self):
        sut = self.create_sut(["/script/name"])
        self.assertTrue(sut.has_parse_error)
    
    def test_no_args__parses_script_name(self):
        sut = self.create_sut(["/script/name"])
        self.assertEquals("/script/name", sut.script_name)

    def test_data_file_arg__parses(self):
        sut = self.create_sut(["/script/name", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals("datafile", sut.data_file)

    def test_data_file_with_spaces_arg__parses(self):
        sut = self.create_sut(["/script/name", "datafile with spaces"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals("datafile with spaces", sut.data_file)

    def test_two_data_files_arg__parses_to_error(self):
        sut = self.create_sut(["/script/name", "datafile", "datafile2"])
        self.assertTrue(sut.has_parse_error)

    def test_filter_for_types_default_arg__is_correct(self):
        sut = self.create_sut(["/script/name", "datafile"])
        self.assertEquals(sut.filter_for_types,["anchor","block","pass"])

    def test_filter_for_types_three__is_correct(self):
        sut = self.create_sut(["/script/name", "--filter=anchor,block,pass", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.filter_for_types,["anchor","block","pass"])

    def test_filter_for_types_two__is_correct(self):
        sut = self.create_sut(["/script/name", "--filter=anchor,pass", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.filter_for_types,["anchor","pass"])

    def test_filter_for_types_one__is_correct(self):
        sut = self.create_sut(["/script/name", "--filter=block", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.filter_for_types, ["block"])

    def test_default_format__is_present(self):
        sut = self.create_sut(["/script/name", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.format_string, "'%(id)i':'%(label)s%(msg)s'")

    def test_format__is_parsed(self):
        sut = self.create_sut(["/script/name", "--format='%(id)i':'%(label)s%(msg)s'", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.format_string, "'%(id)i':'%(label)s%(msg)s'")

    def test_format__is_parsed2(self):
        sut = self.create_sut(["/script/name", "--format=xxx", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.format_string, "xxx")
    
    def test_good_pfsenseversion__is_parsed(self):
        sut = self.create_sut(["/script/name", "--pfsense-version=2.1", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.pfsense_version, "2.1")
    
    def test_unknown_pfsenseversion__fails(self):
        sut = self.create_sut(["/script/name", "--pfsense-version=2.3", "datafile"])
        self.assertTrue(sut.has_parse_error)
    
    def test_empty_pfsenseversion__fails(self):
        sut = self.create_sut(["/script/name", "--pfsense-version=", "datafile"])
        self.assertTrue(sut.has_parse_error)

if __name__ == '__main__':
    unittest.main()

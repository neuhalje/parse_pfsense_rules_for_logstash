import unittest
import cli

class CliArgParser_Test(unittest.TestCase):

    def create_sut(self, argv):
        return cli.from_argv(argv)

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
        sut = self.create_sut(["/script/name", "--filter-for-types=anchor,block,pass", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.filter_for_types,["anchor","block","pass"])

    def test_filter_for_types_two__is_correct(self):
        sut = self.create_sut(["/script/name", "--filter-for-types=anchor,pass", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.filter_for_types,["anchor","pass"])

    def test_filter_for_types_one__is_correct(self):
        sut = self.create_sut(["/script/name", "--filter-for-types=block", "datafile"])
        self.assertFalse(sut.has_parse_error)
        self.assertEquals(sut.filter_for_types, ["block"])

if __name__ == '__main__':
    unittest.main()

import os
import unittest


def analyze_text(filename):
    """
    Calculate the number of lines and characters in a file

    Args:
        filename: The file to be analyzed

    Raises:
        IOError: If 'file' does not exist or can't be read
    """
    line_count = 0
    char_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
            char_count += len(line)
    return line_count,char_count


class TextAnalysisTests(unittest.TestCase):
    """
    Tests for the analyze_text() method
    """
    def setUp(self):
        """
        Fixture that creates a file for the test methods to use
        """
        self.file = "text.txt"
        with open(self.file,'w') as file:
            file.write("Now we are engaged in a great civil war.\n"
                       "Now we are engaged in a great civil war.\n"
                       "Now we are engaged in a great civil war.\n"
                       "Now we are engaged in a great civil war.")

    def tearDown(self):
        """
        Fixture that deletes the file created for use by test methods
        """
        try:
            os.remove(self.file)
        except:
            pass

    def test_function_runs(self):
        """
        Basic smoke test : Does the analyze_text() method run?
        """
        analyze_text(self.file)

    def test_line_count(self):
        """
        Check if the line count is as expected in the file
        """
        self.assertEqual(analyze_text(self.file)[0], 4)

    def test_character_count(self):
        """
        Check if the number of characters is as expected in the file
        """
        self.assertEqual(analyze_text(self.file)[1], 163)

    def test_no_such_file(self):
        """
        Check if analyze_text() fails with invalid filename
        """
        with self. assertRaises(IOError):
            analyze_text("foobar")

    def test_no_deletion(self):
        """
        Check if analyze_text() deletes the file
        """
        analyze_text(self.file)
        self.assertTrue(os.path.exists(self.file))


if __name__ == '__main__':
    unittest.main()
import unittest
import tempfile as t
import os
import pandas as pan
from app.io.input import input_from_file, input_from_file_pandas

class test_input(unittest.TestCase):
    def test_input_from_file_valid_file(self):
        """
        Tests reading from a valid text file.

        Checks whether the `input_from_file` function correctly reads and returns
        the contents of a non-empty text file.

        Raises:
            AssertionError: If the file content is not read correctly.
        """
        with t.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write("Tralala\nSecond tralala.")
            temp_file_path = temp_file.name

        result = input_from_file(temp_file_path)
        expected = "Tralala\nSecond tralala."
        self.assertEqual(result, expected)

        os.remove(temp_file_path)

    def test_input_from_file_file_not_found(self):
        """
        Tests behavior when the file does not exist.

        Ensures that `input_from_file` raises a FileNotFoundError when trying to
        read a non-existent file.

        Raises:
            FileNotFoundError: If the file is not found.
        """
        with self.assertRaises(FileNotFoundError):
            input_from_file("asjfahdsgl.txt")

    def test_input_from_file_empty_file(self):
        """
        Tests reading from an empty file.

        Verifies that `input_from_file` returns an empty string when reading
        a file with no content.

        Raises:
            AssertionError: If the returned value is not an empty string.
        """
        with t.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file_path = temp_file.name

        res = input_from_file(temp_file_path)
        expected = ""
        self.assertEqual(res, expected)

        os.remove(temp_file_path)

    def test_input_from_file_pandas_valid_file(self):
        """
        Tests reading tabular data using pandas.

        Checks whether the `input_from_file_pandas` function correctly reads a
        tab-separated file and returns it as a string.

        Raises:
            AssertionError: If the returned string does not match expected format.
        """
        with t.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
            temp_file.write("Alina\t2\tJournalism\nVova\t2\tIPZ")
            temp_file_path = temp_file.name

        res = input_from_file_pandas(temp_file_path)
        expected = "Alina  2  Journalism\nVova    2  IPZ"
        self.assertEqual(res.strip(), expected)

        os.remove(temp_file_path)

    def test_input_from_file_pandas_file_not_found(self):
        """
        Tests behavior when reading a non-existent file using pandas.

        Ensures that `input_from_file_pandas` raises a FileNotFoundError
        if the file does not exist.

        Raises:
            FileNotFoundError: If the file is not found.
        """
        with self.assertRaises(FileNotFoundError):
            input_from_file_pandas("ahghlsdgpua.txt")

    def test_input_from_file_pandas_empty_file(self):
        """
        Tests reading an empty file using pandas.

        Ensures that `input_from_file_pandas` raises a pandas.errors.EmptyDataError
        when the input file is empty.

        Raises:
            pandas.errors.EmptyDataError: If the file contains no data.
        """
        with t.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file_path = temp_file.name

        with self.assertRaises(pan.errors.EmptyDataError):
            input_from_file_pandas(temp_file_path)

        os.remove(temp_file_path)

if __name__ == '__main__':
    unittest.main()
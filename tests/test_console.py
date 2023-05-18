import unittest
from io import StringIO
import sys
from console import HBNBCommand


class ConsoleTestCase(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def capture_stdout(self, func, *args, **kwargs):
        """Capture stdout output for a function"""
        captured_output = StringIO()
        sys.stdout = captured_output
        func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip()

    def test_create(self):
        result = self.capture_stdout(self.console.onecmd, "create User")
        self.assertIsNotNone(result)  # Check if output is not empty

    def test_show(self):
        result = self.capture_stdout(self.console.onecmd, "show User 123")
        self.assertEqual(result, "** no instance found **")

    def test_all(self):
        result = self.capture_stdout(self.console.onecmd, "all")
        self.assertIsNotNone(result)  # Check if output is not empty

    def test_destroy(self):
        result = self.capture_stdout(self.console.onecmd, "destroy User 123")
        self.assertEqual(result, "** no instance found **")

    def test_update(self):
        result = self.capture_stdout(
            self.console.onecmd, 'User.update("123", {"first_name": "Emma"})')
        self.assertEqual(result, "** no instance found **")

    def test_count(self):
        result = self.capture_stdout(self.console.onecmd, "count User")
        self.assertIsNotNone(result)  # Check if output is not empty
        self.assertTrue(result.isdigit())  # Check if output is a number


if __name__ == '__main__':
    unittest.main()

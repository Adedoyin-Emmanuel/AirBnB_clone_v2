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

    def test_create_missing_class(self):
        result = self.capture_stdout(self.console.onecmd, "create")
        self.assertEqual(result, "** class name missing **")

    def test_create_invalid_class(self):
        result = self.capture_stdout(
            self.console.onecmd, "create InvalidClass")
        self.assertEqual(result, "** class doesn't exist **")

    def test_create_valid_class(self):
        result = self.capture_stdout(self.console.onecmd, "create User")
        self.assertIsNotNone(result)  # Check if output is not empty

    def test_show_missing_class(self):
        result = self.capture_stdout(self.console.onecmd, "show")
        self.assertEqual(result, "** class name missing **")

    def test_show_missing_id(self):
        result = self.capture_stdout(self.console.onecmd, "show User")
        self.assertEqual(result, "** instance id missing **")

    def test_show_invalid_id(self):
        result = self.capture_stdout(self.console.onecmd, "show User 123")
        self.assertEqual(result, "** no instance found **")

    def test_all_invalid_class(self):
        result = self.capture_stdout(self.console.onecmd, "all InvalidClass")
        self.assertEqual(result, "** class doesn't exist **")

    def test_all_valid_class(self):
        result = self.capture_stdout(self.console.onecmd, "all User")
        self.assertIsNotNone(result)  # Check if output is not empty

    def test_destroy_missing_class(self):
        result = self.capture_stdout(self.console.onecmd, "destroy")
        self.assertEqual(result, "** class name missing **")

    def test_destroy_missing_id(self):
        result = self.capture_stdout(self.console.onecmd, "destroy User")
        self.assertEqual(result, "** instance id missing **")

    def test_destroy_invalid_id(self):
        result = self.capture_stdout(self.console.onecmd, "destroy User 123")
        self.assertEqual(result, "** no instance found **")

    def test_update_missing_class(self):
        result = self.capture_stdout(self.console.onecmd, "update")
        self.assertEqual(result, "** class name missing **")

    def test_update_missing_id(self):
        result = self.capture_stdout(self.console.onecmd, "update User")
        self.assertEqual(result, "** instance id missing **")

    def test_update_missing_dictionary(self):
        result = self.capture_stdout(self.console.onecmd, 'User.update("123")')
        self.assertEqual(result, "** no instance found **")

    def test_update_invalid_id(self):
        result = self.capture_stdout(
            self.console.onecmd, 'User.update("123", {"first_name": "Emma"})')
        self.assertEqual(result, "** no instance found **")

    def test_update_invalid_dictionary(self):
        result = self.capture_stdout(
            self.console.onecmd, 'User.update("123", "invalid")')
        self.assertEqual(result, "** no instance found **")

    def test_update_valid_dictionary(self):
        result = self.capture_stdout(
            self.console.onecmd, 'User.update("5610c8e7-f06f-48e7-afae-a02adc959787", {"first_name": "Emma"})')
        self.assertEqual(result, "Instance updated successfully.")

    def test_update_missing_attribute_value(self):
        result = self

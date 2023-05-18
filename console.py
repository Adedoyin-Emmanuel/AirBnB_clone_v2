#!/usr/bin/python3
"""Entry point for command line interpreter."""
import cmd
from shlex import split
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review

all_classes = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Review"
    "Amenity"
]


def parse_args_with_brackets(args, brackets):
    """This function parses the arguments with brackets"""
    opening_bracket_index = brackets.span()[0]
    args_before_brackets = args[:opening_bracket_index]

    # Splitting the string using a comma as the delimiter
    lexer = args_before_brackets.split(",")
    cleaned_lexer = [element.strip() for element in lexer]
    cleaned_lexer.append(brackets.group())

    return cleaned_lexer


def parse(args):
    """Base console parsing function"""
    brackets = re.search(r"\[(.*?)\]", args)
    curly_brackets = re.search(r"\{(.*?)\}", args)
    if curly_brackets is None:
        if brackets is None:
            return [i.strip() for i in split(args)]
        else:
            parse_args_with_brackets(args, brackets)
    else:
        parse_args_with_brackets(args, curly_brackets)


def check_args(args):
    """
    Checks if args is valid
    args(string)

    Returns error is args is None or invalid class
    else returns the arguments
    """
    argument_list = parse(args)

    if (len(argument_list) == 0):
        print("** class name missing **")
    elif argument_list[0] not in all_classes:
        print("** class doesn't exist **")
    else:
        return argument_list


class HBNBCommand(cmd.Cmd):
    """Base class for AirBnB Console
    """
    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def default(self, arg):
        """Default behaviour for cmd module when input is invalid"""
        action_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        match = re.search(r"\.", arg)
        if match:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in action_map:
                    call = "{} {}".format(arg1[0], command[1])
                    return action_map[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, argv):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_quit(self, argv):
        """When executed, exits the console."""
        return True

    def do_create(self, argv):
        """Creates a new instance of BaseModel, saves it (to a JSON file)
        and prints the id"""
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """Prints the string representation of an instance based
        on the class name and id"""
        args = check_args(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def do_all(self, argv):
        """Prints all string representation of all instances based or not
        based on the class name"""
        arg_list = split(argv)
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in all_classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_destroy(self, argv):
        """Delete a class instance based on the name and given id."""
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, argv):
        """Updates an instance based on the class name and id by adding or
        updating attribute and save it to the JSON file."""
        arg_list = check_args(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")

            self.storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        arg1 = parse(arg)
        count = 0
        try:
            for obj in models.storage.all().values():
                if arg1[0] == type(obj).__name__:
                    count += 1
        except IndexError:
            pass
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

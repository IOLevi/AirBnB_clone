#!/usr/bin/python3
'Console module'

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    "Console class"

    # expand this list when you add new classes
    myclasses = ["BaseModel", "User", "Place",
                 "State", "City", "Amenity", "Review"]

    def emptyline(self):
        'empty lines will not repeat last command'
        pass

    def do_quit(self, s):
        "quit method"
        return True

    def help_quit(self):
        "help quit"
        print("Exit the interpreter.")
        print("You can also use CTRL-D (EOF) to exit")

    def do_create(self, s):
        "create a class"
        #classes = ["BaseModel"]
        #l = s.split()

        if len(s) < 1:  # should i make it !=
            print("** class name missing **")
            return False

        if s not in self.myclasses:
            print("** class doesn't exist **")
            return False

        created = eval("{}()".format(s))  # changed this
        created.save()
        print(created.id)

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id")

    def do_show(self, s):
        if len(s) < 1:
            print("** class name missing **")
            return False

        cname = s.split()[0]
        if cname not in self.myclasses:
            print("** class doesn't exist **")
            return False

        try:
            cid = s.split()[1]
        except BaseException:
            print("** instance id missing **")
            return False

        bucket = storage.all()  # a dictionary which includes every obj in storage
        for k in bucket:
            if k == "{}.{}".format(cname, cid):
                print(bucket[k])
                return False
        print("** no instance found **")

    def help_show(self):
        "help for show"
        print("Prints the string representation of an instance based on the class name and id.")

    def do_destroy(self, s):
        "destroy method"

        if len(s) < 1:
            print("** class name missing **")
            return False

        cname = s.split()[0]
        if cname not in self.myclasses:
            print("** class doesn't exist **")
            return False

        try:
            cid = s.split()[1]
        except BaseException:
            print("** instance id missing **")
            return False

        bucket = storage.all()  # __objects from the FileStorage

        for k in bucket:
            if k == "{}.{}".format(cname, cid):
                bucket.pop(k)  # removes it from __objects in storage
                storage.save()  # rewrites the json file
                return False
        print("** no instance found **")

    def help_destroy(self):
        "help for destroy"
        print("destroys an object by overwriting it from the json file")

    def do_all(self, s):
        """prints all objects"""
        if s and s not in self.myclasses:
            print("** class doesn't exist **")
            return False

        bucket = storage.all()
        if s:  # if they specified a classname
            for k in bucket:
                if k.startswith(s):
                    print(bucket[k])
            return False

        for i in self.myclasses:  # if no classname were specified, use everything in my self.myclasses class list
            for k in bucket:
                if k.startswith(i):
                    print(bucket[k])
        return False

    def help_all(self):
        "help for all"
        print("all [<class name>] -> prints all instances of every class if no argument is specified; otherwise all the instances of specified class")

    def do_update(self, s):
        "update an attribute in an existing obj"
        if len(s) < 1:
            print("** class name missing **")
            return False

        cname = s.split()[0]
        if cname not in self.myclasses:
            print("** class doesn't exist **")
            return False

        try:
            cid = s.split()[1]
        except BaseException:
            print("** instance id missing **")
            return False

        try:
            cattrname = s.split()[2]
        except BaseException:
            print("** attribute name missing **")
            return False

        try:
            cattrvalue = s.split()[3]
        except BaseException:
            print("** value missing **")
            return False

        bucket = storage.all()

        # need to cast attribute name to attribute value
        try:
            target = bucket["{}.{}".format(cname, cid)]
        except KeyError:
            print("** no instance found **")
            return False
        # could just check if "." in cattrvalue and if so cast float else cast
        # int if alphanumeric else pass as string

        try:
            setattr(target, cattrname, float(cattrvalue) if not cattrvalue.isdecimal() else int(
                cattrvalue))  # how to dynamically know the value of an atttribute...then cast... type it?
            storage.save()
        # wrote it this way if the float("alphastring" fails)
        except ValueError:
            setattr(target, cattrname, cattrvalue)
            storage.save()

    def help_update(self):
        "help for update"
        print("update <classname> <classid> <attrname> <attrvalue: (int, float, str)>")
        # isdecimal doesn't return true for float numbers

        # ENOTE: need to test for a "update BModel 343243 cattrname "a spaced
        # value"""

    do_EOF = do_quit
    help_EOF = help_quit
    prompt = "(hbnb) "


if __name__ == "__main__":
    interpreter = HBNBCommand()
    interpreter.cmdloop()

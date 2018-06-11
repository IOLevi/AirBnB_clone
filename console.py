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

    def emptyline(self):
        'empty lines will not repeat last command'
        pass

    def do_exit(self, s):
        return True

    def help_exit(self):
        print("Exit the interpreter.")
        print("You can also use CTRL-D (EOF) to exit")

    def do_create(self, s):
        #classes = ["BaseModel"]
        #l = s.split()
        
        if len(s) < 1: #should i make it !=
            print("** class name missing **")
            return False

        if s not in self.myclasses:
            print("** class doesn't exist **")
            return False
        
        created = eval("{}()".format(s)) #changed this
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

        bucket = storage.all()
        for k in bucket:
            if k == "{}.{}".format(cname, cid):
                print(bucket[k])
                return False
        print("** no instance found **")
    
    def help_show(self):
        print("Prints the string representation of an instance based on the class name and id.")

    def do_destroy(self, s):
        """If the class name is missing, print ** class name missing ** (ex: $ destroy)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
        If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ destroy BaseModel 121212)"""
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
        
        bucket = storage.all()

        for k in bucket:
            if k == "{}.{}".format(cname, cid):
                bucket.pop(k)
                storage.save()
                return False
        print("** no instance found **")

    def help_destroy(self):
        print("destroys an object by overwriting it from the json file")

    def do_all(self, s):
        """prints all objects"""
        if s and s not in self.myclasses:
            print("** class doesn't exist **")
            return False
        
        bucket = storage.all()
        if s: #if they specified a classname
            for k in bucket:
                if k.startswith(s):
                    print(bucket[k])
            return False
        
        for i in self.myclasses:#if no classname were specified, use everything in my self.myclasses class list
            for k in bucket:
                if k.startswith(i):
                    print(bucket[k])
        return False
    
    def help_all(self):
        print("all [<class name>] -> prints all instances of every class if no argument is specified; otherwise all the instances of specified class")
    
    def do_update(self, s):
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

        #need to cast attribute name to attribute value
        try:
            target = bucket["{}.{}".format(cname, cid)]
        except KeyError:
            print("** no instance found **")
            return False
        # could just check if "." in cattrvalue and if so cast float else cast int if alphanumeric else pass as string

        try:
            setattr(target, cattrname, float(cattrvalue) if not cattrvalue.isdecimal() else int(cattrvalue))#how to dynamically know the value of an atttribute...then cast... type it?
            storage.save()
        except ValueError:#wrote it this way if the float("alphastring" fails)
            setattr(target, cattrname, cattrvalue)
            storage.save()
        
    
    def help_update(self):
        print("update <classname> <classid> <attrname> <attrvalue: (int, float, str)>")
        #isdecimal doesn't return true for float numbers

        #ENOTE: need to test for a "update BModel 343243 cattrname "a spaced value"""

        




    do_EOF = do_exit
    help_EOF = help_exit
    prompt = "(hbnb)"
    myclasses = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"] #expand this list when you add new classes


if __name__ == "__main__":
    interpreter = HBNBCommand()
    interpreter.cmdloop()

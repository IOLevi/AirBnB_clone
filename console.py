#!/usr/bin/python3
'Console module'

import cmd
from models.base_model import BaseModel
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
        
        created = BaseModel()
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

    do_EOF = do_exit
    help_EOF = help_exit
    prompt = "(hbnb)"
    myclasses = ["BaseModel"]


if __name__ == "__main__":
    interpreter = HBNBCommand()
    interpreter.cmdloop()

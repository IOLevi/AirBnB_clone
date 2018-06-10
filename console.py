#!/usr/bin/python3
'Console module'

import cmd

"""
You must use the module cmd
Your class definition must be: class HBNBCommand(cmd.Cmd):
Your command interpreter should implement:
quit and EOF to exit the program
help (this action is provided by default by cmd but you should keep it updated and documented)
a custom prompt: (hbnb)
an empty line + ENTER shouldn’t execute anything
Your code should not be executed when imported"""

class HBNBCommand(cmd.Cmd):

    def emptyline(self):
        'empty lines will not repeat last command'
        pass
    
    def do_exit(self, s):
        return True
    
    def help_exit(self):
        print("Exit the interpreter.")
        print("You can also use CTRL-D (EOF) to exit")
    
    do_EOF = do_exit
    help_EOF = help_exit
    prompt = "(hbnb)"
    
if __name__ == "__main__":
    interpreter = HBNBCommand()
    interpreter.cmdloop()
    





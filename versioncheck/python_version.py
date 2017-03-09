from invoke import task
from subprocess import call
import invoke 

def check_invoke_version(ctx):
    minimal_verion = "0.15.0"
    if minimal_verion > invoke.__version__:
        print("Your python-invoke version is too old (currently "+invoke.__version__+"). Please update to version "+minimal_verion+" or higher.")
        print("call: pip install invoke --upgrade")
        correct = False
        response = False
        print("\nDo you want to resume with a old version? [YES/NO]?")
        while response != True:
            choice = raw_input().lower()
            if choice in yes:
                correct = True
                response = True
            elif choice in no:
                correct = False
                response = True
            else:
                sys.stdout.write("Please respond with 'yes' or 'no'")

        if correct == False:
            return False

        return True

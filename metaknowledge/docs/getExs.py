import os
import ast

# getExs: generates the docs in rst for the exceptions listed in mkExceptions.py
def getExs():

    os.chdir('..')

    with open('mkExceptions.py', 'r') as exceps:
        # use ast to read the docstrings for the overall module
        module = ast.parse(exceps.read())

    classes = []

    for node in module.body:  # each of the functions in that file
        if isinstance(node, ast.ClassDef):  # if it's a class...

            name = node.name
            docs = ast.get_docstring(node)
            params = [n.id for n in node.bases]

            # create an entry for each class
            entry = {"docs": docs, "name": name, "params": params}
            classes.append(entry)

    header = "#####################" # this is what you use to "underline" a header in RST

    # switch directories to now go into the docs and create, or overwrite, the exceptions docs
    os.chdir(os.path.join('docs', 'documentation', 'exceptions'))

    with open('index.rst', 'w') as f:
        # creating the header
        f.write(header + "\nExceptions\n")
        f.write(header + "\n\n")
        # done the header
        f.write("The exceptions defined by *metaknowledge* are:")
        f.write("\n\n********************\n\n")

        c_count = 0

        while c_count < len(classes):
            # writing each of the exceptions
            f.write("**" + classes[c_count]["name"] + "**\ ")
            params_list = classes[c_count]["params"]

            if len(params_list) == 0:
                pass
            elif len(params_list) == 1:
                f.write("(*" + params_list[0] + "*)")
            else:
                f.write("(")
                for p in params_list[:-1]:
                    f.write("*" + p + "*, ")
                f.write("*" + params_list[-1] + "*\ )")

            # if you do not wish to include the docstrings (as the existing docs do not), remove the next two lines:
            # otherwise, this checks if there are docstrings and adds them if there are.
            if classes[c_count]["docs"] != None:
                f.write("\n\n" + classes[c_count]["docs"])

            # adding a line before the next one
            if c_count < len(classes) - 1:
                f.write("\n\n********************\n\n")

            c_count += 1

    # go up one to be in the right place for next file
    os.chdir('..')


# main: so we can run it from the command line and it'll run all the functions
def main():
    getExs()

if __name__ == '__main__':
    main()



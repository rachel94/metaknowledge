import os
import ast

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

    header = "#####################"

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

            # if you do not wish to include the docstrings, remove the next two lines:
            if classes[c_count]["docs"] != None:
                f.write("\n\n" + classes[c_count]["docs"])
            ###

            if c_count < len(classes) - 1:
                f.write("\n\n********************\n\n")

            c_count += 1

    os.chdir('..')


# main: so we can run it from the command line and it'll run all the functions
def main():
    getExs()

if __name__ == '__main__':
    main()



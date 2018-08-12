import os
import ast

def getClasses():

    os.chdir('..')

    # start by doing this for just citation.py, then do it for all of them that follow this pattern. most are gonna be all the same.

    with open('citation.py', 'r') as f:
        # use ast to read the docstrings for the overall module
        module = ast.parse(f.read())

    classes = []

    # find the citation class itself
    for node in module.body:

        if isinstance(node, ast.ClassDef):
            name = node.name
            docs = ast.get_docstring(node)

            ## we get the methods inside the function by looking for FunctionDef s inside node.body!

            methods = []

            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    methods.append(item)

           # params = [n.id for n in node.bases]

            entry = {"docs": docs, "name": name, "methods": methods}
            #, "params": params}
            classes.append(entry)

    header = "#####################"

    os.chdir(os.path.join('docs', 'documentation', 'classes'))

    with open('citation.rst', 'w') as f:
        # creating the header
        f.write(header + "\nCitation\n")
        f.write(header + "\n\n")
        # done the header
        f.write("\n\n********************\n\n")
        f.write("Citations are special, here is how they are handled.")

        cls = classes[0]['name']

        f.write("\n\n" + cls)

        f.write("\n\n" + classes[0]['docs'])

        f.write("\n\n")

        title = '**The {} class has the following methods:**'.format(cls)
        f.write(title)
        f.write("\n" + "^" * len(title) + "\n\n")

        for mthd in methods:
            if mthd.name[0:2] != "__": # not including those with __; if you would like to, then just remove this if, and dedent the following...
                mthd_title = cls + "." + mthd.name + "()"
                f.write(mthd_title)
                f.write("\n" + "=" * len(title) + "\n\n")
                # okay need to add the params and defaults like you did in docsGen!!!
                f.write(ast.get_docstring(mthd))
                f.write("\n\n***********\n\n")
        # here we should be able to use the code from docsGen to get the function names from inside citation.py


            #f.write(entry['name'])

            # c_count = 0
            #
            # while c_count < len(classes):
            #     f.write("**" + classes[c_count]["name"] + "**\ ")
            #     params_list = classes[c_count]["params"]
            #
            #     if len(params_list) == 0:
            #         pass
            #     elif len(params_list) == 1:
            #         f.write("(*" + params_list[0] + "*)")
            #     else:
            #         f.write("(")
            #         for p in params_list[:-1]:
            #             f.write("*" + p + "*, ")
            #         f.write("*" + params_list[-1] + "*\ )")
            #
            #     # if you do not wish to include the docstrings, remove the next two lines:
            #     if classes[c_count]["docs"] != None:
            #         f.write("\n\n" + classes[c_count]["docs"])
            #     ###
            #
            #     if c_count < len(classes) - 1:
            #         f.write("\n\n********************\n\n")
            #
            #     c_count += 1

    os.chdir('..')

# main: so we can run it from the command line and it'll run all the functions
def main():
    getClasses()

if __name__ == '__main__':
    main()


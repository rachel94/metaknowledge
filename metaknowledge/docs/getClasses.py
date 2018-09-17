import os
import ast

# getClasses: Used to get the docstrings for each of the classes in mk and generate docs for them
def getClasses():

    # we start in docs directory so we need to go up one level
    os.chdir('..')

    # I started by doing this for just citation.py, with the idea of figuring it out for one and then generalizing or following the same pattern for the others, as most will basically need to be done the same way.

    with open('citation.py', 'r') as f:
        # use ast to read the docstrings for the overall file
        module = ast.parse(f.read())

    classes = []

    # find the citation class itself
    for node in module.body:

        if isinstance(node, ast.ClassDef): # if it's a class – ast package has lots of methods you can use to check like this
            name = node.name
            docs = ast.get_docstring(node)

            ## we the get the methods inside the function by looking for FunctionDef s inside node.body
            methods = []

            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    methods.append(item)

            # we then need to get the parameters too, I haven't done this yet...
           # params = [n.id for n in node.bases]

            entry = {"docs": docs, "name": name, "methods": methods}
            #, "params": params}
            classes.append(entry)

    header = "#####################" # this is the RST syntax

    # change directory so we can go to where the docs need to be generated
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

        # this is to create a table of contents...

        m_count = 0


        for mthd in methods:
            if mthd.name[0:2] != "__": # not including those with __; if you would like to, then just remove this if, and dedent the following...
                mthd_title = cls + "." + mthd.name + "()"
                f.write(mthd_title)
                f.write("\n" + "=" * len(title) + "\n\n")
                # here we would want to add the parameters and defaults the way we did in genModules.
                f.write(ast.get_docstring(mthd))
                f.write("\n\n***********\n\n")

        # here we should be able to basically use the code from getModules to get the function names from inside citation.py
        # this is essentially copied over from getExs, it may prove useful here

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
            #         f.write("\n\n" + classes[c_count]["docs"]
            #
            #     if c_count < len(classes) - 1:
            #         f.write("\n\n********************\n\n")
            #
            #     c_count += 1

    # go up one to be in the right place for next file
    os.chdir('..')



# main: so we can run it from the command line and it'll run all the functions
def main():
    getClasses()

if __name__ == '__main__':
    main()


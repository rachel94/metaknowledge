import os
import ast

# mods: this is the names of the modules; ideally this would be generated automatically
mods = ['WOS', 'contour', 'medline', 'proquest', 'scopus', 'journalAbbreviations']

# convertDefaults: used to convert the defaults into a usable format
# so far this has only been used in getModules, but it'd be useful for any others that have defaults that you want to include in the docs
def convertDefaults(default_list, params_list):

    new_defaults = []

    for d in default_list:
        # the following is to convert the defaults into a more easy to work with/familiar type
        if type(d) == ast.Num:
            new_defaults.append(str(d.n))
        elif type(d) == ast.NameConstant:
            new_defaults.append(str(d.value))
        elif type(d) == ast.Str:
            new_defaults.append(d.s)
        else:
            try:
                new_defaults.append(d.value)
            except:
                new_defaults.append("unknown value")

    # the first parameters are those without defaults, so if not all parameters have defaults, then len(new_defaults) < len(params_list). To make it easier to format things later, this adds blanks for those parameters that do not have corresponding defaults, so that the indices for parameters that do have defaults are the same as their corresponding default
    len_def = len(new_defaults)
    len_params = len(params_list)

    if len_def == len_params:
        pass

    else:
        blanks = [" "] * (len_params-len_def)
        new_defaults = blanks + new_defaults

    return new_defaults



# writeModFiles: gets the info from the module files and writes it to the rst files. this is for the 6 modules of mk.
def writeModFiles():

    # this is run from docs, so we need to go up to access the modules
    os.chdir('..')

    for mod in mods: # do everything for each module

        os.chdir(mod)
        with open('__init__.py', 'r') as init:
            # use ast to read the docstrings for the overall module, in __init__.py
            tree = ast.parse(init.read())
        docstring = ast.get_docstring(tree)

        # find all the files with scripts:
        good_file = (file for file in os.listdir() if file[-3:] == '.py' and file != '__init__.py')

        # this was an attempt to also access any "good files" in tagProcessing subdirectory, if it existed. It didn't work so I access those later, in a diff way

        # good_tag_files = (file for file in os.listdir('tagProcessing') if file[-3:] == '.py' and file != '__init__.py')
        #
        # for file in good_tag_files:
        #     file += os.path.join('tagProcessing, file')
        #
        # good_file = itertools.chain(good_tag_files, good_file)
        # print(good_file)

        functions = []

        for file in good_file: #each of the .py files
            with open(file, 'r') as f:
                module = ast.parse(f.read())

            for node in module.body: # each of the functions in that file
                if isinstance(node, ast.FunctionDef): # if it's a function...

                    # getting the parameters and defaults
                    params = node.args.args
                    params_list = [p.arg for p in params]
                    defaults = node.args.defaults
                    defaults = convertDefaults(defaults, params_list)

                    # create a list of parameters and defaults together
                    p_d_list = []
                    i = 0
                    while i < len(params_list):
                        if defaults[i] != " ":
                            p_d = params_list[i] + "=" + defaults[i]
                        else:
                            p_d = params_list[i]
                        p_d_list.append(p_d)
                        i += 1

                    # create an entry for each function
                    entry = {"docs": ast.get_docstring(node), "fn_name": node.name, "params": params_list, "defaults": defaults, "params_defs": p_d_list}
                    functions.append(entry)

        # some modules also have a subdirectory called tagProcessing that has more functions we need.
        if mod == "medline" or mod == "WOS" or mod == "proquest":
            os.chdir('tagProcessing')

            with open('tagFunctions.py', 'r') as f:
                module = ast.parse(f.read())

            for node in module.body:  # each of the functions in that file

                if isinstance(node, ast.FunctionDef): # if it's a function
                    if (mod == "proquest" and node.name == 'proQuestTagToFunc') or mod != "proquest": # we want all of them from WOS or medline, but only one from proquest

                        # this then does the same thing that we did for the other files above, so ideally it would be simplified to remove this repeated code:
                        params = node.args.args
                        params_list = [p.arg for p in params]
                        defaults = node.args.defaults
                        defaults = convertDefaults(defaults, params_list)

                        # create a list of parameters and defaults together
                        p_d_list = []
                        i = 0
                        while i < len(params_list):
                            if defaults[i] != " ":
                                p_d = params_list[i] + "=" + defaults[i]
                            else:
                                p_d = params_list[i]
                            p_d_list.append(p_d)
                            i += 1

                        # create an entry for each function
                        entry = {"docs": ast.get_docstring(node), "fn_name": node.name, "params": params_list, "defaults": defaults, "params_defs": p_d_list}
                        functions.append(entry)

            # if we've gone into a tagProcessing subdirectory, we need to get out of it
            os.chdir('..')

        # before exiting the loop, get out of the mod file, and go into docs, since this is where we need to be at the start of the loop
        os.chdir(os.path.join('..', 'docs'))



        # now, create the rst files (for readability, we might want to make this its own function)
        fname =  os.path.join("documentation", "modules", mod + ".rst")
        header = "#####################" # that is part of the rst syntax

        # creating the files and writing if it doesn't exist yet
        # if the file already exists, it gets overwritten
        with open(fname, 'w') as f:
            # creating the header
            f.write(header + "\n")
            if mod == "journalAbbreviations":
                f.write('Journal Abbreviations' + "\n")
            elif mod == "WOS":
                f.write("WOS" + "\n")
            else:
                f.write(mod.capitalize() + "\n")
            f.write(header + "\n\n")
            # done the header
            f.write(docstring + "\n\n")
            title = '**The {} module provides the following functions:**'.format(mod)
            f.write(title)
            f.write("\n" + "-"*len(title) + "\n\n")

            # now add the functions!

            # first a TOC for the functions. I tried to make these have links (hence all the commented code), but it didn't work. I left it so you can try to work from this.
            f_count = 0

            while f_count < len(functions):
                #link_name = mod + "_" + functions[f_count]["fn_name"]
                # f.write("|" + link_name + "|_" + "\n\n")
                # f.write(".. _" + link_name + ": #" + link_name + "\n")
                # f.write(".. |" + link_name + "| replace:: ")
                f.write("**" + functions[f_count]["fn_name"] + "**\ (")

                # add the parameters to the function
                p_str = ""
                for p in functions[f_count]["params_defs"]:
                    p_str += p + ", "
                p_str = p_str[:-2]

                f.write(p_str + ")\n\n")


                # f.write(p_str + ") <#")
                # f.write(mod + "-")
                # p_str = ""
                # for p in functions[f_count]["params_defs"]:
                #     p_str += p + "-"
                # p_str = p_str[:-2]
                # f.write(p_str + ">`__\n\n")



                f_count += 1

            f.write("\n\n**********************\n\n")

            # now the details of the functions
            f_count = 0

            while f_count < len(functions):
                # again this was all an attempt to get IDs on the html elements so that it could link to each function. I don't think they should need IDs though as RST seems to implement this automatically.
                #link_name = mod + "_" + functions[f_count]["fn_name"]
                # f.write(".. container::\n")
                # f.write("    :name: " + link_name + "\n\n")
                # f.write("    " + mod.lower() + ".\ **" + functions[f_count]["fn_name"] + "**\ (")
                p_str = ""
                for p in functions[f_count]["params_defs"]:
                    p_str += p + ", "
                p_str = p_str[:-2]

                mod_name = mod + "." + functions[f_count]["fn_name"] + "(" + p_str + ")"
                f.write(mod_name)
                f.write("\n" + "=" * len(mod_name) + "\n\n")

                f.write("\n" + functions[f_count]["docs"])

                if f_count < len(functions)-1:
                    # creates a line to separate from the following function
                    f.write("\n\n********************\n\n")

                f_count += 1

        # go up one to be in the right place for next file
        os.chdir('..')



# main: so we can run it from the command line and it'll run all the functions
def main():
    writeModFiles()

if __name__ == '__main__':
    main()

import os
import ast

# this is the names of the modules
# ideally this would be generated automatically
mods = ['WOS', 'contour', 'medline', 'proquest', 'scopus', 'journalAbbreviations']

# here we convert the defaults into a usable format
def convertDefaults(default_list, params_list):

    new_defaults = []

    for d in default_list:
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

    len_def = len(new_defaults)
    len_params = len(params_list)

    if len_def == len_params:
        pass

    else:
        blanks = [" "] * (len_params-len_def)
        new_defaults = blanks + new_defaults

    return new_defaults



# writeModFiles gets the info from the module files and writes it to the rst files
def writeModFiles():
    if not os.path.exists('mods'):
        os.makedirs('mods')

    # go up so we can access the modules
    os.chdir('..')

    for mod in mods:

        os.chdir(mod)
        with open('__init__.py', 'r') as init:
            tree = ast.parse(init.read())
        docstring = ast.get_docstring(tree)

        # find all the files with scripts:
        good_file = (file for file in os.listdir() if file[-3:] == '.py' and file != '__init__.py')

        functions = []

        for file in good_file: #each of the .py  files
            with open(file, 'r') as f:
                module = ast.parse(f.read())

            for node in module.body: #each of the functions in that file
                if isinstance(node, ast.FunctionDef):

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
                        print(p_d_list)

                        i += 1

                    # create an entry for each function
                    entry = {"docs": ast.get_docstring(node), "fn_name": node.name, "params": params_list, "defaults": defaults, "params_defs": p_d_list}
                    functions.append(entry)

        os.chdir(os.path.join('..', 'docs'))

        # now, create the rst files
        fname =  os.path.join("documentation", "modules", mod + ".rst")
        header = "#####################"

        # creating the files and writing if it doesn't exist yet
        # if the file already exists, it gets overwritten
        with open(fname, 'w') as f:
            f.write(header + "\n")
            if mod == "journalAbbreviations":
                f.write('Journal Abbreviations' + "\n")
            else:
                f.write(mod.capitalize() + "\n")
            f.write(header + "\n\n")
            f.write(docstring + "\n\n")
            f.write('**The {} module provides the following functions:**'.format(mod))
            f.write('\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            f.write('\n\n')

            print(functions[0]["params_defs"])
            print(functions[0]["defaults"])

            for fn in functions:
                f.write("**" + fn["fn_name"] + "**\ (")

                # add the parameters to the function
                p_str = ""
                for p in fn["params_defs"]:
                    p_str += p + ", "
                p_str = p_str[:-2]
                f.write(p_str + ")\n\n")

                f.write(fn["docs"] + "\n\n********************\n\n")

        # go up two to be in the right place for next file
        os.chdir(os.path.join('..'))




    

def main():
    writeModFiles()

if __name__ == '__main__':
    main()

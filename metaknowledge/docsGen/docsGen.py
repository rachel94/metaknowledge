import os
import ast

mods = ['WOS', 'contour', 'medline', 'proquest', 'scopus', 'journalAbbreviations']

def writeModFiles():
    if not os.path.exists('mods'):
        os.makedirs('mods')

    # go up so we can access the modules
    os.chdir('..')

    for mod in mods:

        #os.chdir(mod)
        with open(os.path.join(mod, '__init__.py'), 'r') as init:
            tree = ast.parse(init.read())
        docstring = ast.get_docstring(tree)

        os.chdir(os.path.join('docsGen', 'mods'))

        # now, create the new stuff.
        fname =  mod + ".rst"
        # creating the files and writing if it doesn't exist yet
        # if the file already exists, it gets overwritten
        with open(fname, 'w') as f:
            f.write(docstring + "\n\n")
            f.write('**The {} module provides the following functions:**'.format(mod))

        # go up two to be in the right place for next file
        os.chdir(os.path.join('..', '..'))

 

        
    

def main():
    writeModFiles()

if __name__ == '__main__':
    main()

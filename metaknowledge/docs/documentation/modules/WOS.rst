#####################
Wos
#####################

These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.

**The WOS module provides the following functions:**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**recordParser**\ (paper)

This is function that is used to create [`Records`](#metaknowledge.Record) from files.

**recordParser**() reads the file _paper_ until it reaches 'ER'. For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following two lines in a record:

    AF BREVIK, I
       ANICIN, B

The entry in the returned dict would be `{'AF' : ["BREVIK, I", "ANICIN, B"]}`

`Record` objects can be created with these dictionaries as the initializer.

# Parameters

_paper_ : `file stream`

> An open file, with the current line at the beginning of the WOS record.

# Returns

`OrderedDict[str : List[str]]`

> A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.

********************

**isWOSFile**\ (infile, checkedLines=3)

Determines if _infile_ is the path to a WOS file. A file is considerd to be a WOS file if it has the correct encoding (`utf-8` with a BOM) and within the first _checkedLines_ a line starts with `"VR 1.0"`.

# Parameters

_infile_ : `str`

> The path to the targets file

_checkedLines_ : `optional [int]`

> default 2, the number of lines to check for the header

# Returns

`bool`

> `True` if the file is a WOS file

********************

**wosParser**\ (isifile)

This is function that is used to create [`RecordCollections`](#metaknowledge.RecordCollection) from files.

**wosParser**() reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF. All WOS records it encounters are parsed with [**recordParser**()](#metaknowledge.recordParser) and converted into [`Records`](#metaknowledge.Record). A list of these `Records` is returned.

`BadWOSFile` is raised if an issue is found with the file.

# Parameters

_isifile_ : `str`

> The path to the target file

# Returns

`List[Record]`

> All the `Records` found in _isifile_

********************


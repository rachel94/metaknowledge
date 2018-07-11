#####################
Medline
#####################

These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.

**The medline module provides the following functions:**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**isMedlineFile**\ (infile, checkedLines=2)

Determines if _infile_ is the path to a Medline file. A file is considerd to be a Medline file if it has the correct encoding (`latin-1`) and within the first _checkedLines_ a line starts with `"PMID- "`.

# Parameters

_infile_ : `str`

> The path to the targets file

_checkedLines_ : `optional [int]`

> default 2, the number of lines to check for the header

# Returns

`bool`

> `True` if the file is a Medline file

********************

**medlineParser**\ (pubFile)

Parses a medline file, _pubFile_, to extract the individual entries as [`MedlineRecords`](#metaknowledge.MedlineRecord).

A medline file is a series of entries, each entry is a series of tags. A tag is a 2 to 4 character string each tag is padded with spaces on the left to make it 4 characters which is followed by a dash and a space (`'- '`). Everything after the tag and on all lines after it not starting with a tag is considered associated with the tag. Each entry's first tag is `PMID`, so a first line looks something like `PMID- 26524502`. Entries end with a single blank line.

# Parameters

_pubFile_ : `str`

> A path to a valid medline file, use [`isMedlineFile`](#metaknowledge.isMedlineFile) to verify

# Returns

`set[MedlineRecord]`

> Records for each of the entries

********************

**medlineRecordParser**\ (record)

The parser [`MedlineRecord`](#metaknowledge.MedlineRecord) use. This takes an entry from [`medlineParser()`](#metaknowledge.medlineParser) and parses it a part of the creation of a `MedlineRecord`.

# Parameters

_record_ : `enumerate object`

> a file wrapped by `enumerate()`

# Returns

`collections.OrderedDict`

> An ordered dictionary of the key-vaue pairs in the entry

********************


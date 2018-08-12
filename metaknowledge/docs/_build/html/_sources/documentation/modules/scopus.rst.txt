#####################
Scopus
#####################

These are the functions used to process scopus csv files at the backend. They are meant for use internal use by metaknowledge.

**The scopus module provides the following functions:**
-------------------------------------------------------

**scopusRecordParser**\ (record, header=None)

**isScopusFile**\ (infile, checkedLines=2, maxHeaderDiff=3)

**scopusParser**\ (scopusFile)



**********************

scopus.scopusRecordParser(record, header=None)
==============================================


The parser `ScopusRecords <../classes/scopusrecord.html>`__ use. This takes a line from `scopusParser() <#scopus-scopusparser-scopusfile>`__ and parses it as a part of the creation of a `ScopusRecord`.

**Note** this is for csv files downloaded from scopus _not_ the text records as those are less complete. Also, Scopus uses double quotes (`"`) to quote strings, such as abstracts, in the csv so double quotes in the string must be escaped. For reasons not fully understandable by mortals they choose to use two double quotes in a row (`""`) to represent an escaped double quote. This parser does not unescape these quotes, but it does correctly handle their interacts with the outer double quotes.

**Parameters**

| *record*\ : ``str``
| string ending with a newline containing the record's entry

**Returns**

| ``dict``
| A dictionary of the key-vaue pairs in the entry

********************

scopus.isScopusFile(infile, checkedLines=2, maxHeaderDiff=3)
============================================================


Determines if *infile* is the path to a Scopus csv file. A file is considerd to be a Scopus file if it has the correct encoding (`utf-8` with BOM (Byte Order Mark)) and within the first *checkedLines* a line contains the complete header, the list of all header entries in order is found in `scopus.scopusHeader <#scopus>`__.

**Note** this is for csv files *not* plain text files from scopus, plain text files are not complete.

**Parameters**

| *infile*\ : ``str``
| The path to the targets file

| *checkedLines*\ : ``optional [int]``
| default 2, the number of lines to check for the header

| *maxHeaderDiff*\ : ``optional [int]``
| default 3, maximum number of different entries in the potetial file from the current known header ``metaknowledge.scopus.scopusHeader``, if exceeded an ``False`` will be returned

**Returns**
| ``bool``
| ``True`` if the file is a Scopus csv file

********************

scopus.scopusParser(scopusFile)
===============================


Parses a scopus file, *scopusFile*, to extract the individual lines as `ScopusRecords <../classes/scopusrecord.html>`__.

A Scopus file is a csv (Comma-separated values) with a complete header, see [`scopus.scopusHeader`](#metaknowledge.scopus) for the entries, and each line after it containing a record's entry. The string valued entries are quoted with double quotes which means double quotes inside them can cause issues, see [`scopusRecordParser()`](#metaknowledge.scopusRecordParser) for more information.

**Parameters**

| *scopusFile*\ : ``str``
| A path to a valid scopus file, use `isScopusFile() <#scopus-isscopusfile-infile-checkedlines-2-maxheaderdiff-3>`__ to verify

**Returns**

| ``set[ScopusRecord]``
| Records for each of the entries
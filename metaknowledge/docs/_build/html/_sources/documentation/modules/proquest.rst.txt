#####################
Proquest
#####################

These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.

**The proquest module provides the following functions:**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**isProQuestFile**\ (infile, checkedLines=2)

**proQuestParser**\ (proFile)

**proQuestRecordParser**\ (enRecordFile, recNum)



**********************

proquest.\ **isProQuestFile**\ (infile, checkedLines=2):


Determines if *infile* is the path to a ProQuest file. A file is considered to be a Proquest file if it has the correct encoding (``utf-8``) and within the first *checkedLines* the following starts. ::

    ____________________________________________________________

    Report Information from ProQuest

**Parameters**

| *infile*\ : ``str``
| The path to the targets file

| *checkedLines*\ : ``optional [int]``
| default 2, the number of lines to check for the header

**Returns**

| ``bool``
| ``True`` if the file is a valid ProQuest file

********************

proquest.\ **proQuestParser**\ (proFile):


Parses a ProQuest file, *proFile*, to extract the individual entries.

A ProQuest file has three sections, first a list of the contained entries, second the full metadata and finally a bibtex formatted entry for the record. This parser only uses the first two as the bibtex contains no information the second section does not. Also, the first section is only used to verify the second section. The returned [`ProQuestRecords`](#metaknowledge.ProQuestRecord) contains the data from the second section, with the same key strings as ProQuest uses and the unlabeled sections are called in order, ``'Name'``, ``'Author'`` and ``'url'``.

**Parameters**

| *proFile*\ : ``str``
| A path to a valid ProQuest file, use [`isProQuestFile`](#metaknowledge.isProQuestFile) to verify

**Returns**

| ``set[ProQuestRecord]``
| Records for each of the entries

********************

proquest.\ **proQuestRecordParser**\ (enRecordFile, recNum):


The parser [`ProQuestRecords`](#metaknowledge.ProQuestRecord) use. This takes an entry from [`proQuestParser()`](#metaknowledge.proQuestParser) and parses it a part of the creation of a ``ProQuestRecord``.

**Parameters**

| *enRecordFile*\ : ``enumerate object``
| a file wrapped by ``enumerate()``

| *recNum*\ : ``int``
| The number given to the entry in the first section of the ProQuest file

**Returns**

| ``collections.OrderedDict``
| An ordered dictionary of the key-vaue pairs in the entry
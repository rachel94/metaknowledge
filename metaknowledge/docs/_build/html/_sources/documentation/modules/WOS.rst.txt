#####################
WOS
#####################

These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.

**The WOS module provides the following functions:**
----------------------------------------------------

**recordParser**\ (paper)

**isWOSFile**\ (infile, checkedLines=3)

**wosParser**\ (isifile)

**pubType**\ (val)

**authorsFull**\ (val)

**group**\ (val)

**editedBy**\ (val)

**authorsShort**\ (val)

**bookAuthor**\ (val)

**bookAuthorFull**\ (val)

**groupName**\ (val)

**title**\ (val)

**editors**\ (val)

**journal**\ (val)

**seriesTitle**\ (val)

**seriesSubtitle**\ (val)

**language**\ (val)

**docType**\ (val)

**confTitle**\ (val)

**confDate**\ (val)

**confSponsors**\ (val)

**wosTimesCited**\ (val)

**authAddress**\ (val)

**confLocation**\ (val)

**j9**\ (val)

**funding**\ (val)

**subjectCategory**\ (val)

**citations**\ (val)

**publisherCity**\ (val)

**ISSN**\ (val)

**articleNumber**\ (val)

**issue**\ (val)

**email**\ (val)

**eISSN**\ (val)

**DOI**\ (val)

**wosString**\ (val)

**orcID**\ (val)

**meetingAbstract**\ (val)

**isoAbbreviation**\ (val)

**pageCount**\ (val)

**publisher**\ (val)

**ISBN**\ (val)

**month**\ (val)

**fundingText**\ (val)

**bookDOI**\ (val)

**volume**\ (val)

**ResearcherIDnumber**\ (val)

**citedRefsCount**\ (val)

**beginningPage**\ (val)

**abstract**\ (val)

**supplement**\ (val)

**confHost**\ (val)

**publisherAddress**\ (val)

**endingPage**\ (val)

**year**\ (val)

**authKeywords**\ (val)

**reprintAddress**\ (val)

**totalTimesCited**\ (val)

**partNumber**\ (val)

**specialIssue**\ (val)

**subjects**\ (val)

**keywords**\ (val)

**pubMedID**\ (val)

**documentDeliveryNumber**\ (val)



**********************

WOS.recordParser(paper)
=======================


This is function that is used to create [`Records`](#metaknowledge.Record) from files.

**recordParser**\ () reads the file *paper* until it reaches 'ER'. For each field tag it adds an entry to the returned dict with the tag as the key and a list of the entries as the value, the list has each line separately, so for the following two lines in a record: ::

    AF BREVIK, I
    ANICIN, B

The entry in the returned dict would be ``{'AF' : ["BREVIK, I", "ANICIN, B"]}``

``Record`` objects can be created with these dictionaries as the initializer.

**Parameters**

| *paper*\ : ``file stream``
| An open file, with the current line at the beginning of the WOS record.

**Returns**

| `OrderedDict[str : List[str]]``
| A dictionary mapping WOS tags to lists, the lists are of strings, each string is a line of the record associated with the tag.

********************

WOS.isWOSFile(infile, checkedLines=3)
=====================================


Determines if *infile*\ is the path to a WOS file. A file is considerd to be a WOS file if it has the correct encoding (``utf-8`` with a BOM) and within the first *checkedLines*\ a line starts with ``"VR 1.0"``.

**Parameters**

| *infile*\ : ``str``
| The path to the targets file

| *checkedLines*\ : ``optional [int]``
| default 2, the number of lines to check for the header

**Returns**

| ``bool``
| ``True`` if the file is a WOS file

********************

WOS.wosParser(isifile)
======================


This is function that is used to create [`RecordCollections`](#metaknowledge.RecordCollection) from files.

**wosParser**\ () reads the file given by the path isifile, checks that the header is correct then reads until it reaches EF. All WOS records it encounters are parsed with [**recordParser**\ ()](#metaknowledge.recordParser) and converted into [`Records`](#metaknowledge.Record). A list of these ``Records`` is returned.

``BadWOSFile`` is raised if an issue is found with the file.

**Parameters**

| *isifile*\ : ``str``
| The path to the target file

**Returns**

| ``List[Record]``
| All the ``Records`` found in *isifile*

********************

WOS.pubType(val)
================


**The PT Tag**

| extracts the type of publication as a character: conference, book, journal, book in series, or patent

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| A string

********************

WOS.authorsFull(val)
====================


**The AF Tag**

| extracts a list of authors full names

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| A list of author's names

********************

WOS.group(val)
==============


**The GP Tag**

| extracts the group associated with the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| A the name of the group

********************

WOS.editedBy(val)
=================


**The BE Tag**

| extracts a list of the editors of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| A list of editors

********************

WOS.authorsShort(val)
=====================


**The AU Tag**

| extracts a list of authors shortened names

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| A list of shortened author's names

********************

WOS.bookAuthor(val)
===================


**The BA Tag**

| extracts a list of the short names of the authors of a book Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| A list of shortened author's names

********************

WOS.bookAuthorFull(val)
=======================


**The BF Tag**

| extracts a list of the long names of the authors of a book Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| A list of author's names

********************

WOS.groupName(val)
==================


**The CA Tag**

| extracts the name of the group associated with the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The group's name

********************

WOS.title(val)
==============


**The TI Tag**

| extracts the title of the record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The title of the record

********************

WOS.editors(val)
================


**Needs Work**

| currently not well understood, returns *val*    

********************

WOS.journal(val)
================


**The SO Tag**

| extracts the full name of the publication and normalizes it to uppercase

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The name of the journal

********************

WOS.seriesTitle(val)
====================


**The SE Tag**

| extracts the title of the series the Record is in

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The title of the series

********************

WOS.seriesSubtitle(val)
=======================


**The BS Tag**

| extracts the title of the series the Record is in

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The subtitle of the series

********************

WOS.language(val)
=================


**The LA Tag**

| extracts the languages of the Record as a string with languages separated by ', ', usually there is only one language

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The language(s) of the record

********************

WOS.docType(val)
================


**The DT Tag**

| extracts the type of document the Record contains

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The type of the Record

********************

WOS.confTitle(val)
==================


**The CT Tag**

| extracts the title of the conference associated with the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The title of the conference

********************

WOS.confDate(val)
=================


**The CY Tag**

| extracts the date string of the conference associated with the Record, the date is not normalized

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The data of the conference

********************

WOS.confSponsors(val)
=====================


**The SP Tag**

| extracts a list of sponsors for the conference associated with the record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``

> A the list of of sponsors

********************

WOS.wosTimesCited(val)
======================


**The TC Tag**

| extracts the number of times the Record has been cited by records in WOS

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

``int``
| The number of time the Record has been cited

********************

WOS.authAddress(val)
====================


**The C1 Tag**

| extracts the address of the authors as given by WOS. **Warning** the mapping of author to address is not very good and is given in multiple ways.

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``

> A list of addresses

********************

WOS.confLocation(val)
=====================


**The CL Tag**

| extracts the sting giving the conference's location

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The conferences address

********************

WOS.j9(val)
===========


**The J9 Tag**

| extracts the J9 (29-Character Source Abbreviation) of the publication

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The 29-Character Source Abbreviation

********************

WOS.funding(val)
================


**The FU Tag**

| extracts a list of the groups funding the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``

> A list of funding groups

********************

WOS.subjectCategory(val)
========================


**The SC Tag**

| extracts a list of the subjects associated with the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``

> A list of the subjects associated with the Record

********************

WOS.citations(val)
==================


**The CR Tag**

| extracts a list of all the citations in the record, the citations are the [metaknowledge.Citation](#Citation.Citation) class.

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

`` list[metaknowledge.Citation]``

> A list of Citations

********************

WOS.publisherCity(val)
======================


**The PI Tag**

| extracts the city the publisher is in

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The city of the publisher

********************

WOS.ISSN(val)
=============


**The SN Tag**

| extracts the ISSN of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The ISSN string

********************

WOS.articleNumber(val)
======================


**The AR Tag**

| extracts a string giving the article number, not all are integers

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The article number

********************

WOS.issue(val)
==============


**The IS Tag**

| extracts a string giving the issue or range of issues the Record was in, not all are integers

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The issue number/range

********************

WOS.email(val)
==============


**The EM Tag**

| extracts a list of emails given by the authors of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``

> A list of emails

********************

WOS.eISSN(val)
==============


**The EI Tag**

| extracts the EISSN of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The EISSN string

********************

WOS.DOI(val)
============


**The DI Tag**

return the DOI number of the record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The DOI number string

********************

WOS.wosString(val)
==================


**The UT Tag**

| extracts the WOS number of the record as a string preceded by "WOS:"

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The WOS number

********************

WOS.orcID(val)
==============


**The OI Tag**

| extracts a list of orc IDs of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The orc ID

********************

WOS.meetingAbstract(val)
========================


**The MA Tag**

| extracts the ID of the meeting abstract prefixed by 'EPA-'

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The meeting abstract prefixed

********************

WOS.isoAbbreviation(val)
========================


**The JI Tag**

| extracts the iso abbreviation of the journal

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The iso abbreviation of the journal

********************

WOS.pageCount(val)
==================


**The PG Tag**

returns an integer giving the number of pages of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

``int``
| The page count

********************

WOS.publisher(val)
==================


**The PU Tag**

| extracts the publisher of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The publisher

********************

WOS.ISBN(val)
=============


**The BN Tag**

| extracts a list of ISBNs associated with the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list``
| The ISBNs

********************

WOS.month(val)
==============


**The PD Tag**

| extracts the month the record was published in as an int with January as 1, February 2, ...

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

``int``

> A integer giving the month

********************

WOS.fundingText(val)
====================


**The FX Tag**

| extracts a string of the funding thanks

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The funding thank-you

********************

WOS.bookDOI(val)
================


**The D2 Tag**

| extracts the book DOI of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The DOI number

********************

WOS.volume(val)
===============


**The VL Tag**

return the volume the record is in as a string, not all are integers

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The volume number

********************

WOS.ResearcherIDnumber(val)
===========================


**The RI Tag**

| extracts a list of the research IDs of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| The list of the research IDs

********************

WOS.citedRefsCount(val)
=======================


**The NR Tag**

| extracts the number citations, length of CR list

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

``int``
| The number of CRs

********************

WOS.beginningPage(val)
======================


**The BP Tag**

| extracts the first page the record occurs on, not all are integers

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The first page number

********************

WOS.abstract(val)
=================


**The AB Tag**

return abstract of the record, with newlines hopefully in the correct places

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The abstract

********************

WOS.supplement(val)
===================


**The SU Tag**

| extracts the supplement number

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The supplement number

********************

WOS.confHost(val)
=================


**The HO Tag**

| extracts the host of the conference

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The host

********************

WOS.publisherAddress(val)
=========================


**The PA Tag**

| extracts the publishers address

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The publisher address

********************

WOS.endingPage(val)
===================


**The EP Tag**

return the last page the record occurs on as a string, not aall are intergers

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The final page number

********************

WOS.year(val)
=============


**The PY Tag**

| extracts the year the record was published in as an int

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

``int``
| The year

********************

WOS.authKeywords(val)
=====================


**The DE Tag**

| extracts the keywords assigned by the author of the Record. The WOS description is:

    Author keywords are included in records of articles from 1991 forward. They are also include in conference proceedings records.

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| The list of keywords

********************

WOS.reprintAddress(val)
=======================


**The RP Tag**

| extracts the reprint address string

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The reprint address

********************

WOS.totalTimesCited(val)
========================


**The Z9 Tag**

| extracts the total number of citations of the record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

``int``
| The total number of citations

********************

WOS.partNumber(val)
===================


**The PN Tag**

return an integer giving the part of the issue the Record is in

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

``int``
| The part of the issue of the Record

********************

WOS.specialIssue(val)
=====================


**The SI Tag**

| extracts the special issue value

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The special issue value

********************

WOS.subjects(val)
=================


**The WC Tag**

| extracts a list of subjects as assigned by WOS

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| The subjects list

********************

WOS.keywords(val)
=================


**The ID Tag**

| extracts the WOS keywords of the Record. The WOS description is:

    KeyWords Plus are index terms created by Thomson Reuters from significant, frequently occurring words in the titles of an article's cited references.

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``list[str]``
| The keyWords list

********************

WOS.pubMedID(val)
=================


**The PM Tag**

| extracts the pubmed ID of the record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The pubmed ID

********************

WOS.documentDeliveryNumber(val)
===============================


**The GA Tag**

| extracts the document delivery number of the Record

**Parameters**

| *val*\ : ``list[str]``
| The raw data from a WOS file

**Returns**

| ``str``
| The document delivery number
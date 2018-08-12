#####################
Journal Abbreviations
#####################

This module handles the abbreviations, known as J29 abbreviations and given by the J9 tag in WOS Records and for journal titles that WOS employs in citations.

The citations provided by WOS used abbreviated journal titles instead of the full names. The full list of abbreviations can be found at a series pages divided by letter starting at [images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html](http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html). The function `updatej9DB() <#journalabbreviations-updatej9db>`__ is used to scrape and parse the pages, it must be run without error before the other features can be used. *metaknowledge*. If the database is requested by ``getj9dict()``, which is what `Citations <../classes/citation.html>`__ use, and the database is not found or is corrupted then `updatej9DB() <#journalabbreviations-updatej9db>`__ will be run to download the database if this fails an ``mkException`` will be raised, the download and parsing usually takes less than a second on a good internet connection.

The other functions of the module are for manually adding and removing abbreviations from the database. It is recommended that this be done with the command-line tool ``metaknowledge`` instead of with a script.

**The journalAbbreviations module provides the following functions:**
---------------------------------------------------------------------

**j9urlGenerator**\ (nameDict=False)

**_j9SaveCurrent**\ (sDir=.)

**_getDict**\ (j9Page)

**_getCurrentj9Dict**\ ()

**updatej9DB**\ (dbname=unknown value, saveRawHTML=False)

**getj9dict**\ (dbname=unknown value, manualDB=unknown value, returnDict=both)

**addToDB**\ (abbr=None, dbname=unknown value)

**excludeFromDB**\ (abbr=None, dbname=unknown value)



**********************

journalAbbreviations.j9urlGenerator(nameDict=False)
===================================================


How to get all the urls for the WOS Journal Title Abbreviations. Each is varies by only a few characters. These are the currently in use urls they may change.

They are of the form:

| "https://images.webofknowledge.com/images/help/WOS/{VAL}_abrvjt.html"
| Where {VAL} is a capital letter or the string "0-9"

**Returns**

| ``list[str]``
| A list of all the url's strings

********************

journalAbbreviations._j9SaveCurrent(sDir=.)
===========================================


Downloads and saves all the webpages

For Backend

********************

journalAbbreviations._getDict(j9Page)
=====================================


Parses a Journal Title Abbreviations page

Note the pages are not well formatted html as the <DT> tags are not closes so html parses (Beautiful Soup) do not work. This is a simple parser that only works on the webpages and may fail if they are changed

For Backend

********************

journalAbbreviations._getCurrentj9Dict()
========================================


Downloads and parses all the webpages

For Backend

********************

journalAbbreviations.updatej9DB(dbname=unknown value, saveRawHTML=False)
========================================================================


Updates the database of Journal Title Abbreviations. Requires an internet connection. The data base is saved relative to the source file not the working directory.

**Parameters**

| *dbname:* :code:`optional [str]`
| The name of the database file, default is "j9Abbreviations.db"

| *saveRawHTML:* :code:`optional [bool]`
| Determines if the original HTML of the pages is stored, default :code:`False`. If :code:`True` they are saved in a directory inside j9Raws begining with todays date.

********************

journalAbbreviations.getj9dict(dbname=unknown value, manualDB=unknown value, returnDict=both)
=============================================================================================


Returns the dictionary of journal abbreviations mapping to a list of the associated journal names. By default the local database is used. The database is in the file *dbname* in the same directory as this source file

**Parameters**

| *dbname:* :code:`optional [str]`
| The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

| *manualDB:* :code:`optional [str]`
| The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

| *returnDict:* :code:`optional [str]`
| default:code:`'both'`, can be used to get both databases or only one  with:code:`'WOS'` or:code:`'manual'`.

********************

journalAbbreviations.addToDB(abbr=None, dbname=unknown value)
=============================================================


Adds *abbr* to the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by:code:`metaknowledge.journalAbbreviations.manualDBname`. To create an empty database run **addToDB** without an *abbr* argument.

**Parameters**

| *abbr:* :code:`optional [str or dict[str : str]]`
| The journal abbreviation to be added to the database, it can either be a single string in which case that string will be added with its self as the full name, or a dict can be given with the abbreviations as keys and their names as strings, use pipes (`'|'`) to separate multiple names. Note, if the empty string is given as a name the abbreviation will be considered manually __excluded__, i.e. having excludeFromDB() run on it.

| *dbname:* :code:`optional [str]`
| The name of the database file, default is :code:`metaknowledge.journalAbbreviations.manualDBname`.

********************

journalAbbreviations.excludeFromDB(abbr=None, dbname=unknown value)
===================================================================


Marks *abbr* to be excluded the database of journals. The database is kept separate from the one scraped from WOS, this supersedes it. The database by default is stored with the WOS one and the name is given by:code:`metaknowledge.journalAbbreviations.manualDBname`. To create an empty database run [**addToDB**\ ()](#journalAbbreviations.addToDB) without an *abbr* argument.

**Parameters**

| *abbr:* ``optional`` [str or tuple[str] or list[str]`
| The journal abbreviation to be excluded from the database, it can either be a single string in which case that string will be exclude or a list/tuple of strings can be given with the abbreviations.

| *dbname:* :code:`optional [str]`
| The name of the database file, default is :code:`metaknowledge.journalAbbreviations.manualDBname`.
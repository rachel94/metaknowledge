#####################
Citation
#####################



********************

Citations are special, here is how they are handled.

Citation

A class to hold citation strings and allow for comparison between them.

The initializer takes in a string representing a WOS citation in the form: ::

    Author, Year, Journal, Volume, Page, DOI

``Author`` is the author's name in the form of first last name first initial sometimes followed by a period.
``Year`` is the year of publication.
``Journal`` being the 29-Character Source Abbreviation of the journal.
``Volume`` is the volume number(s) of the publication preceded by a V
``Page`` is the page number the record starts on
``DOI`` is the DOI number of the cited record preceded by the letters ``'DOI'``
Combined they look like: ::

    Nunez R., 1998, MATH COGNITION, V4, P85, DOI 10.1080/135467998387343

**Note**\ : any of the fields have been known to be missing and the requirements for the fields are not always met. If something is in the source string that cannot be interpreted as any of these it is put in the `misc` attribute. That is the reason to use this class, it gracefully handles missing information while still allowing for  comparison between WOS citation strings.

Customizations
--------------

Citation's hashing and equality checking are based on `ID() <#citation-id>`__ and use the values of ``author``, ``year`` and ``journal``.

When converted to a string a Citation will return the original string.

Attributes
----------

As noted above, citations are considered to be divided into six distinct fields (``Author``, ``Year``, ``Journal``, ``Volume``, ``Page`` and ``DOI``) with a seventh ``misc`` for anything not in those. Records thus have an attribute with a name corresponding to each ``author``, ``year``, ``journal``, ``V``, ``P``, ``DOI`` and ``misc`` respectively. These are created if there is anything in the field. So a ``Citation`` created from the string: ``'Nunez R., 1998, MATH COGNITION'``` would have ``author``, ``year`` and ``journal`` defined. While one from ``'Nunez R.'``` would have only the attribute ``misc``.

If the parsing of a citation string fails the attribute ``bad`` is set to ``True`` and the attribute ``error`` is created to contain said error, which is a `BadCitation <../exceptions/index.html#badcitation-warning>`__ object. If no errors occur ``bad`` is ``False``.

The attribute ``original`` is the unmodified string (_cite_) given to create the Citation, it can also be accessed by converting to a string, e.g. with ``str()```.

\_\_Init\_\_
------------

Citations can be created by [Records](#metaknowledge.Record) or by giving the initializer a string containing a WOS style citation.

Parameters
----------

*cite*\ : ``str``

A str containing a WOS style citation.

**The Citation class has the following methods:**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Citation.isAnonymous()
=================================================

Checks if the author is given as ``'[ANONYMOUS]'`` and returns ``True`` if so.

**Returns**

``bool``

``True`` if the author is ``'[ANONYMOUS]'``` otherwise ``False``.

***********

Citation.ID()
=================================================

Returns all of ``author``, ``year`` and ``journal`` available separated by ``' ,'``. It is for shortening labels when creating networks as the resultant strings are often unique. `Extra() <#citation-extra>`__ gets everything not returned by **ID**\ ().

This is also used for hashing and equality checking.

**Returns**

``str``

A string to use as the ID of a node.

***********

Citation.allButDOI()
=================================================

Returns a string of the normalized values from the Citation excluding the DOI number. Equivalent to getting the ID with `ID() <#citation-id>`__ then appending the extra values from `Extra() <#citation-extra>`__ and then removing the substring containing the DOI number.

**Returns**

``str``

A string containing the data of the Citation.

***********

Citation.Extra()
=================================================

Returns any ``V``, ``P``, ``DOI`` or ``misc`` values as a string. These are all the values not returned by `ID() <#citation-id>`__, they are separated by ```' ,'```.

**Returns**

``str``

A string containing the data not in the ID of the ``Citation``.

***********

Citation.isJournal()
=================================================

Returns ``True`` if the ``Citation``'s ``journal`` field is a journal abbreviation from the WOS listing found at `http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html <http://images.webofknowledge.com/WOK46/help/WOS/A_abrvjt.html>`_, i.e. checks if the citation is citing a journal.

**Note**: Requires the `j9Abbreviations <../modules/journalAbbreviations.html#journalabbreviations-getj9dict>`__ database file and will raise an error if it cannot be found.

**Note**: All parameters are used for getting the data base with  `getj9dict() <../modules/journalAbbreviations.html#journalabbreviations-getj9dict>`__\ .

**Parameters**

*dbname*\ : ``optional [str]``

The name of the downloaded database file, the default is determined at run time. It is recommended that this remain untouched.

*manualDB*\ : ``optional [str]``

The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

*returnDict*\ : ``optional [str]``

default ``'both'``, can be used to get both databases or only one  with ``'WOS'`` or ``'manual'``.

**Returns**

``bool``

``True`` if the ``Citation`` is for a journal

***********

Citation.FullJournalName()
=================================================

Returns the full name of the Citation's journal field. Requires the `j9Abbreviations <../modules/journalAbbreviations.html#journalabbreviations-getj9dict>`__ database file.

**Note**\ : Requires the `j9Abbreviations <../modules/journalAbbreviations.html#journalabbreviations-getj9dict>`__ database file and will raise an error if it cannot be found.

**Returns**

``str``

The first full name given for the journal of the Citation (or the first name in the WOS list if multiple names exist), if there is not one then ``None`` is returned

***********

Citation.addToDB()
=================================================

Adds the journal of this Citation to the user created database of journals. This will cause `isJournal() <#citation-isjournal>`__ to return ``True`` for this Citation and all others with its ``journal``.

**Note**\ : Requires the `j9Abbreviations <../modules/journalAbbreviations.html#journalabbreviations-getj9dict>`__ database file and will raise an error if it cannot be found.

**Parameters**

*manualName*\ : ``optional [str]``

Default ``None``, the full name of journal to use. If not provided the full name will be the same as the abbreviation.

*manualDB*\ : ``optional [str]``

The name of the manually created database file, the default is determined at run time. It is recommended that this remain untouched.

*invert*\ : ``optional [bool]``

Default ``False``, if ``True`` the journal will be removed instead of added

***********


#####################
Medline
#####################

These are the functions used to process medline (pubmed) files at the backend. They are meant for use internal use by metaknowledge.

**The medline module provides the following functions:**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**isMedlineFile**\ (infile, checkedLines=2)

**medlineParser**\ (pubFile)

**medlineRecordParser**\ (record)

**IR**\ (val)

**FIR**\ (val)

**PROF**\ (val)

**PUBM**\ (val)

**CN**\ (val)

**MHDA**\ (val)

**LID**\ (val)

**EDAT**\ (val)

**OCI**\ (val)

**SB**\ (val)

**DA**\ (val)

**PMCR**\ (val)

**PG**\ (val)

**GS**\ (val)

**VI**\ (val)

**UOF**\ (val)

**OWN**\ (val)

**ORI**\ (val)

**MID**\ (val)

**PMID**\ (val)

**PMC**\ (val)

**RIN**\ (val)

**RPF**\ (val)

**CIN**\ (val)

**FPS**\ (val)

**TT**\ (val)

**PHST**\ (val)

**EFR**\ (val)

**PST**\ (val)

**SPIN**\ (val)

**AU**\ (val)

**FED**\ (val)

**NM**\ (val)

**SO**\ (val)

**IP**\ (val)

**OABL**\ (val)

**CRDT**\ (val)

**DDIN**\ (val)

**MH**\ (val)

**DP**\ (val)

**GN**\ (val)

**CRF**\ (val)

**TI**\ (val)

**CRI**\ (val)

**OT**\ (val)

**ROF**\ (val)

**OTO**\ (val)

**OID**\ (val)

**PT**\ (val)

**RPI**\ (val)

**AB**\ (val)

**EN**\ (val)

**AD**\ (val)

**LA**\ (val)

**TA**\ (val)

**JT**\ (val)

**IRAD**\ (val)

**PS**\ (val)

**IS**\ (val)

**PL**\ (val)

**CTI**\ (val)

**FAU**\ (val)

**VTI**\ (val)

**DCOM**\ (val)

**BTI**\ (val)

**CI**\ (val)

**STAT**\ (val)

**DRIN**\ (val)

**RF**\ (val)

**UIN**\ (val)

**LR**\ (val)

**SFM**\ (val)

**EIN**\ (val)

**AID**\ (val)

**PRIN**\ (val)

**DEP**\ (val)

**AUID**\ (val)

**SI**\ (val)

**ISBN**\ (val)

**RN**\ (val)

**JID**\ (val)

**GR**\ (val)



**********************

medline.\ **isMedlineFile**\ (infile, checkedLines=2):


Determines if *infile* is the path to a Medline file. A file is considerd to be a Medline file if it has the correct encoding (``latin-1``) and within the first *checkedLines* a line starts with ``"PMID- "``.

**Parameters**

| *infile*\ : ``str``
| The path to the targets file

| *checkedLines*\ : ``optional [int]``
| default 2, the number of lines to check for the header

**Returns**

| ``bool``
| ``True`` if the file is a Medline file

********************

medline.\ **medlineParser**\ (pubFile):


Parses a medline file, *pubFile*, to extract the individual entries as [`MedlineRecords`](#metaknowledge.MedlineRecord).

A medline file is a series of entries, each entry is a series of tags. A tag is a 2 to 4 character string each tag is padded with spaces on the left to make it 4 characters which is followed by a dash and a space (``'- '``). Everything after the tag and on all lines after it not starting with a tag is considered associated with the tag. Each entry's first tag is ``PMID``, so a first line looks something like ``PMID- 26524502``. Entries end with a single blank line.

**Parameters**

| *pubFile*\ : ``str``
| A path to a valid medline file, use [`isMedlineFile`](#metaknowledge.isMedlineFile) to verify

**Returns**

| ``set[MedlineRecord]``
| Records for each of the entries

********************

medline.\ **medlineRecordParser**\ (record):


The parser [`MedlineRecord`](#metaknowledge.MedlineRecord) use. This takes an entry from [`medlineParser()`](#metaknowledge.medlineParser) and parses it a part of the creation of a ``MedlineRecord``.

**Parameters**

| *record*\ : ``enumerate object``
| a file wrapped by ``enumerate()``

**Returns**

| ``collections.OrderedDict``
| An ordered dictionary of the key-vaue pairs in the entry

********************

medline.\ **IR**\ (val):


Investigator

********************

medline.\ **FIR**\ (val):


InvestigatorFull

********************

medline.\ **PROF**\ (val):


PartialRetractionOf

********************

medline.\ **PUBM**\ (val):


PublishingModel

********************

medline.\ **CN**\ (val):


CorporateAuthor

********************

medline.\ **MHDA**\ (val):


MeSHDate

********************

medline.\ **LID**\ (val):


LocationIdentifier

********************

medline.\ **EDAT**\ (val):


EntrezDate

********************

medline.\ **OCI**\ (val):


OtherCopyright

********************

medline.\ **SB**\ (val):


Subset

********************

medline.\ **DA**\ (val):


DateCreated

********************

medline.\ **PMCR**\ (val):


PubMedCentralRelease

********************

medline.\ **PG**\ (val):


Pagination
all pagination seen so far seems to be only on one line

********************

medline.\ **GS**\ (val):


GeneSymbol

********************

medline.\ **VI**\ (val):


Volume
The volumes as a string as volume is single line

********************

medline.\ **UOF**\ (val):


UpdateOf

********************

medline.\ **OWN**\ (val):


Owner

********************

medline.\ **ORI**\ (val):


OriginalReportIn

********************

medline.\ **MID**\ (val):


ManuscriptIdentifier

********************

medline.\ **PMID**\ (val):


PubMedUniqueIdentifier

********************

medline.\ **PMC**\ (val):


PubMedCentralIdentifier

********************

medline.\ **RIN**\ (val):


RetractionIn

********************

medline.\ **RPF**\ (val):


RepublishedFrom

********************

medline.\ **CIN**\ (val):


CommentIn

********************

medline.\ **FPS**\ (val):


FullPersonalNameSubject

********************

medline.\ **TT**\ (val):


TransliteratedTitle

********************

medline.\ **PHST**\ (val):


PublicationHistoryStatus

********************

medline.\ **EFR**\ (val):


ErratumFor

********************

medline.\ **PST**\ (val):


PublicationStatus

********************

medline.\ **SPIN**\ (val):


SummaryForPatients

********************

medline.\ **AU**\ (val):


Author

********************

medline.\ **FED**\ (val):


Editor

********************

medline.\ **NM**\ (val):


SubstanceName

********************

medline.\ **SO**\ (val):


Source

********************

medline.\ **IP**\ (val):


Issue

********************

medline.\ **OABL**\ (val):


OtherAbstract

********************

medline.\ **CRDT**\ (val):


CreateDate

********************

medline.\ **DDIN**\ (val):


DatasetIn

********************

medline.\ **MH**\ (val):


MeSHTerms

********************

medline.\ **DP**\ (val):


DatePublication

********************

medline.\ **GN**\ (val):


GeneralNote

********************

medline.\ **CRF**\ (val):


CorrectedRepublishedFrom

********************

medline.\ **TI**\ (val):


Title
only one per record

********************

medline.\ **CRI**\ (val):


CorrectedRepublishedIn

********************

medline.\ **OT**\ (val):


OtherTerm
Nothing needs to be done

********************

medline.\ **ROF**\ (val):


RetractionOf

********************

medline.\ **OTO**\ (val):


OtherTermOwner
one line field

********************

medline.\ **OID**\ (val):


OtherID

********************

medline.\ **PT**\ (val):


PublicationType

********************

medline.\ **RPI**\ (val):


RepublishedIn

********************

medline.\ **AB**\ (val):


Abstract
basically a one liner after parsing

********************

medline.\ **EN**\ (val):


Edition

********************

medline.\ **AD**\ (val):


Affiliation
Undoing what the parser does then splitting at the semicolons and dropping newlines extra fitlering is required beacuse some AD's end with a semicolon

********************

medline.\ **LA**\ (val):


Language

********************

medline.\ **TA**\ (val):


JournalTitleAbbreviation
One line only

********************

medline.\ **JT**\ (val):


JournalTitle
One line only

********************

medline.\ **IRAD**\ (val):


InvestigatorAffiliation

********************

medline.\ **PS**\ (val):


PersonalNameSubject

********************

medline.\ **IS**\ (val):


ISSN

********************

medline.\ **PL**\ (val):


PlacePublication

********************

medline.\ **CTI**\ (val):


CollectionTitle

********************

medline.\ **FAU**\ (val):


FullAuthor

********************

medline.\ **VTI**\ (val):


VolumeTitle

********************

medline.\ **DCOM**\ (val):


DateCompleted

********************

medline.\ **BTI**\ (val):


BookTitle

********************

medline.\ **CI**\ (val):


CopyrightInformation

********************

medline.\ **STAT**\ (val):


Status

********************

medline.\ **DRIN**\ (val):


DatasetUseReportedIn

********************

medline.\ **RF**\ (val):


NumberReferences

********************

medline.\ **UIN**\ (val):


UpdateIn

********************

medline.\ **LR**\ (val):


DateLastRevised

********************

medline.\ **SFM**\ (val):


SpaceFlightMission

********************

medline.\ **EIN**\ (val):


ErratumIn

********************

medline.\ **AID**\ (val):


ArticleIdentifier
The given values do not require any work

********************

medline.\ **PRIN**\ (val):


PartialRetractionIn

********************

medline.\ **DEP**\ (val):


DateElectronicPublication

********************

medline.\ **AUID**\ (val):


AuthorIdentifier
one line only just need to undo the parser's effects

********************

medline.\ **SI**\ (val):


SecondarySourceID

********************

medline.\ **ISBN**\ (val):


ISBN

********************

medline.\ **RN**\ (val):


RegistryNumber

********************

medline.\ **JID**\ (val):


NLMID

********************

medline.\ **GR**\ (val):


GrantNumber
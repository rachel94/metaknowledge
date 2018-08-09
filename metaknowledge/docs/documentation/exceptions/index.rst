#####################
Exceptions
#####################

The exceptions defined by *metaknowledge* are:

********************

**mkException**\ (*Exception*)

********************

**CollectionTypeError**\ (*mkException*, *TypeError*\ )

********************

**RCTypeError**\ (*mkException*, *TypeError*\ )

********************

**TagError**\ (*mkException*)

********************

**RCValueError**\ (*mkException*)

********************

**BadInputFile**\ (*mkException*)

********************

**BadRecord**\ (*mkException*)

********************

**BadPubmedRecord**\ (*mkException*)

********************

**BadPubmedFile**\ (*mkException*)

********************

**BadScopusRecord**\ (*mkException*)

********************

**BadScopusFile**\ (*mkException*)

********************

**BadProQuestRecord**\ (*mkException*)

********************

**BadProQuestFile**\ (*mkException*)

********************

**RecordsNotCompatible**\ (*mkException*)

********************

**JournalDataBaseError**\ (*mkException*)

********************

**GenderException**\ (*mkException*)

********************

**cacheError**\ (*mkException*)

Exception raised when loading a cached RecordCollection fails, should only be seen inside metaknowledge and always be caught.

********************

**BadWOSRecord**\ (*BadRecord*)

Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

    * *Missing field on line (line Number):(line)*\ , which indicates a line was to short, there should have been a tag followed by information

    * *End of file reached before ER*, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

    * *Duplicate tags in record*, which indicates the record had 2 or more lines with the same tag.

    * *Missing WOS number*, which indicates the record did not have a 'UT' tag.

Records with a BadWOSRecord error are likely incomplete or the combination of two or more single records.

********************

**BadWOSFile**\ (*Warning*)

Exception thrown by wosParser for mis-formatted files
    

********************

**BadCitation**\ (*Warning*)

Exception thrown by Citation

********************

**BadGrant**\ (*mkException*)

********************

**GrantCollectionException**\ (*mkException*)

********************

**UnknownFile**\ (*mkException*)
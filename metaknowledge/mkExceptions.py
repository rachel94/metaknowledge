class mkException(Exception):
    pass

class CollectionTypeError(mkException, TypeError):
    pass

class RCTypeError(mkException, TypeError):
    pass

class TagError(mkException):
    pass

class RCValueError(mkException):
    pass

class BadInputFile(mkException):
    pass

class BadRecord(mkException):
    pass

class BadPubmedRecord(mkException):
    pass

class BadPubmedFile(mkException):
    pass

class BadScopusRecord(mkException):
    pass

class BadScopusFile(mkException):
    pass

class BadProQuestRecord(mkException):
    pass

class BadProQuestFile(mkException):
    pass

class RecordsNotCompatible(mkException):
    pass

class JournalDataBaseError(mkException):
    pass

class GenderException(mkException):
    pass

class cacheError(mkException):
    """Exception raised when loading a cached RecordCollection fails, should only be seen inside metaknowledge and always be caught."""
    pass

class BadWOSRecord(BadRecord):
    """Exception thrown by the [record parser](#metaknowledge.recordParser) to indicate a mis-formated record. This occurs when some component of the record does not parse. The messages will be any of:

        * *Missing field on line (line Number):(line)*\ , which indicates a line was to short, there should have been a tag followed by information

        * *End of file reached before ER*, which indicates the file ended before the 'ER' indicator appeared, 'ER' indicates the end of a record. This is often due to a copy and paste error.

        * *Duplicate tags in record*, which indicates the record had 2 or more lines with the same tag.

        * *Missing WOS number*, which indicates the record did not have a 'UT' tag.

    Records with a BadWOSRecord error are likely incomplete or the combination of two or more single records.
    """
    pass

class BadWOSFile(Warning):
    """Exception thrown by wosParser for mis-formatted files
    """
    pass

class BadCitation(Warning):
    """
    Exception thrown by Citation
    """
    pass

class BadGrant(mkException):
    pass


class GrantCollectionException(mkException):
    pass

class UnknownFile(mkException):
    pass

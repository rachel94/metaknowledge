WOSRecord(ExtendedRecord) – the object for containing and processing WOS entries <WOSRecord>
Citation(Hashable) – citations are special, here is how they are handled <Citation>
GrantCollection(CollectionWithIDs) – a collection of Grants, this is what does most of the stuff on Grants <GrantCollection>
FallbackGrant(Grant) – the Grant used if a file was not identifiable <FallbackGrant>
Grant(Record, MutableMapping) – the base for all other Grants <Grant>
CIHRGrant(Grant) – the container for CIHR grant entires <CIHRGrant>
MedlineGrant(Grant) – the container for grants derived from Medline Records entries <MedlineGrant>
NSERCGrant(Grant) – the container for NSERC grant entries <NSERCGrant>
NSFGrant(Grant) – the container for NSF grant entries <NSFGrant>
MedlineRecord(ExtendedRecord) – the object for containing and processing Medline entries <MedlineRecord>
Collection(MutableSet, Hashable) – the base of all other Collections, basically a set <Collection>
CollectionWithIDs(Collection) – a Collection that only holds metaknowledge objects <CollectionWithIDs>
ExtendedRecord(Record) – a Record that processes its contents before returning them <ExtendedRecord>
Record(Mapping, Hashable) – the base of all the other Records, basically a dict <Record>
ProQuestRecord(ExtendedRecord) – the object for containing and processing ProQuest entries <ProQuestRecord>
RecordCollection(CollectionWithIDs) – a Collection of Records, this is what does most of the stuff on Records <RecordCollection>
ScopusRecord(ExtendedRecord) – the object for containing and processing Scopus entries <ScopusRecord>

contour – a nicer matplotlib graph visualizer and contour plot <contour>
journalAbbreviations – handles the abbreviated journal names used by WOS <journalAbbreviations>
medline – the backend functions and classes associated with Medline, the format used by Pubmed <medline>
proquest – the backend functions and classes associated with ProQuest <proquest>
scopus – the backend functions and classes associated with records from Scopus <scopus>
WOS – the backend functions and classes associated with the Web of Science <WOS>

import typing
import error
class Field(object):
    Header = dict()
    None_Helper_Method = ['Comment len','File name length','Extra field length','File comm. len']
class End_Of_Central_Directory_Header(Field):
    def __init__(self):
        self.Header = {
            'Signature' : ["The signature of end of central directory record. This is always '\x50\x4b\x05\x06'.",4],
            'Disk Number' : ["The number of this disk (containing the end of central directory record)",2],
            'Disk # w/cd' : ["Number of the disk on which the central directory starts",2],
            'Disk entries' : ["The number of central directory entries on this disk",2],
            'Total entries' : ["Total number of entries in the central directory.",2],
            'Central directory size' : ["Size of the central directory in bytes",4],
            'Offset of cd wrt to starting disk' : ["Offset of the start of the central directory on the disk on which the central directory starts",4],
            'Comment len' : ["The length of the following comment field",2],
            'ZIP file comment' : ["Optional comment for the Zip file",None]
        }
class Central_Directory_Header(Field):
    def __init__(self):
        self.Header = {
            'Signature' : ["The signature of the file header. This is always '\x50\x4b\x01\x02'.",4],
            'Version' : ["Version made by:\n\nupper byte: \n0 - MS-DOS and OS/2 (FAT / VFAT / FAT32 file systems)\n1 - Amiga \n2 - OpenVMS\n3 - UNIX \n4 - VM/CMS\n5 - Atari ST\n6 - OS/2 H.P.F.S.\n7 - Macintosh \n8 - Z-System\n9 - CP/M \n10 - Windows NTFS\n11 - MVS (OS/390 - Z/OS) \n12 - VSE\n13 - Acorn Risc \n14 - VFAT\n15 - alternate MVS \n16 - BeOS\n17 - Tandem \n18 - OS/400\n19 - OS/X (Darwin) \n20 - 255: unused\n\nlower byte:\nzip specification version",2],
            'Vers. needed' : ["PKZip version needed to extract",2],
            'Flags' : ["General purpose bit flag:\nBit 00: encrypted file\nBit 01: compression option \nBit 02: compression option \nBit 03: data descriptor\nBit 04: enhanced deflation\nBit 05: compressed patched data\nBit 06: strong encryption\nBit 07-10: unused\nBit 11: language encoding\nBit 12: reserved\nBit 13: mask header values\nBit 14-15: reserve",2],
            'Compression method' : ["00: no compression\n01: shrunk\n02: reduced with compression factor 1\n03: reduced with compression factor 2 \n04: reduced with compression factor 3 \n05: reduced with compression factor 4 \n06: imploded\n07: reserved\n08: deflated\n09: enhanced deflated\n10: PKWare DCL imploded\n11: reserved\n12: compressed using BZIP2\n13: reserved\n14: LZMA\n15-17: reserved\n18: compressed using IBM TERSE\n19: IBM LZ77 z\n98: PPMd version I, Rev 1 ",2],
            'File modification time' : ["stored in standard MS-DOS format:\nBits 00-04: seconds divided by 2 \nBits 05-10: minute\nBits 11-15: hour",2],
            'File modification date' : ["stored in standard MS-DOS format:\nBits 00-04: day\nBits 05-08: month\nBits 09-15: years from 1980",2],
            'Crc-32 checksum' : ["value computed over file data by CRC-32 algorithm with 'magic number' 0xdebb20e3 (little endian)",4],
            'Compressed size' : ["if archive is in ZIP64 format, this filed is 0xffffffff and the length is stored in the extra field",4],
            'Uncompressed size' : ["if archive is in ZIP64 format, this filed is 0xffffffff and the length is stored in the extra field",4],
            'File name length' : ["the length of the file name field below",2],
            'Extra field length' : ["the length of the extra field below",2],
            'File comm. len' : ["he length of the file commen",2],
            'Disk # start' : ["the number of the disk on which this file exists",2],
            'Internal attr' : ["Internal file attributes:\nBit 0: apparent ASCII/text file\nBit 1: reserved\nBit 2: control field records precede logical records\nBits 3-16: unused",2],
            'External attr' : ["xternal file attributes:\nhost-system dependent",4],
            'Offset of local header' : ["Relative offset of local header. This is the offset of where to find the corresponding local file header from the start of the first disk.",4],
            'File name' : ["the name of the file including an optional relative path. All slashes in the path should be forward slashes '/'.",None],
            'Extra field' : ["Used to store additional information. The field consistes of a sequence of header and data pairs, where the header has a 2 byte identifier and a 2 byte data size field.",None],
            'File comment' : ["An optional comment for the file.",None]
        }
class Local_File_Header(Field):
    def __init__(self):
        self.Header = {
            'Signature' : ["The signature of the local file header. This is always '\x50\x4b\x03\x04'.",4],
            'Version' : ['PKZip version needed to extract',2],
            'Flags' : ["General purpose bit flag:\nBit 00: encrypted file\nBit 01: compression option \nBit 02: compression option \nBit 03: data descriptor\nBit 04: enhanced deflation\nBit 05: compressed patched data\nBit 06: strong encryption\nBit 07-10: unused\nBit 11: language encoding\nBit 12: reserved\nBit 13: mask header values\nBit 14-15: reserved",2],
            'Compression method' : ["00: no compression\n01: shrunk\n02: reduced with compression factor 1\n03: reduced with compression factor 2 \n04: reduced with compression factor 3 \n05: reduced with compression factor 4 \n06: imploded\n07: reserved\n08: deflated\n09: enhanced deflated\n10: PKWare DCL imploded\n11: reserved\n12: compressed using BZIP2\n13: reserved\n14: LZMA\n15-17: reserved\n18: compressed using IBM TERSE\n19: IBM LZ77 z\n98: PPMd version I, Rev 1",2],
            'File modification time' : ["tored in standard MS-DOS format:\nBits 00-04: seconds divided by 2 \nBits 05-10: minute\nBits 11-15: hour",2],
            'File modification date' : ["stored in standard MS-DOS format:\nBits 00-04: day\nBits 05-08: month\nBits 09-15: years from 1980",2],
            'Crc-32 checksum' : ["value computed over file data by CRC-32 algorithm with 'magic number' 0xdebb20e3 (little endian)",4],
            'Compressed size' : ["if archive is in ZIP64 format, this filed is 0xffffffff and the length is stored in the extra field",4],
            'Uncompressed size' : ["if archive is in ZIP64 format, this filed is 0xffffffff and the length is stored in the extra field",4],
            'File name length' : ['the length of the file name field below',2],
            'Extra field length' : ['the length of the extra field below',2],
            'File name' : ["the name of the file including an optional relative path. All slashes in the path should be forward slashes '/'.",None],
            'Extra field' : ["Used to store additional information. The field consistes of a sequence of header and data pairs, where the header has a 2 byte identifier and a 2 byte data size field.",None]
        }
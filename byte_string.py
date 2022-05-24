class byte_decoding(object):
    def __init__(self,data):
        self.data = data
    def decodeing(self,deformat='ascii'):
        i=0
        string = ''
        while i<len(self.data):
            data = ord(self.data[i:i+1])
            if data>=0x20 and data<=0x7E:
                string+=self.data[i:i+1].decode(deformat)
            else:
                string+='.'
            i+=1
        return string
    def hex_split(self):
        hex_string = []
        temp  = self.data.hex().upper()
        i=0
        while i<len(temp):
            hex_string.append(temp[i:i+4])
            i+=4
        return hex_string
import os
import sys
import error
import data_struct
import byte_string
class ZIP_View(object):
    signature = {'end_of_central_directory':b'PK\x05\x06','central_directory':b'PK\x01\x02','local_header':b'PK\x03\x04'}
    def __init__(self,file_name,root=os.getcwd()):
        print("{0}ZIP File View{0}".format("="*20))
        print("[INFO]\t파일을 읽는 중 입니다.")
        with open(root+os.sep+str(file_name),'rb') as f:
            data = f.read()
        if data[:4] != self.signature['local_header']:
            raise error.Zip_File_Read_Error
        self.name = file_name
        self.Data = data
        self.End_Of_Central_Directory = None
        self.Central_Directory = list()
        self.Local_Header = []
        self.File_Data = []
        self.End_Of_Central_Directory_Split = data_struct.End_Of_Central_Directory_Header()
        self.Central_Directory_Split = []
        self.Local_File_Split = []
        self.version = 1.0
        self.Read_End_Of_Central_Directory()
        self.Read_Central_Directory()
        self.Read_Local_Header()
        self.mode='Print'
        self.ascii = byte_string.byte_decoding(self.Data).decodeing()
        self.hex = ' '.join(byte_string.byte_decoding(self.Data).hex_split())
    def Read_End_Of_Central_Directory(self):
        print("[INFO]\tEnd Of Central Directory을 읽는중 입니다.")
        i=len(self.Data)-1
        while True:
            if i<0:
                raise error.End_Of_Central_Directory_Read_Error
            if self.Data[i:i+1] == b'P' and self.Data[i:i+4] == self.signature['end_of_central_directory']:
                self.End_Of_Central_Directory = self.Data[i:]
                break
            i-=1
        self.Data_Split(self.End_Of_Central_Directory,self.End_Of_Central_Directory_Split)
        print("[INFO]\tEnd of Central Directory을 읽기에 성공 했습니다.")
        return 1
    def Read_Central_Directory(self):
        print("[INFO]\tCentral Directory을 읽는중 입니다.")
        offset = int.from_bytes(self.End_Of_Central_Directory_Split.Header['Offset of cd wrt to starting disk'][2],'little')
        Size_of_Cetrnal_Directory = int.from_bytes(self.End_Of_Central_Directory_Split.Header['Central directory size'][2],'little')
        self.Central_Directory = self.Data[offset:Size_of_Cetrnal_Directory+offset]
        temp_list = []
        Read_len = 0
        while Read_len<Size_of_Cetrnal_Directory:
            temp = data_struct.Central_Directory_Header()
            temp_data = self.Data[offset+Read_len:Size_of_Cetrnal_Directory+offset]
            if temp_data[:4] != self.signature['central_directory']:
                raise error.entral_Directory_Read_Error
            Read_len += self.Data_Split(temp_data,temp)
            self.Central_Directory_Split.append(temp)
        print("[INFO]\tCentral Directory을 읽기에 성공 했습니다.")
        print("[INFO]\tCentral Directory의 개수 : {}".format(len(self.Central_Directory_Split)))
        return 1
    def Read_Local_Header(self):
        print("[INFO]\tLocal Header을 읽는중 입니다.")
        i=len(self.Central_Directory_Split)-1
        Read_len = temp_data = int.from_bytes(self.End_Of_Central_Directory_Split.Header['Offset of cd wrt to starting disk'][2],'little')
        while i>=0:
            offset = int.from_bytes(self.Central_Directory_Split[i].Header['Offset of local header'][2],'little')
            data_len = int.from_bytes(self.Central_Directory_Split[i].Header['Compressed size'][2],'little')
            temp = data_struct.Local_File_Header()
            temp_data = self.Data[offset:Read_len]
            if temp_data[:4] != self.signature['local_header']:
                raise error.Local_Header_Read_Error
            Read_len -= self.Data_Split(temp_data,temp)
            self.Local_File_Split.append(temp)
            i-=1
        print("[INFO]\tLocal Header을 읽기에 성공 했습니다.")
        print("[INFO]\tLocal Header의 개수 : {}".format(len(self.Local_File_Split)))
        return 1
    def Data_Split(self,Data,class_):
        temp = class_.None_Helper_Method
        i = 0
        test = []
        for Field,list_ in class_.Header.items():
            if list_[1] == None:
                class_.Header[Field][1] = test.pop(0)
            class_.Header[Field].append(Data[i:i+list_[1]])
            if Field in temp:
                test.append(int.from_bytes(class_.Header[Field][2],'little'))
            i+=list_[1]
        return i

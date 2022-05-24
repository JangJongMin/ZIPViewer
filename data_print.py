from data_read import *

class print_file_info(ZIP_View):
        def main(self):
            if len(self.Local_File_Split) != len(self.Central_Directory_Split):
                raise error.Zip_File_Read_Error
            str_format='%-10s%-20s%-20s\n'
            main = str_format%("[SELECT]","1.전체 보기 (Hex,Ascii)","2.전체 보기(Ascii)")
            main += str_format%("[SELECT]","3.전체 보기(Hex)","4.구조체 설명")
            main += str_format%("[SELECT]","5.자세히 보기","6.반환 형식 변경")
            main += str_format%("[SELECT]","7.프로그램 설명",'8.종료')
            while True:
                print("="*50)
                print("\n{:<10}[{}]\n[FILE] ZIP 파일의 이름 :{:>20}".format("[Main]",self.mode,self.name))
                print("[FILE] ZIP 파일의 크기 :{0:>20}".format(str(len(self.Data))+" Byte"))
                print(main)
                select = int(input("Enter : "))
                if select==8:
                    print("프로그램을 종료 합니다.")
                    exit()
                elif select==7:
                    strout="[INFO]이 프로그램은 공부 목적으로 제작 되었습니다.\n"
                    strout+="[INFO]프로그램 이름 : ZIPView\n"
                    strout+="[INFO]제작자 : NOP\n"
                    strout+="[INFO]제작자 블로그 : https://nooperation.tistory.com\n"
                    strout+="[INFO]프로그램 버전 : {}\n".format(self.version)
                elif select>=1 and select<=3:
                    strout = self.basic_strout(self.Data,self.hex,self.ascii,select)
                elif select==4:
                    strout = self.struct()
                elif select==5:
                    strout = self.detail()
                elif select==6:
                    if self.mode=='TXT':
                        strout = self.change_mode("Print")
                        print("반환 모드가 Print로 변경 되었습니다.")
                    elif self.mode=="Print":
                        strout = self.change_mode("TXT")
                        print("반환 모드가 TXT로 변경 되었습니다.")
                    continue
                if strout!=1:
                    self.last_return(strout)
                else:
                    continue
        def basic_strout(self,offset,hex_string,ascii_string,select):
            if select==1:
                str_format='{:<8}    {:<43}{:<20}\n'
                strout = str_format.format("OFFSET","HEX","ASCII")
                str_format='{:0>8}    {:<43}{:<20}\n'
            if select==2:
                str_format='{:<8}    {:<20}\n'
                strout = str_format.format("OFFSET","ASCII")
                str_format='{:0>8}    {:<20}\n'
            if select==3:
                str_format='{:<8}    {:<43}\n'
                strout = str_format.format("OFFSET","HEX")
                str_format='{:0>8}    {:<43}\n'
            i=0
            count = 0
            while i<len(offset):
                if select==1:
                    strout += str_format.format(hex(i)[2:],hex_string[i*2+count*8:(i+16)*2+(count+1)*8],ascii_string[i:i+16])
                elif select==2:
                    strout += str_format.format(hex(i)[2:],ascii_string[i:i+16])
                elif select==3:
                    strout += str_format.format(hex(i)[2:],hex_string[i*2+count*8:(i+16)*2+(count+1)*8])
                i+=16
                count+=1
            return strout
        def struct(self):
            str_format='%-10s%-30s\t%-20s\n'
            main = "\n{:<10}[{}]\n".format("[Struct]",self.mode)
            main += str_format%("[SELECT]","1.전체 보기","2.End Of Central Directory 구조체 보기")
            main += str_format%("[SELECT]","3.Central Directory 구조체 보기","4.Local Header 구조체 보기")
            main += str_format%("[SELECT]","5.메인으로 나가기",'6.종료')
            while True:
                print("="*50)
                print(main)
                select = int(input("Enter : "))
                if select==6:
                    print("프로그램을 종료합니다.")
                    exit()
                elif select==5:
                    return 1
                elif select>=1 and select <=5:
                    strout = self.struct_strout(select)
                self.last_return(strout)
        def struct_strout(self,select):
            str_format='{:<10}{:<10}\n{}\n'
            strout=''
            if select==2 or select==1:
                strout+=("="*20+"[End of Central Directory]"+'='*20+'\n')
                for i,k in self.End_Of_Central_Directory_Split.Header.items():
                    strout += str_format.format("[INFO]","[NAME] : "+i,"[EXPLANATION] : "+k[0])
            if select==3 or select==1:
                strout+=("="*20+"[Central Directory]"+'='*20+'\n')
                for i,k in self.Central_Directory_Split[0].Header.items():
                    strout += str_format.format("[INFO]","[NAME] : "+i,"[EXPLANATION] : "+k[0])
            if select==4 or select==1:
                strout+=("="*20+"[Local File Header]"+'='*20+'\n')
                for i,k in self.Local_File_Split[0].Header.items():
                    strout += str_format.format("[INFO]","[NAME] : "+i,"[EXPLANATION] : "+k[0])
            return strout
        def detail(self):
            str_format='%-10s%-30s\t%-20s\n'
            main = "\n{:<10}[{}]\n".format("[Deetail]",self.mode)
            main += str_format%("[SELECT]","1.전체 보기","2.End Of Central Directory 자세히 보기")
            main += str_format%("[SELECT]","3.Central Directory 자세히 보기","4.Local Header 자세히 보기")
            main += str_format%("[SELECT]","5.메인으로 나가기",'6.종료')
            while True:
                print("="*50)
                print(main)
                select = int(input("Enter : "))
                if select==6:
                    print("프로그램을 종료합니다.")
                    exit()
                elif select==5:
                    return 1
                elif select>=1 and select <=5:
                    strout = self.detail_strout(select)
                self.last_return(strout)
        def detail_strout(self,select):
            str_format='{:<10}{:<10}\n{:<10}\t{:<10}\t{:<10}\n'
            strout=''
            if select==2 or select==1:
                strout+=("="*20+"[End of Central Directory]"+'='*20+'\n')
                for i,k in self.End_Of_Central_Directory_Split.Header.items():
                    strout += str_format.format("[INFO]","[NAME] : "+i,"[VALUSE(ASCII)] : "+byte_string.byte_decoding(k[2]).decodeing(),"[VALUSE(HEX)] : "+k[2].hex(),"[VALUSE(BYTE)] : "+str(k[2]))
            if select==3 or select==1:
                strout+="Central Directory의 개수 : "+str(len(self.Central_Directory_Split))+"\n"
                for n in range(len(self.Central_Directory_Split)):
                    strout+=("\n"+"="*20+"[Central Directory]["+str(n+1)+"]"+'='*20+'\n')
                    for i,k in self.Central_Directory_Split[n].Header.items():
                        strout += str_format.format("[INFO]","[NAME] : "+i,"[VALUSE(ASCII)] : "+byte_string.byte_decoding(k[2]).decodeing(),"[VALUSE(HEX)] : "+k[2].hex(),"[VALUSE(BYTE)] : "+str(k[2]))
            if select==4 or select==1:
                strout+=("\n"+"="*20+"[Local File Header]"+'='*20+'\n')
                for i,k in self.Local_File_Split[0].Header.items():
                    strout += str_format.format("[INFO]","[NAME] : "+i,"[VALUSE(ASCII)] : "+byte_string.byte_decoding(k[2]).decodeing(),"[VALUSE(HEX)] : "+k[2].hex(),"[VALUSE(BYTE)] : "+str(k[2]))
            return strout
        def change_mode(self,mode):
            self.mode = mode
            return 1
        def last_return(self,strout):
            if self.mode=="TXT":
                file_name = input("생성할 파일 이름을 입력해 주세요 : ")
                with open(file_name,'w') as f:
                    f.write(strout)
                print("파일에 정삭적으로 작성 되었습니다.")
            elif self.mode=="Print":
                print(strout)
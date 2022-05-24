class End_Of_Central_Directory_Read_Error(Exception):
    def __init__(self):
        super().__init__('End_Of_Central_Directory를 찾지 못 했습니다.')
class Central_Directory_Read_Error(Exception):
    def __init__(self):
        super().__init__('Central_Directory를 찾지 못 했습니다.')
class Local_Header_Read_Error(Exception):
    def __init__(self):
        super().__init__('Local_Header를 찾지 못 했습니다.')
class Zip_File_Read_Error(Exception):
    def __init__(self):
        super().__init__('ZIP파일이 아니거나 읽는데 오류가 발생 했습니다.')
class Invalid_Argument_Passed(Exception):
    def __init__(self):
        super().__init__('잘못된 인자를 전달하셨습니다.')
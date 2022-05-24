import data_print

print("경로를 입력해 주세요 (미입력시 현재 디렉토리 기준)")
root = input("Enter : ")
print("파일 이름을 입략해 주세요 ")
file_name = input("Enter : ")
if root:
    info = data_print.print_file_info(file_name,root)
else:
    info = data_print.print_file_info(file_name)
info.main()
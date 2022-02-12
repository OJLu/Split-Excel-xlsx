###########以下参数不可修改################
import pandas as pd
import os
from datetime import datetime

from config import xlsx_file_name, sheet_name, split_list

split_list_num=len(split_list)

def save_to_xlsx(df):
    dest_file_name=''
    for i in range(0,split_list_num-1):
        dest_file_name += df.iloc[0][split_list[i]]+'+'
    dest_file_name += df.iloc[0][split_list[split_list_num-1]]
    writer=pd.ExcelWriter(dir_name+"/"+dest_file_name+".xlsx")
    df.to_excel(writer,'Sheet1')
    writer.save()
    print(dest_file_name+".xlsx 已生成\n")

if __name__ == '__main__':
    try:
        frame = pd.read_excel(pd.ExcelFile(xlsx_file_name), sheet_name)
    except:
        print("打开xlsx文件错误。请检查文件名和表格名是否正确。")
        exit(1)
  
    dir_name=xlsx_file_name+'_'+sheet_name+'_'+datetime.now().strftime("%Y%m%d_%H%M%S")
    os.mkdir(dir_name)
    group = frame.groupby(split_list).apply(save_to_xlsx)
    print("\n拆分已完成，文件存储在文件夹"+dir_name)
#####################1.参数名称不可修改#################

#################2.表格第一行应当是各列标签##############

######3.合并的单元格应当拆分并使每一个单元格中都有对应值#######

#####4. v1.0仅支持单文件单表拆分，如有多表需求下个版本更#######


#####################下面是参数########################

#输入本程序的xlsx文件名
xlsx_file_name = '1.xlsx'

#上面xlsx文件下的表名
sheet_name = 'Sheet1'

#需要进行拆分的列名，格式为：['列名1','列名2',.....,'列名n']，注意最后一个关键字前无逗号，列名不要含有特殊字符
split_list=['A', 'B']


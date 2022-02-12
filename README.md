#脚本功能：根据列中元素的值，拆分Excel xlsx文件，并将拆分结果存入多个新的xlsx文件中
#例如：
  A B C\n
  1 2 3
  1 2 4
  1 3 4
  1 3 5
  2 3 4
#按AB两列拆分，则得到1+2.xlsx,1+3.xlsx,2+3.xlsx

#运行环境：Windows系统，Python 3.7

#运行方法：
#1.安装Python3.7
#2.点击运行install.bat，安装依赖包
#3.将待拆分的表格放到代码所在目录下，默认为1.xlsx, Sheet1
#4.在config.py中更改参数
#5.点击运行start.bat
#6.拆分结果在代码所在目录下

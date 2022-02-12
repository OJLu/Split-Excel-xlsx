title Install python env
@echo =======  Installing python environment =========

pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install xlrd
pip install openpyxl

@echo ===== Press any key to exit ======
@pause >nul
exit
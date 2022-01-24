#-*- codeing = utf-8 -*-
#@Author: Fyf

import xlwt
from xlwt.Workbook import Workbook

wookbook = xlwt.Workbook(encoding="utf-8")

worksheet = wookbook.add_sheet("sheet1")

worksheet.write(0, 0, 'hello')
wookbook.save("xlwt_practice.xls")

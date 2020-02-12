# -*- coding: utf-8 -*-
import xlrd
import xlsxwriter
def file_iterator(file_name, chunk_size=512):
    with open(file_name,'rb') as f:
        while True:
            c = f.read(chunk_size)
            if not c:
                break
            yield c
            
# 列表保存为电子表格。data形如[['data1',...],['data1',...],...]数据 , headings电子表格标题，电子表格标题栏，与数据库字段保持一致。参见models.py Order数据库字段； filePath文件路径
def ListToXlsx(data, headings, filePath):
    ret = True
    try:
        A = 65 # 'A'
        workbook = xlsxwriter.Workbook(filePath)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': 1})  #如何控制单元格宽度？  
        worksheet.write_row('A1', headings, bold)
        for n in range(len(headings)):
            worksheet.write_column(chr(A + n) +'2', data[n])
        workbook.close() 
    except Exception as _e:       
        ret = False    
    return ret 

#xls表转换成列表 [[第一行元素],[第二行元素],...] 工程还未用
def XlsxToList(filename_xls):
    try:
        table = xlrd.open_workbook(filename_xls)#创建一个book class，打开excel文件
        sh = table.sheet_by_index(0) #获取一个sheet对象
        for line in range(0,sh.nrows):#0-含第一行。nrows = table.nrows #行数 ncols = table.ncols #列数 print sh.row_values(rownum)
            row = sh.row_values(line)
            yield [r for r in row]
    except Exception as ex:
        print('Error execute: {}'.format(ex))
        yield []

import unittest            
class TestfileAPI(unittest.TestCase):        
    def test_XlsxToList(self):
        self.assertEquals(list(XlsxToList("testMyFile/xfile.xls")),[[1.0, u'name', u'password'], [2.0, u'admin', u'admin@1234'], [3.0, u'wcl6005', u'wcl6005@1234'], [4.0, u'wj', u'wj@1234']])

if __name__ == '__main__':
    unittest.main()  
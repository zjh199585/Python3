#  将数据写入新文件
import xlwt

def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    
    #将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i,j,data[j])
        i = i + 1
        
    f.save(file_path) #保存文件
a=[2,2,4,5,4,8,5,3,4,1]
data_write('/Users/zhuji/Desktop/Python/twitter.txt',a)

#将列表写入 TXT
def text_save(filename, data):#filename为写入文件路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功") 

#将列表写入 CSV
import csv
import codecs

def data_write_csv(filename, datas):#file_name为写入CSV文件的路径，datas为要写入数据列表
    file_csv = codecs.open(filename,'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(data)
    print("保存文件成功")
           
#将列表存入 Excel
import xlwt

def data_write(file_path, datas): #  将数据写入新文件
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    
    #将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i,j,data[j])
        i = i + 1
        
    f.save(file_path) #保存文件
    print('保存文件成功')

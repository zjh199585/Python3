def txt_reading1(txt):                   # txt为带读取文件地址

    with open(txt,'r') as f:
        line = f.readlines()            # 完成列表载入，但是每个项后会存在 '\n'

                  # 完成所有元素末尾 '\n' 的消除
    
    print(line)
txt_reading1('/Users/zhuji/Desktop/Python/massage.txt')
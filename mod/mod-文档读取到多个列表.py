def txt_read(txt):

    with open(txt,'r') as f:
        line = f.readline().strip()
        while line:
            linestr = line.split(" ")
            print(linestr)       
            line = f.readline().strip()


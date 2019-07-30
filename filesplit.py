import os
import sys


'''recommend for txt file like nginx logfile or other txt files, mode 1'''

def filesplitbylines(filename,count,destname):
    fp = open(filename,"rb")
    lines = 0
    while True:
        buffer = fp.read(1024*8192)
        if not buffer:
            break
        lines = lines + buffer.count('\n')
    tmpsize = lines/count
    fp.close()
    fp = open(filename,"r")
    i = 0
    for i in range(1,count):
        fp2 = open(destname+"_"+str(i),"w")
        for j in range(0,tmpsize):
            buf = fp.readline()
            fp2.writelines(buf)
            buf = ""
        fp2.close()
    tmp = i+1
    fp2 = open(destname+"_"+str(tmp),"w")
    for i in range(1, lines - tmpsize*(count-1)):
        buf = fp.readline()
        fp2.writelines(buf)
        buf = ""
    fp.close()
    fp2.close()
    
'''recommend for data files like rar files or other, mode 0, defult mode, much more faster than txt mode'''

def filesplitbychunk(filename,count,destname):
    chunksize = 1024
    filesize = os.path.getsize(filename)
    print("filesize: "+str(filesize/1024/1024)+"MB")
    tmpsize = filesize/count
    ressize = filesize - tmpsize*(count - 1)
    print("filesize: "+str(filesize)+" tmpsize: "+str(tmpsize)+" ressize: "+str(ressize))
    fp = open(filename,"r")
    i = 0
    for i in range(1,count):
        fp2 = open(destname+"_"+str(i),"wb")
        count2 = tmpsize/chunksize
        res2 = tmpsize - chunksize*(count2 - 1)
        for j in range(1,count2):
            buf = fp.read(chunksize)
            fp2.write(buf)
            buf = ""
        buf = fp.read(res2)
        fp2.write(buf)
        fp2.close()
    tmp = i+1
    fp2 = open(destname+"_"+str(tmp),"wb")
    count3 = ressize/chunksize
    res3 = ressize - chunksize*(count3-1)
    for i in range(1,count3):
        buf = fp.read(chunksize)
        fp2.write(buf)
        buf = ""
    buf = fp.read(res3)
    fp2.write(buf)
    fp2.close()
    fp.close()

    
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("plese input \" mode count inputfilename outputname\"")
    else:
        mode = sys.argv[1]
        count = sys.argv[2]
        inputfilename = sys.argv[3]
        outputname = sys.argv[4]
        flag = 1
        if not os.path.exists(inputfilename):
            print("file not exist!")
            flag = 0
        if not count.isdigit():
            print("invalid count!")
            flag = 0
        if flag == 1:
            if mode == '0':
                filesplitbychunk(inputfilename,int(count),outputname)
            elif mode == '1':
                filesplitbylines(inputfilename,int(count),outputname)
            else:
                print("invalid mode")

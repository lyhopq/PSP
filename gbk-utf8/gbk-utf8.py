# -*- coding: utf-8 -*-
 
import os,sys  

def is_c_file(filename):
    _name, ext = os.path.splitext(filename)
    return ext in ('.c', '.cpp', '.cxx', '.h', '.hpp)
  
def convert(filename, in_enc = "GBK", out_enc="UTF8"):  
    if not is_c_file(filename):
        return
    try:  
        print "convert " + filename,  
        with open(filename, 'r') as f:
            content = f.read()  
            new_content = content.decode(in_enc).encode(out_enc)  
        with open(filename, 'w') as f:
            f.write(new_content)  
        print " done"  
    except:  
        print " error"  
  
def explore(dir):  
    for root, dirs, files in os.walk(dir):  
        for file in files:  
            path = os.path.join(root, file)  
            convert(path)  
  
def main():  
    for path in sys.argv[1:]:  
        if os.path.isfile(path):  
            convert(path)  
        elif os.path.isdir(path):  
            explore(path)  
  
if __name__ == "__main__":  
    main()

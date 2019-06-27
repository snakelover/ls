import optparse
import os
import locale

def ls(path, modified, order, sizes):
    #path = os.path.normpath(path)
    one_path_list = []
    files = {}
    #abspath = os.getcwd()
    #print(path)
    #os.chdir(path)
    relpath = os.path.relpath(path,start=path)
    #print(relpath)
    #print(os.pardir)
    #print()
    dirs_counter = 0
    files_counter = 0
    string = ""
    
    functions = {}
    if modified:
        string += "modified"
        functions["modified"] = os.path.getmtime
    
    if sizes:
        string += " sizes"
        functions["sizes"] = os.path.getsize
    if order in {"name", "n"}:
        string += " name"
        functions["name"] = os.path.basename
    elif order in {" size", "s"} and not sizes:
        string += " sizes"
        functions["size"] = os.path.getsize
    elif order in {"modified", "m"} and not modified:
        string += " modified"
        functions["modified"] = os.path.getmtime
    print(string)
    Test = collections.namedtuple("Test", string)
    l = []
    print(functions)
    for name in os.listdir(path):
        fullname = os.path.join(path, name)
        p = []
        key = collections.namedtuple('Key', string)
	
        for n, fun in functions.items():
            f = fun
            p.append(f(fullname))
            #key.n = f(fullname)
            #print(fun(fullname))
        
        print(p)
        key = p
        print(key)
        l.append(key)
        
        #if modified:
            #key.modified = os.path.getmtime(fullname)
        
        if order in {'name', 'n'}:
            pass
        elif order in {'modified', 'm'}:
            pass
        elif order in {'size', 's'}:
            pass
        
        if os.path.isdir(fullname):
            fullname += os.sep
            dirs_counter += 1
        else:
            files_counter += 1
        #print(fullname) 
        print(l)
        one_path_list.append(fullname)
        #print(fullname)
        #print(os.path.basename(fullname))
    #return one_path_list


def rec_ls(path):#, modified, order, sizes):

    dirs_counter = 0
    files_counter = 0

    files = {}
    
    for root, dirs, files in os.walk(path):
        #dirs[:] = [dir for dir in dirs if not dir.startswith("h")]
        
        for filename in files:
            fullname = os.path.join(root, filename)
            files_counter += 1
            print(root)
            #print(filename)
            print(fullname)
        #if not hidden_flag:
        
        for directory in dirs:
            dirs_counter += 1
            #print(os.path.dirname(fullname))
            #print(os.path.relpath(path, fullname))
            #dirs.append(os.path.relpath(fullname))

    #dirs[:] = [dir for dir in dirs if not dir.startswith(".")]

#rec_ls(os.getcwd())

#rec_ls("C:\Videos")

print(ls(os.curdir,True, 'name', True))
#rec_ls(os.curdir)
        


def main():
    parser = optparse.OptionParser(usage="Usage: %prog [options] [path1 [path2 [... pathN]]]",
                                   description="The paths are optional; if not given . is used.")
    parser.add_option("-H", "--hidden", action="store_true", default=False,
                      dest="hidden", help="show hidden files [default: %default]")
    parser.add_option("-m", "--modified", action="store_true", default=False,
                      dest="modified", help="show last modified date/time [default: %default]")
    #parser.add_option("-o", "--order", default=False, dest="order")
    parser.add_option("-o", "--order", type="choice", choices=["name", "n", "modified", "m", "size", "s"],
                      default="name", help="\norder by ('name', 'n', 'modified', 'm', 'size', 's') [default: %default]")
    parser.add_option("-r", "--recursive", action="store_true", default=False,
                      dest="recursive", help="recurse into subdirectories [default: %default]")
    parser.add_option("-s", "--sizes", action="store_true", default=False,
                      dest="sizes", help="show sizes [default: %default]")

    #parser.set_defaults(hidden=False)
    #parser.add_option('--earth', action="store_const", const='earth', dest='element', default='earth')
    #parser.add_option('--air', action='store_const', const='air', dest='element')
    #parser.add_option('--water', action='store_const', const='water', dest='element')
    #parser.add_option('--fire', action='store_const', const='fire', dest='element')
    opts, args = parser.parse_args()
    dirs = []
    if args:
        for path in args:
            dirs += show(path)
    else:
        dirs = show()

    for entity in dirs:
        print(entity)
    

main()

    

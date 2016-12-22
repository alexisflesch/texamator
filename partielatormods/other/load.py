# -*- coding: utf-8 -*-
import os, codecs


def file_to_dict(fichier,defautDict):    
    try:
        f = codecs.open(fichier,'r','utf-8')
    except:
        return defautDict
    lines=f.readlines()
    f.close()
    ret = defautDict
    for line in lines:
        line = line.strip()
        if line and line[0] != "#":
            values = line.split("=")
            ret[values[0]] = values[1].replace('\"','')
    return ret

def file_to_tag_list(fichier,defautList):
    try:
        f = codecs.open(fichier,'r','utf-8')
    except:
        return defautList
    lines=f.readlines()
    f.close()
    tags = [[],[]]
    for line in lines:
        line = line.strip()
        if line and line[0] != "#":
            values = line.split("!!!")
            tags[0].append(values[0])
            tags[1].append(values[1])
    return tags

def gimme_my_settings():
    """Give preferences"""
    #First of all, create a .partielator dir in the home folder if it doesn't exist
    #and delete .partielator if it's a file (old version worked with a .partielator file)
    #Tells if a .partielator dir was found so as to know whether the wizard should be shown
    home_dir = os.path.expanduser("~")
    first_time = False
    if ".partielator" in os.listdir(home_dir):
        if os.path.isfile(os.path.join(home_dir,".partielator")):
            os.remove(os.path.join(home_dir,".partielator"))
            os.mkdir(os.path.join(home_dir,".partielator"))
            first_time = True
        if not "generate" in os.listdir(os.path.join(home_dir,".partielator")):
            os.mkdir(os.path.join(home_dir,".partielator","generate"))
    else:
        os.mkdir(os.path.join(home_dir,".partielator"))
        os.mkdir(os.path.join(home_dir,".partielator","generate"))
        first_time = True

    #Get basic settings in a dictionnary
    fichier = os.path.join(home_dir,".partielator","basics")
    defautDict = { "file_viewer" : "okular",\
               "save_location" : home_dir,\
               "tex_path" : home_dir,\
               "little_splitter_s1" : "200",\
               "little_splitter_s2" : "250",\
               "big_splitter_s1" : "450",\
               "big_splitter_s2" : "550",\
               "height" : "550",\
               "width" : "1000",\
               "prefs width" : "800",\
               "prefs height" : "600",\
               "export width" : "400",\
               "export height" : "400",\
               "edit width" : "400",\
               "edit height" : "600",\
               "AMC" : "False",\
               "AMC-text" : "%AMC-stuff",\
               "AMC-env" : "qcm",\
               "prefs splitter one" : "250",\
               "prefs splitter two" : "150",\
               "preferred compile sequence" : "Default (pdflatex)",\
               "preferred compile sequence for exportation" : "Default (pdflatex)",\
               "preferred type of export" : "pdf",\
               "preferred header/footer" : "Same header/footer",\
               "lang" : "en"}
    dictionnary = file_to_dict(fichier,defautDict)

    #Get header
    try:
        f = codecs.open(os.path.join(home_dir,".partielator","header"),'r','utf-8')
        header = ""
        for l in f.readlines():
            header += l
    except:
        header = "\\documentclass{article}\n"
        header += "\\begin{document}"

    #Get footer
    try:
        f = codecs.open(os.path.join(home_dir,".partielator","footer"),'r','utf-8')
        footer = ""
        for l in f.readlines():
            footer += l
    except:
        footer = "\\end{document}"
    
    #Get tags
    defautList = [["\\begin{exercise}"],["\\end{exercise}"]]
    fichier = os.path.join(home_dir,".partielator","tags")
    tags = file_to_tag_list(fichier,defautList)
    
    #Get compile sequence
    #compile_seq is a dictionnary of compile sequences :
    compile_seq = {}
    liste_fichiers = os.listdir(os.path.join(home_dir,".partielator"))
    if "compile_seq2" not in liste_fichiers:           #First time running Texamator > 1.6
        #Adding default compile sequences
        setDefaultSequences(compile_seq)
        #Export new config to text file
        f = codecs.open(os.path.join(home_dir,".partielator","compile_seq2"),'w','utf-8')
        for key in compile_seq.keys():
            f.write('###' + key + '###\n')
            f.write('#type of file:' + compile_seq[key]['type of file'] + '\n')
            f.write('#use preview:' + compile_seq[key]['use preview'] + '\n')
            for item in compile_seq[key]['sequence']:
                f.write(item+'\n')
        f.close()
    else:
        f = codecs.open(os.path.join(home_dir,".partielator","compile_seq2"),'r','utf-8')
        for i in f.readlines():
            i = i.replace("\n","")
            if i[:3]=="###" and i[-3:]=="###":
                sequenceName = i[3:-3]
                compile_seq[sequenceName] = {'sequence':[],'type of file':'pdf', 'use preview':'False'}
            elif i[:13] == '#type of file':
                compile_seq[sequenceName]['type of file'] = i[14:]
            elif i[:12] == '#use preview':
                compile_seq[sequenceName]['use preview'] = i[13:]
            else:
                compile_seq[sequenceName]['sequence'].append(i)
        #Adding default compile sequences
        setDefaultSequences(compile_seq)
    
    #Get generate files
    generate = {"Same header/footer" : [header,footer]}
    liste = os.listdir(os.path.join(home_dir,".partielator","generate"))
    for i in liste:
        if i[-4:] != ".end":
            try:
                f = codecs.open(os.path.join(home_dir,".partielator","generate",i),'r','utf-8')
                generate[i] = ["",""]
                for l in f:
                    generate[i][0] += l
                f.close()
                if i+".end" in liste:
                    g = codecs.open(os.path.join(home_dir,".partielator","generate",i+".end"),'r','utf-8')
                    for l in g:
                        generate[i][1] += l
                    g.close()
            except:
                print("couldn't process file "+f)

    return first_time, tags, header, footer, dictionnary, compile_seq, generate


def setDefaultSequences(compile_seq):
    #Old computer : with latex/dvipng/preview package and a QLabel to handle the png
    compile_seq["Old computer (dvi no okular)"] = {}
    compile_seq["Old computer (dvi no okular)"]['sequence'] = ["latex -interaction=nonstopmode file.tex", "dvipng file.dvi -o file.png"]
    compile_seq["Old computer (dvi no okular)"]['use preview'] = 'True'
    compile_seq["Old computer (dvi no okular)"]['type of file'] = 'png'
    #Alternative : with latex/no preview package/okular
    compile_seq["Alternative (latex)"] = {}
    compile_seq["Alternative (latex)"]['sequence'] = ["latex -interaction=nonstopmode file.tex"]
    compile_seq["Alternative (latex)"]['type of file'] = 'dvi'
    compile_seq["Alternative (latex)"]['use preview'] = 'False'
    #Default : with pdflatex/no preview package/okular
    compile_seq["Default (pdflatex)"] = {}
    compile_seq["Default (pdflatex)"]['sequence'] = ["pdflatex -interaction=nonstopmode file.tex"]
    compile_seq["Default (pdflatex)"]['type of file'] = 'pdf'
    compile_seq["Default (pdflatex)"]['use preview'] = 'False'    


if __name__ == "__main__":
    first_time, tags, header, footer, dictionnary, compile_seq, generate = gimme_my_settings()
    for key in compile_seq.keys():
        print(key)
        print(compile_seq[key])




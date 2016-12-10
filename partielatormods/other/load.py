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
    defautDict = { "file_viewer" : "xdvi",\
               "type_of_file" : "pdf",\
               "save_location" : home_dir,\
               "tex_path" : home_dir,\
               "use_preview" : "True",\
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
               "prefs splitter one" : "250",\
               "prefs splitter two" : "150",\
               "preferred compile sequence" : "Default (pdf + okular)",\
               "preferred compile sequence for exportation" : "Default (pdf + okular)",\
               "preferred type of export" : "pdf",\
               "preferred header/footer" : "Same header/footer",\
               "embedded viewer" : "okular",\
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
        compile_seq["Old computer (dvi no okular)"] = ["latex -interaction=nonstopmode file.tex",\
                    "dvipng file.dvi -o file.png"]
        compile_seq["Alternative (dvi + okular)"] = ["latex -interaction=nonstopmode file.tex"]
        compile_seq["Default (pdf + okular)"] = ["pdflatex -interaction=nonstopmode file.tex"]
        if "compile_seq" in liste_fichiers:            #TeXamator < 1.6 has been used before on this computer, adding old compile config
            compile_seq["User Defined"] = []
            f = codecs.open(os.path.join(home_dir,".partielator","compile_seq"),'r','utf-8')
            for i in f.readlines():
                compile_seq["User Defined"].append(i.replace("\n",""))
            f.close()
            if compile_seq["User Defined"] == compile_seq["Default (dvi no okular)"]:
                del compile_seq["User Defined"]
        #Export new config to text file
        f = codecs.open(os.path.join(home_dir,".partielator","compile_seq2"),'w','utf-8')
        for key in compile_seq.keys():
            f.write("###" + key + "###\n")
            for item in compile_seq[key]:
                f.write(item+'\n')
        f.close()
            
    else:
        f = codecs.open(os.path.join(home_dir,".partielator","compile_seq2"),'r','utf-8')
        sequence = "plop"
        for i in f.readlines():
            i = i.replace("\n","")
            if i[:3]=="###" and i[-3:]=="###":
                sequence = i[3:-3]
                compile_seq[sequence] = []
                continue
            compile_seq[sequence].append(i)
        #Adding default compile sequences
        compile_seq["Old computer (dvi no okular)"] = ["latex -interaction=nonstopmode file.tex",\
                    "dvipng file.dvi -o file.png"]
        compile_seq["Alternative (dvi + okular)"] = ["latex -interaction=nonstopmode file.tex"]
        compile_seq["Default (pdf + okular)"] = ["pdflatex -interaction=nonstopmode file.tex"]
    
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



if __name__ == "__main__":
    tags, header, dictionnary, compile_seq, generate = gimme_my_settings()
    print generate["basics"]




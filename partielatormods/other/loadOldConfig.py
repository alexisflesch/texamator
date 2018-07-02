# -*- coding: utf-8 -*-

"""This file is to be deleted in a few years
   along with 
   | in load.py
           if ".partielator" not in os.listdir(home_dir):
            first_time = True
   | in texamator.py
           first_time = "partielator"
    and what comes next.
"""


import os, codecs, shutil


def getDefaultSequences():
    """Returns a dictionnary containing two Default compilation sequences"""
    compile_seq = {}
    #Alternative : with latex/dvips/ps2pdf
    compile_seq["Alternative (latex/dvips/ps2pdf)"] = ["latex -interaction=nonstopmode file.tex"]
    compile_seq["Alternative (latex/dvips/ps2pdf)"].append("dvips file.dvi")
    compile_seq["Alternative (latex/dvips/ps2pdf)"].append("ps2pdf file.ps")
    #Default : with pdflatex
    compile_seq["Default (pdflatex)"] = ["pdflatex -interaction=nonstopmode file.tex"]  
    return compile_seq

def fileToDict(fichier, defautDict):    
    """turns a file into a dictionnary"""
    try:
        f = codecs.open(fichier,'r','utf-8')
    except:
        return defautDict
    lines = f.readlines()
    f.close()
    ret = defautDict
    for line in lines:
        line = line.strip()
        if line and line[0] != "#":
            values = line.split("=")
            if values[1] != "Old computer (dvi no okular)":
                ret[values[0]] = values[1].replace('\"','')
    return ret

def fileToTagList(fichier, defautList):
    """ extracts tags from the text file where they are stored.
        There is one tag per line, looking like this:
        \begin{tag}!!!\end{tag}
    """
    try:
        f = codecs.open(fichier,'r','utf-8')
    except:
        return defautList
    lines = f.readlines()
    f.close()
    tags = [[],[]]
    for line in lines:
        line = line.strip()
        if line and line[0] != "#":
            values = line.split("!!!")
            tags[0].append(values[0])
            tags[1].append(values[1])
    return tags

def getOldSettings():
    """ Fetch settings in .partielator directory (TeXamator before version 3)
        and turns into something understandable by TeXamator version >= 3).
    """
    tags, header, footer, dictionnary, compile_seq, generate = extractOldSettings()
    
    #Compile sequences
    compile_seq2 = compile_seq.copy()
    for key in compile_seq:
        if key=="Old computer (dvi no okular)" or key=="Alternative (latex)":
            continue
        else:
            compile_seq2[key] = compile_seq[key]
    
    #Header/footer and generate are now in the same dictionnary
    preamblesPostambles = generate
    preamblesPostambles["Default"] = [header, footer]
    
    saveSettings(tags, dictionnary, compile_seq2, preamblesPostambles)
    
    return tags, dictionnary, compile_seq2, preamblesPostambles


def saveSettings(tags, dictionnary, compile_seq, preamblesPostambles):
    """Save settings previously extracted to directory ~/.texamator"""
    home_dir = os.path.expanduser("~")
    #Saving general preferences
    f = codecs.open(os.path.join(home_dir, ".texamator", "preferences.txt"), 'w', "utf-8")
    for key, value in dictionnary.items():
        f.write(key + "=" + str(value) + "\n")
    f.close()
    #Saving compile sequences
    for key in compile_seq.keys():
        if key in ["Alternative (latex/dvips/ps2pdf)","Default (pdflatex)"]:
            continue
        foo = os.path.join(home_dir, ".texamator", "compile.sequences", key)
        f = codecs.open(foo, 'w', 'utf-8')
        for item in compile_seq[key]:
            f.write(item+'\n')
        f.close()
    #Saving tags
    shutil.copyfile(os.path.join(home_dir,".partielator","tags"),os.path.join(home_dir,".texamator","tags.txt"))
    #Saving preambles/postambles 
    for key in preamblesPostambles.keys():
        f = codecs.open(os.path.join(home_dir, ".texamator", "preambles.and.postambles", key+".preamble.tex"), 'w', 'utf-8')
        g = codecs.open(os.path.join(home_dir, ".texamator", "preambles.and.postambles", key+".postamble.tex"), 'w', 'utf-8')
        f.write(preamblesPostambles[key][0])
        g.write(preamblesPostambles[key][1])
        f.close()
        g.close()

def extractOldSettings():
    """Give preferences"""
    #First of all, create a .partielator dir in the home folder if it doesn't exist
    #and delete .partielator if it's a file (old version worked with a .partielator file)
    #Tells if a .partielator dir was found so as to know whether the wizard should be shown
    home_dir = os.path.expanduser("~")

    #Get basic settings in a dictionnary
    fichier = os.path.join(home_dir,".partielator","basics")
    defautDict = { "file_viewer" : "okular",\
               "save_location" : home_dir,\
               "tex_path" : home_dir,\
               "little_splitter_s1" : "200",\
               "little_splitter_s2" : "250",\
               "big_splitter_s1" : "450",\
               "big_splitter_s2" : "550",\
               "height" : "600",\
               "width" : "800",\
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
               "preferred preamble" : "Default",\
               "preferred preamble for export" : "Default",\
               "lang" : "en"}
    dictionnary = fileToDict(fichier, defautDict)

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
    fichier = os.path.join(home_dir, ".partielator", "tags")
    tags = fileToTagList(fichier, defautList)
    
    #Get compile sequence
    #compile_seq is a dictionnary of compile sequences :
    compile_seq = getDefaultSequences()
    liste_fichiers = os.listdir(os.path.join(home_dir,".partielator"))
    f=codecs.open(os.path.join(home_dir,".partielator","compile_seq2"),'r','utf-8')
    for i in f.readlines():
        i = i.strip()
        if i[:3]=="###" and i[-3:]=="###":
            sequenceName = i[3:-3]
        if sequenceName in ["Default (pdflatex)", "Alternative (latex)", "Old computer (dvi no okular)"]:
            continue
        else:
            compile_seq[sequenceName] = []
        if i[:1] != '#':
            compile_seq[sequenceName].append(i)
    
    #Get generate files
    generate = {}
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

    return tags, header, footer, dictionnary, compile_seq, generate


if __name__ == "__main__":
    print(getOldSettings())




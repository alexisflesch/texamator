# -*- coding: utf-8 -*-
import os, codecs
from .loadOldConfig import *


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



def getDefaultPreamblePostamble():
    """Creates a minimalist preamble to compile tex files"""
    preamblesPostambles = {}
    #Default preamble (what comes before the exercises)
    pre = """\\documentclass[a4paper,10pt]{article}""" + "\n"
    pre += """\\usepackage[utf8]{inputenc}""" + "\n"
    pre += """\\usepackage[top=0cm,bottom=0cm,left=0cm,right=0cm]{geometry}""" + "\n"
    pre += """\\usepackage{amsthm}""" + "\n"
    pre += """\\usepackage{amssymb}""" + "\n"
    pre += """\\newtheorem{exercise}{Exercise}""" + "\n"
    pre += """\\begin{document}""" + "\n"
    #Default postamble (what comes after the exercises)
    post = """\\end{document}"""
    preamblesPostambles["Default"] = [pre, post]
    return preamblesPostambles



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



def getSettings():
    """Extract preferences from ~/.texamator folder"""
    #First of all, create a .texamator dir in the home folder if it doesn't exist
    #Tells if a .texamator dir was found so as to know whether the wizard should be shown
    home_dir = os.path.expanduser("~")
    first_time = False
    if ".texamator" not in os.listdir(home_dir):
        os.mkdir(os.path.join(home_dir,".texamator"))
        os.mkdir(os.path.join(home_dir,".texamator","compile.sequences"))
        os.mkdir(os.path.join(home_dir,".texamator","preambles.and.postambles"))
        if ".partielator" not in os.listdir(home_dir):
            first_time = True
        else:
            first_time = "partielator"
            tags, dictionnary, compile_seq, preamblesPostambles = getOldSettings()
            return first_time, tags, dictionnary, compile_seq, preamblesPostambles
    #Get basic settings in a dictionnary
    fichier = os.path.join(home_dir,".texamator","preferences.txt")
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
    
    #Get tags
    defautList = [["\\begin{exercise}"],["\\end{exercise}"]]
    fichier = os.path.join(home_dir,".texamator","tags.txt")
    tags = fileToTagList(fichier, defautList)
    
    #Get compile sequences
    #compile_seq is a dictionnary of compile sequences. Initiate it with default sequences
    compile_seq = getDefaultSequences()
    #Grab the other sequences
    dirName = os.path.join(home_dir,".texamator","compile.sequences")
    listOfFiles = os.listdir(dirName)
    for foo in listOfFiles:
        f = codecs.open(os.path.join(dirName,foo),'r','utf-8')
        compile_seq[foo] = []
        for line in f.readlines():
            line = line.strip()
            compile_seq[foo].append(line)
        f.close()

    #Get preambles/postambles
    #preamblesPostambles is a dictionnary of lists : [preamble, postamble].
    if first_time:
        preamblesPostambles = getDefaultPreamblePostamble()
    else:
        preamblesPostambles = {}
    dirName = os.path.join(home_dir,".texamator","preambles.and.postambles")
    listOfFiles = os.listdir(dirName)
    for foo in listOfFiles:
        if foo[-13:]==".preamble.tex":
            f = codecs.open(os.path.join(dirName,foo),'r','utf-8')
            preamblesPostambles[foo[:-13]] = ["",""]
            for line in f.readlines():
                preamblesPostambles[foo[:-13]][0] += line
            f.close()
            g = codecs.open(os.path.join(dirName,foo[:-13]+".postamble.tex"),'r','utf-8')
            for line in g.readlines():
                preamblesPostambles[foo[:-13]][1] += line
            g.close()

    return first_time, tags, dictionnary, compile_seq, preamblesPostambles



if __name__ == "__main__":
    getSettings()
    


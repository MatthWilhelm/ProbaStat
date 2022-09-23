import os
import re

########################################################

def FileList(dir):
    """
    """
    pathList = os.listdir(dir)
    index_to_remove = []
    
    for i, p in enumerate(pathList):
        root, extension = os.path.splitext(p)
        
        if extension == "":
            index_to_remove.append(i)
            if p[0] != "." and not re.search("/.",p):
                print(p)
                newlist = os.listdir(os.path.join(dir,p))
                for l in newlist:
                    pathList.append(os.path.join(p,l))
                    
    for i in reversed(index_to_remove):
        del pathList[i]
        
    return pathList

########################################################
import pandas as pd

to_translate = pd.DataFrame(data = {
"english": ["Algorithm","Axiom","Assumption","Criterion","Definition","Example","Lemma","Property","Remark","Theorem"],
"french": ["Algorithme","Axiome","Supposition","Critère","Définition","Exemple","Lemme","Propriété","Remarque","Théorème"]
                            })

def translate_admonition(source):
    ind = 0
    n1 = len("<p class=\"admonition-title\">")
    n2 = len("</p>")
    while re.search("<p class=\"admonition-title\">",source[ind:]):
        i = source[ind:].find("<p class=\"admonition-title\">")
        j = source[i+ind:].find("</p>")
        for ii, name in enumerate(to_translate.english):
            if re.search(name,source[i+ind:ind+i+j]):
                source = source[:ind+i]  + source[ind+i:ind+i+j].replace(name,to_translate.french[ii]) + source[ind+i+j:]
        ind = ind + j + i + 1
        
    return source
    
########################################################

def filter_svg_pdf(source, type):
    """
    """
    if type == "html":
        source = source.replace(".#",".svg")
    else:
        source = source.replace(".#","." + type)
    return source
    
########################################################

def colour_handling(source,type):
    """
    """
    
    n = len("\_color")
    while re.search("\_color",source):
        
        begin = source.find("\_color")
        i1 = source[begin:].find("{")
        i2 = source[begin:].find("}")
        color = source[begin+i1+1:begin+i2]
        j1 = i2+1
        j2 = source[begin+j1:].find("}_color")
        text = source[begin+j1+1:begin+j1+j2]
        
        if type == "html":
            source = source[:begin] + "<font color=\"" + color + "\">" + text + "</font>" + source[begin+j1+j2+len("}_color"):]
        elif type == "pdf":
            source = source[:begin+1] + source[begin+2:]
            # text + "**" + source[begin+j1+j2:]
            
    return source

########################################################

def center(source,type):
    """
    """
    
    n = len("\_center")
    while re.search("\_center",source):
        begin = source.find("\_center")
        end = source[begin:].find("}_center")
        if type == "html":
            if re.search("\\",source[begin:end]):
                source = source[:begin] + source[begin:end].replace("\\","<br>") + source[end:]
                end = source[begin:].find("}_center")
            source = source[:begin] + "<p style=\"text-align:center\">" + source[begin+n+1:begin+end] + "</p>" + source[begin+end+n:]
        elif type == "pdf":
            source = source[:begin] + "\\begin{gather*} \n" + source[begin+n+1:begin+end] + "\n \end{gather*}" + source[begin+end+n:]
    return source

########################################################

def duplicate_filter(source, type):
    """
    """
    
    if type == "html":
        if re.search("%%html",source):
            source = source.replace("%%html","")
        if re.search("%%pdf",source):
            while re.search("%%pdf",source):
                i = source.find("%%pdf")
                j = source[i+len("%%pdf"):].find("%%pdf")
                source = source[:i] + source[i+j+2*len("%%pdf"):]
    if type == "pdf":
        if re.search("%%pdf",source):
            source = source.replace("%%pdf","")
        if re.search("%%html",source):
            while re.search("%%html",source):
                i = source.find("%%html")
                j = source[i+len("%%html"):].find("%%html")
                source = source[:i] + source[i+j+2*len("%%html"):]
    
    return source
    
########################################################

def global_filter(source,type):
    
    source = filter_svg_pdf(source, type)
    source = colour_handling(source,type)
    source = center(source,type)
    source = duplicate_filter(source,type)
    
    return source

########################################################

                

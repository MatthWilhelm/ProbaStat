#!/bin/env python3

import argparse
import subprocess
import shutil
import os
import helper

def main():
    """
    """
    
    parser = argparse.ArgumentParser(description='Filtering HMTL/PDF output.')
    parser.add_argument("--html", action='store_true',
                        help="Asks to produce the html version of the book")
    parser.add_argument("-p", "--pdf", action='store_true',
                        help="Asks to produce the pdf version of the book")
    arguments = parser.parse_args()
    
    pathList = helper.FileList("book")
    
    # Translate the admnotition of the sphinx-proof package
    for folder in pathList:
        #print(folder)
        root, extension = os.path.splitext(folder)
        ## Cleaning the file
        if extension == ".md":
            # clean .md
            
            with open(os.path.join(f"book/_build/html",root+".html")) as f:
                content = f.read()
            content = helper.translate_admonition(content)
            with open(os.path.join(f"book/_build/html",root+".html"),"w") as f:
                f.write(content)
    
    if False:
        subprocess.run("mkdir book",shell = True)
        
        #if os.path.exists("book"):
            #shutil.rmtree("book")
        
        #shutil.copytree("bookHybrid",f"bookHTML")
        # Filter the code of each .md files
        for folder in pathList:
            root, extension = os.path.splitext(folder)
            ## Cleaning the file
            if extension == ".md":
                # clean .md
                with open(os.path.join(f"book",folder)) as f:
                    content = f.read()
                content = helper.global_filter(content,"html")
                with open(os.path.join(f"book",folder),"w") as f:
                    f.write(content)
            elif extension == ".ipynb":
                # clean .ipynb
                i  = 1
    elif False:
        if os.path.exists("bookPDF"):
            shutil.rmtree("bookPDF")
        
        shutil.copytree("bookHybrid","bookPDF")
        # Filter the code of each .md files
        for folder in pathList:
            root, extension = os.path.splitext(folder)
            ## Cleaning the file
            if extension == ".md":
                # clean .md
                with open(os.path.join("bookPDF",folder)) as f:
                    content = f.read()
                content = helper.global_filter(content,"pdf")
                with open(os.path.join("bookPDF",folder),"w") as f:
                    f.write(content)
            elif extension == ".ipynb":
                # clean .ipynb
                i  = 1
    
################################################################
if __name__ == "__main__":
    main()

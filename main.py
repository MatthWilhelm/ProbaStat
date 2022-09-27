#!/bin/env python3

import argparse
import subprocess

def main():
    """
    """
    
    #subprocess.run("python convertion.py --html",shell = True)
    
    subprocess.run(f"jupyter-book clean book/ --all",shell = True)
    subprocess.run(f"jb build book/",shell = True)
    subprocess.run("python convertion.py ",shell = True)

    #subprocess.run(f"jupyter-book build book --builder pdfhtml",shell = True)
    
################################################################
if __name__ == "__main__":
    main()


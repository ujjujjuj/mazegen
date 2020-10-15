import os
import sys
from mazegen import generator
from mazegen import view
from mazegen import solver

options = ['generate','view','solve', '-h','--help']

helptxt = 'Usage: mazegen [option] [filename] [optional]\n'\
        '\n'\
        'OPTIONS:\n'\
        'generate        Generates .maze file\n'\
        'view            Views existing .maze file as an image\n'\
        'solve           Solves a .maze file\n'\
        '\n'\
        'OPTIONAL ARGUMENTS:\n'\
        '-s, --save      Save generated .png file'

usage = 'Usage: mazegen [option] [filename] [optional]'

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--help','-h']:
            print(helptxt)
            exit()
    if len(sys.argv) < 3:
        print(usage)
        exit()
    if sys.argv[1] not in options:
        print(usage)
        exit()
    save = False
    if len(sys.argv) > 3:
        if sys.argv[3] in ['-s','--save']:
            save = True
    if sys.argv[1] == "generate":
        generator.main(os.getcwd(), sys.argv[2], save)
    elif sys.argv[1] == "view":
        view.main(os.getcwd(), sys.argv[2], save)
    else:
        solver.main(os.getcwd(), sys.argv[2], save) 

if __name__ == "__main__":
    main()

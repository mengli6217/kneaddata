'''
Ad Hoc script to filter Silva database FASTAs. First, it changes U's to T's.
Then, it removes spaces in the sequence entries. Finally, it removes sequences
that are not from bacteria or archaea.
'''

import argparse
import re
import sets

def filter_bugs(infile, outfile):
    '''
    Converts all the U to T from the input FASTA, infile. Writes the output to
    the output FASTA specified by outfile
    '''
    f_in = open(infile, "r")
    f_out = open(outfile, "w")

    regex = r'([A-Za-z]+) ([A-Za-z]+) *\n'
    bugs_list = ["Fusobacterium nucleatum"]
    bugs = sets.Immutable(bugs_list)

    fKeep = False
    for line in f_in:
        if line[0] == '>':
            # Only keep those that are in our set
            match = re.search(regex, line)
            if match:
                strBugName = match.group(1) + " " + match.group(2)
                if strBugName in bugs:
                    fKeep = True
                    print(new_line)
                    f_out.write(new_line)
                    continue
                else:
                    fIsBacteria = False
                    continue
            else:
                print("No match found in the following line: " + line)

        if fIsBacteria:
            f_out.write(new_line)

    f_in.close()
    f_out.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="input fasta containing RNA data")
    parser.add_argument("outfile", help="output file")

    args = parser.parse_args()

    filter_bugs(args.infile, args.outfile)

if __name__ == '__main__':
    main()

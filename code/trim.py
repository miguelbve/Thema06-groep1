#!/usr/bin/env python3
"""

"""

__author__ = "Jorick Baron"

import sys
import subprocess


def trimmer():
    with open('../logs/data_path.log', 'r') as pathlog, open('../logs/fastq_files.log', 'r') as fastqlog:
        data_path = pathlog.readline()
        fastqdirs = [("../results/trim_galore/" + file[0:-4]) for file in fastqlog]
        fastqlog.seek(0) # set the current read position back to the first line
        fastqfiles = [(data_path+file[0:-1]) for file in fastqlog]
        for fastqfile, fastqdir in zip(fastqfiles, fastqdirs):
            subprocess.run(["trim_galore", fastqfile, '-o', fastqdir, "--fastqc_args", "--outdir " + fastqdir], text=True)


def main():
    """
    
    """
    trimmer()
    return 0


if __name__ == '__main__':
    sys.exit(main())

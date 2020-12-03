"""
Reads log files to determine data file paths and use them as arguments for the fastqc CLI tool

usage:
    python3 fastqc.py       program file
"""

import subprocess
import argparse


def execute_fastqc():
    """ Execute fastqc and write the output to the data directories """
    with open('../logs/data_path.log', 'r') as pathlog, open('../logs/fastq_files.log', 'r') as fastqlog:
        data_path = pathlog.readline()
        fastqdirs = [("../results/fastqc/" + file[0:-4]) for file in fastqlog]
        fastqlog.seek(0) # set the current read position back to the first line
        fastqfiles = [(data_path+file[0:-1]) for file in fastqlog]
        for fastqfile, fastqdir in zip(fastqfiles, fastqdirs):
            subprocess.run(["fastqc", fastqfile, '-o', fastqdir], text=True)


def main():
    """ main """
    execute_fastqc()


if __name__ == "__main__":
    main()
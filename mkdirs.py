"""
path to data
/data/storix2/student/2019-2020/Thema06/project-data/How_to_deal_with_difficult_data/Data/

data files
SRR018013_1.fastq.gz  SRR018015.fastq.gz  SRR057599.fastq.gz   SRR1106122.fastq.gz  SRR1106139.fastq.gz
SRR018013_2.fastq.gz  SRR057598.fastq.gz  SRR1106118.fastq.gz  SRR1106138.fastq.gz  SRR1106140.fastq.gz
"""

import subprocess
import argparse

def log_fastq_files(data_path):
    """ Logs the names of the fastq data files to scanned_fastq_files.log"""
    with open('scanned_fastq_files.log', 'w') as file_obj:
        subprocess.run(["ls", data_path], text=True, stdout=file_obj)


def make_fastq_dirs():
    """ Returns directories derived from the base names"""
    with open('scanned_fastq_files.log') as file_obj:
        fastqdirs = [file[0:-4] for file in file_obj]
        for dir in fastqdirs:
            subprocess.run(["mkdir", dir], text=True, stdout=file_obj)


# def check_quality(in_path):
#     """ reads fastq file """
#     subprocess.run(f"fastqc {in_path} ", shell=True, executable="/bin/bash")


def main():
    """ main """
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path")
    args = parser.parse_args()

    log_fastq_files(args.data_path)
    make_fastq_dirs()



if __name__ == "__main__":
    main()
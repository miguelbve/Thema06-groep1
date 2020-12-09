"""
Creates log files and data/fastq directories, it also notifies the user

path to data
/data/storix2/student/2019-2020/Thema06/project-data/How_to_deal_with_difficult_data/Data/

data files
SRR018013_1.fastq.gz  SRR018015.fastq.gz  SRR057599.fastq.gz   SRR1106122.fastq.gz  SRR1106139.fastq.gz
SRR018013_2.fastq.gz  SRR057598.fastq.gz  SRR1106118.fastq.gz  SRR1106138.fastq.gz  SRR1106140.fastq.gz

usage:
    python3 mkdirs /data/storix2/student/2019-2020/Thema06/project-data/How_to_deal_with_difficult_data/Data/

output:
    scanned_fastq_files.log     file
    scanned_data_path.log       file
    data                        directory
"""

import subprocess
import argparse

def log_data_files(data_path):
    """ Logs the names of the fastq data files to scanned_fastq_files.log"""
    with open('../logs/fastq_files.log', 'w') as file_obj:
        subprocess.run(["ls", data_path], text=True, stdout=file_obj)

def log_data_path(data_path):
    """ Logs the path of the fastq data files to scanned_data_path.log"""
    with open('../logs/data_path.log', 'w') as file_obj:
        file_obj.write(data_path)

def make_fastq_dirs():
    """ Makes data directories and names them based on their .fastq.gz file extension """
    with open('../logs/fastq_files.log') as file_obj:
        fastqdirs = ["../results/fastqc/"+file[0:-4] for file in file_obj]
        subprocess.run(["rm", "-vrf", "results/fastqc"], text=True) # remove if exist, notify user
        for dir in fastqdirs:
            subprocess.run(["mkdir", "-vp", dir], text=True) # make fastqc dirs, notify user
            
def make_trim_galore_dirs():
    """ Makes data directories and names them based on their .fastq.gz file extension """
    with open('../logs/fastq_files.log') as file_obj:
        fastqdirs = ["../results/trim_galore/"+file[0:-4] for file in file_obj]
        subprocess.run(["rm", "-vrf", "results/trim_galore"], text=True) # remove if exist, notify user
        for dir in fastqdirs:
            subprocess.run(["mkdir", "-vp", dir], text=True) # make fastqc dirs, notify user

def main():
    """ main """
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path")
    args = parser.parse_args()

    # remove log file if exist, otherwise create them and notify user
    subprocess.run("rm -vrf ../logs; mkdir -v ../logs", shell=True, executable="/bin/bash")
    log_data_files(args.data_path)
    log_data_path(args.data_path)
    make_fastq_dirs()


if __name__ == "__main__":
    main()

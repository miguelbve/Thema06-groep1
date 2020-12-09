"""
Creates log files and data/fastq directories, it also notifies the user

path to data
/data/storix2/student/2019-2020/Thema06/project-data/How_to_deal_with_difficult_data/Data/

data files
SRR018013_1.fastq.gz  SRR018015.fastq.gz  SRR057599.fastq.gz   SRR1106122.fastq.gz  SRR1106139.fastq.gz
SRR018013_2.fastq.gz  SRR057598.fastq.gz  SRR1106118.fastq.gz  SRR1106138.fastq.gz  SRR1106140.fastq.gz

usage:
    python3 mkdirs.py /data/storix2/student/2019-2020/Thema06/project-data/How_to_deal_with_difficult_data/Data/ /data/storix2/student/2020-2021/Thema06/project-data/

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

def log_storage_path(storage_path):
    with open('../logs/storage_path.log', 'w') as file_obj:
        file_obj.write(storage_path)

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
            subprocess.run(["mkdir", "-vp", dir], text=True)


## These dirs can be found in the external_storage path. For more info ##
def make_ref_genomes_dirs():
    with open('../logs/storage_path.log') as file_obj:
        dir = file_obj.readline()
        subprocess.run(["mkdir", "-vp", dir+"groep1/ref_genomes"], text=True)

def make_ref_genomes_index_dirs():
    with open('../logs/storage_path.log') as file_obj:
        dir = file_obj.readline()
        subprocess.run(["mkdir", "-vp", dir+"groep1/ref_genomes_index"], text=True)


def main():
    """ main """
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path")
    parser.add_argument("storage_path")
    args = parser.parse_args()

    # remove log file if exist, otherwise create them and notify user
    subprocess.run("rm -vrf ../logs; mkdir -v ../logs", shell=True, executable="/bin/bash")
    log_data_files(args.data_path)
    log_data_path(args.data_path)
    log_storage_path(args.storage_path)

    make_fastq_dirs()
    make_trim_galore_dirs()
    make_ref_genomes_dirs()
    make_ref_genomes_index_dirs()


if __name__ == "__main__":
    main()

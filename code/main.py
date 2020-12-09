"""
Main

usage:
    python3 main.py /data/storix2/student/2019-2020/Thema06/project-data/How_to_deal_with_difficult_data/Data/ /data/storix2/student/2020-2021/Thema06/project-data/
"""
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path")
    parser.add_argument("storage_path")
    args = parser.parse_args()

    # preprocess the data
    subprocess.run(f"python3 mkdirs.py {args.data_path} {args.storage_path}", shell=True, executable="/bin/bash")
    subprocess.run(f"python3 fastqc.py", shell=True, executable="/bin/bash")
    subprocess.run(f"python3 trim.py", shell=True, executable="/bin/bash")
    subprocess.run(f"python3 determine_genome.py", shell=True, executable="/bin/bash")

if __name__ == "__main__":
    main()
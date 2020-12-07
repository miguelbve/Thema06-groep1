"""
Execute efetch
"""

__date__ = "2020-12-6"

import subprocess
import tqdm

'esearch -db SRA -query "SRR1106139" | efetch -format native > second_temp.xml'

def get_fastq_queries():
    with open('../logs/fastq_files.log', 'r') as fastqlog:
        esearch_queries = [fastq[0:-10] for fastq in fastqlog if not "_" in fastq]
        fastqlog.seek(0)
        esearch_paired_queries = [fastq[0:-12] for fastq in fastqlog if "_" in fastq]
        return esearch_queries + esearch_paired_queries

def write_xmls(esearch_queries):
    for item in esearch_queries:
        subprocess.run(f'esearch -db SRA -query "{item}" | efetch -format native > ../logs/{item}.txt', shell=True, executable="/bin/bash")
    print("Writing xml files of the ")

def main():
    """ Main"""
    esearch_queries = get_fastq_queries()
    write_xmls(esearch_queries)

if __name__ == "__main__":
    main()
"""
Execute efetch
"""

__date__ = "2020-12-6"

import subprocess

'esearch -db SRA -query "SRR1106139" | efetch -format native > second_temp.xml'

def get_fastq_queries():
    with open('../logs/fastq_files.log', 'r') as fastqlog:
        esearch_queries = [fastq[0:-10] for fastq in fastqlog]
        return esearch_queries

def write_xmls(esearch_queries):
    for item in esearch_queries:
        subprocess.run(f'esearch -db SRA -query "{item}" | efetch -format native > ../logs/{item}.xml', shell=True, executable="/bin/bash")

def main():
    """ Main"""
    esearch_queries = get_fastq_queries()
    write_xmls(esearch_queries)

if __name__ == "__main__":
    main()
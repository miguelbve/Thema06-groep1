"""
Execute efetch
"""

__date__ = "2020-12-6"
__version__ = 2

import subprocess
from tqdm import tqdm


def get_fastq_queries():
    """ """
    with open('../logs/fastq_files.log', 'r') as fastqlog:
        esearch_queries = [fastq[0:-10] for fastq in fastqlog if not "_" in fastq]
        fastqlog.seek(0)
        esearch_paired_queries = [fastq[0:-12] for fastq in fastqlog if "_" in fastq]
        return esearch_queries + esearch_paired_queries

def write_txt(esearch_queries):
    """ Perform esearch and write outcome to txt file. Log the made txt files """
    data_paths = []
    print("Writing the output of esearch SRA to logs/*.txt")
    for item in tqdm(esearch_queries):
        subprocess.run(f'esearch -db SRA -query "{item}" | efetch -format native > ../logs/{item}.txt', 
                        shell=True, executable="/bin/bash")
        data_paths.append(f'{item}.txt \n')
    
    # write made txt file names to txt_files.log    
    with open('../logs/txt_files.log', 'w') as file_obj:
         for i in data_paths:
             file_obj.write(i)       
    file_obj.close()
    
    return data_paths

def determine_organism(data_paths):
    """ Read txt file and determine organism, return dictionary with query and organism """
    dict_txt = {}
    for i in data_paths:
        i = i.strip()
        with open(f'../logs/{i}') as txt:
            for line in txt:
                if line.startswith("<EXPERIMENT_PACKAGE>"):
                    index_first = line.find("organism")
                    line = line[index_first:]
                    index_last = line.find(">")
                    organism = line[:index_last]
        dict_txt[i[:-4]] = organism[10:-1]
    txt.close()
    return dict_txt


def main():
    """ Main"""
    esearch_queries = get_fastq_queries()
    data_paths = write_txt(esearch_queries)

    dict_organism = determine_organism(data_paths)
    print(dict_organism)

if __name__ == "__main__":
    main()

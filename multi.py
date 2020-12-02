"""

this reads fastq.gz files,
runs them trough fastqc,
and puts those folders trough multiqc



"""
import os


def fastqc(filename, datadir, outdir):
    command = 'fastqc --extract --outdir=' + outdir + ' ' + datadir + filename
    print(command)
    os.system(command)


def multiqc(fast, multi):
    command = 'multiqc -o ' + multi + ' ' + fast
    print(command)
    os.system(command)


def main():
    files = []
    fastoutdir = '/homes/mrsikkema/fastqcout'
    multioutdir = '/homes/mrsikkema/multiqcout'
    datadir = '/data/storix2/students/2020-2021/Thema06/project-data/How_to_deal_with_difficult_data/Data/'
    filelijst = os.listdir(datadir)
    for name in filelijst:
        if name.endswith('.fastq.gz'):
            files.append(name)
    #for filen in files:
    #    fastqc(filen, datadir, fastoutdir)
    multiqc(fastoutdir, multioutdir)
    

main()

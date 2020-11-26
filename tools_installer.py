"""
Pre-installed command-line tools on bioinf.nl:
Picard:             picard-tools
Hisat:              hisat2
FastQC:             fastqc
SAMtools:           samtools

After running this script the following command-line tools, will be installed and configured:
MultiQC:            multiqc
Cutadapt:           cutadapt
Trim Galore:        trim_galore
featureCounts:      featureCounts (from the Subread package)
"""

__author__ = "Miguel"
__date__ = "2020-11-26"


import subprocess

def install_tools():
    # change to the home directory, here the source files of the command-line tools will be installed
    subprocess.run(f"cd ~ && "
    # install Cutadapt    
    f"python3 -m pip install --user --upgrade cutadapt && "
    # install MultiQC
    f"pip3 install multiqc && "
    # install Trim Galore
    f"curl -LO https://github.com/FelixKrueger/TrimGalore/archive/0.6.6.zip && unzip 0.6.6.zip && rm -rf 0.6.6.zip && "
    # install the Subread package that includes featureCounts, exactSNP, subindel, subjunc, sublong, subread-align and subread-buildindex
    f"curl -LO https://sourceforge.net/projects/subread/files/subread-2.0.1/subread-2.0.1-Linux-x86_64.tar.gz &&" 
    f"tar -xzvf subread-2.0.1-Linux-x86_64.tar.gz && rm -rf subread-2.0.1-Linux-x86_64.tar.gz && "  
                   
    # adds source paths to .bash_profile, this allows the user of this program to run all the installed command line tools
    f"echo 'source ~/.bashrc\n"
    f"export PATH=$PATH:~/.local/bin\n"
    f"export PATH=$PATH:~/TrimGalore-0.6.6\n"
    f"export PATH=$PATH:~/subread-2.0.1-Linux-x86_64/bin' >> ~/.bash_profile && source ~/.bash_profile && "
    
    # change to the initial directory
    f"cd -", shell=True, executable="/bin/bash") # executes the commands through using the bash shell


def main():
    # Install all the required pipe line command line tools
    install_tools()


if __name__ == "__main__":
    main()

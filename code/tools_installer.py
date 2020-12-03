"""
Pre-installed command-line tools on bioinf.nl:
Picard:             picard-tools
HISAT:              hisat2
FastQC:             fastqc
SAMtools:           samtools

After running this script the following command-line tools, will be installed and configured:
MultiQC:            multiqc
Cutadapt:           cutadapt
Trim Galore:        trim_galore
featureCounts:      featureCounts (from the Subread package)
"""

__date__ = "2020-11-26"


import subprocess
import argparse

def install_tools():
    # change to the home directory, here the source files of the command-line tools will be installed
    subprocess.run(f"cd ~ && "
    # install Cutadapt    
    f"python3 -m pip install --user --upgrade cutadapt && "
    # install MultiQC
    f"pip3 install multiqc && "
    # install Trim Galore
    f"curl -LO https://github.com/FelixKrueger/TrimGalore/archive/0.6.6.zip && unzip 0.6.6.zip && rm -rf 0.6.6.zip && "
    # install Subread package that includes featureCounts, exactSNP, subindel, subjunc, sublong, subread-align and subread-buildindex
    f"curl -LO https://sourceforge.net/projects/subread/files/subread-2.0.1/subread-2.0.1-Linux-x86_64.tar.gz && " 
    f"tar -xzvf subread-2.0.1-Linux-x86_64.tar.gz && rm -rf subread-2.0.1-Linux-x86_64.tar.gz && "  
                   
    # create a .bash_profile, and add the paths that redirect to the installed tools
    f"echo 'source ~/.bashrc\n"
    f"export PATH=$PATH:~/.local/bin\n"
    f"export PATH=$PATH:~/TrimGalore-0.6.6\n"
    f"export PATH=$PATH:~/subread-2.0.1-Linux-x86_64/bin' > ~/.bash_profile && source ~/.bash_profile && exec bash && "
    
    # change to the initial directory
    f"cd -", shell=True, executable="/bin/bash") # executes the commands through using the bash shell


def uninstall_tools():
    # change to the home directory, here the source files of the command-line tools are installed
    subprocess.run(f"cd ~ && "
    # uninstall Cutadapt
    f"pip3 uninstall cutadapt && "
    # uninstall MultiQC
    f"pip3 uninstall multiqc && "
    # uninstall Trim Galore
    f"rm -rf TrimGalore-0.6.6 && "
    # uninstall Subread package that includes featureCounts, exactSNP, subindel, subjunc, sublong, subread-align and subread-buildindex
    f"rm -rf subread-2.0.1-Linux-x86_64 && "
    # remove the .bash_profile, since all the tools are uninstalled. We don't need the specified paths anymore.
    f"rm -rf .bash_profile && exec bash && source ~/.bashrc && "
    
    # change to the initial directory
    f"cd - ", shell=True, executable="/bin/bash")
    print("Successfully uninstalled TrimGalore-0.6.6\n"
          "Successfully uninstalled subread-2.0.1-Linux-x86_64")



def main():
    parser = argparse.ArgumentParser(description="install and configure missing cli tools for the M. Dubbelaar pipeline")
    parser.add_argument('-u', '--uninstall', help="uninstall and deconfigure cli tools for the M. Dubbelaar pipeline",
                        action='store_true')
    args = parser.parse_args()
    if args.uninstall:
        uninstall_tools()
    else:
        install_tools()


if __name__ == "__main__":
    main()

import os
import re

RED = "\033[91m"
RESET = "\033[0m"

def print_banner():
    os.system('clear')
    print("""
██████╗  █████╗  ██████╗██╗  ██╗██████╗  ██████╗  ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██████╔╝███████║██║     █████╔╝ ██║  ██║██║   ██║██║   ██║██████╔╝
██╔══██╗██╔══██║██║     ██╔═██╗ ██║  ██║██║   ██║██║   ██║██╔══██╗
██████╔╝██║  ██║╚██████╗██║  ██╗██████╔╝╚██████╔╝╚██████╔╝██║  ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                  
██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗               
██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗              
███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝              
██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗              
██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║    @VesperaIX     
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝              
               
Jika sudah menemukan indikasi shell backdoor / judi online mohon segera hapus dan diperbaiki keamanannya               
    """)
    
def load_wordlist(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error loading wordlist: {e}")
        return []

def scan_file(file_path, patterns):
    try:
        with open(file_path, 'r', errors='ignore') as file:
            content = file.read()
            for pattern in patterns:
                if re.search(pattern, content):
                    return pattern
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
    return None

def scan_directory(directory, backdoor_patterns, judi_patterns):
    backdoor_found = False
    judi_found = False

    print(f"Scanning directory: {directory}\n")
    for root, _, files in os.walk(directory):
        for file in files:
            if file in ['wordlist.txt', 'hunt.py', 'judol.txt']:
                continue 
            file_path = os.path.join(root, file)

            pattern_found = scan_file(file_path, backdoor_patterns)
            if pattern_found:
                print(f"{RED}[BACKDOOR DITEMUKAN]{RESET} File: {file_path} - Pattern: {pattern_found}")
                backdoor_found = True

            judi_pattern_found = scan_file(file_path, judi_patterns)
            if judi_pattern_found:
                print(f"{RED}[JUDI ONLINE DITEMUKAN]{RESET} File: {file_path} - Pattern: {judi_pattern_found}")
                judi_found = True

    if not backdoor_found:
        print("Tidak ditemukan backdoor\n")

    if not judi_found:
        print("Tidak ditemukan judi online\n")

if __name__ == "__main__":
    print_banner()

    backdoor_patterns = load_wordlist('wordlist.txt')

    judi_patterns = load_wordlist('judol.txt')

    scan_directory(os.getcwd(), backdoor_patterns, judi_patterns)

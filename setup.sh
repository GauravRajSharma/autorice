#!/bin/sh

# Check for necessary programs and architecture
# - Arch
# - pacman, git, yay, make, sed, stow, python3, pip, nodejs, npm

error() { clear; printf "ERROR:\\n%s\\n" "$1"; exit;}

check_requirements(){
    [ -z 'pacman']
}

parse_programs_file(){
    # Removed Comments
    # Trimmed White Spaces
    # Deleted Empty Lines
    sed '/^#d;/^\s*$/d' programs.csv > /tmp/program-dotfiles.csv
}

fetch_dotfiles(){
    pushd '~/Documents/'
    git clone 'https:www.github.com/GauravRajSharma/dotfiles.git'
    popd
}

run_installer(){
    chmod +x install.py
    python3 install.py
}

run_symbolic_linker(){
    pushd '~/Documents/dotfiles'
    make install
}


main(){
    check_requirements | error 'Please make sure you have installed pacman'
}
# Run stow on the ~/Documents/dotfiles
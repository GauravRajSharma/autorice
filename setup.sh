#!/bin/sh

# Check for necessary programs and architecture
# - Arch
# - pacman, git, yay, make, sed, stow, python3, pip, nodejs, npm

error() { clear; printf "ERROR:\\n%s\\n" "$1"; exit;}

check_requirements(){
    # if no pacman exits

    # if no git, yay,make sed, stow, python3, pip nodejs, npm -> get from pacman
}

parse_programs_file(){
    # Removed Comments
    # Trimmed White Spaces
    # Deleted Empty Lines
    sed '/^#d;/^\s*$/d' programs.csv > /tmp/programs-dotfiles.csv
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
    chmod +x install.sh
    ./install.sh
    popd
}


main(){
	check_requirements || error "Checking Requirements failed. Make sure you have installed pacman!"
	parse_program_file || error "Make sure installer folder consists programs.csv"
	run_installer || error "Installer file not found!"
	fetch_dotfiles || error "Unable to fetch dotfiles!"
	run_symbolic_linker || error "Configuration .config / .script files failed!"

}
# Run stow on the ~/Documents/dotfiles

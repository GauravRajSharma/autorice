import csv
from subprocess import call
from pathlib import Path

# Global Variables
file_ = f'/tmp/programs-dotfiles.csv'
file_ = f'install.csv'
git_programs_location = Path.home() / 'Documents/programs'


def print_app_profile(app_name, description):
    print(f'Installing | {app_name:<30} | {description}')


if __name__ == "_f_main__":
    with open(file=file_) as p_file:
        data = csv.reader(p_file, delimiter=',', quotechar='"')
        tags = ['', 'A', 'P', 'N']
        installer = {
            '': lambda app_name: f'sudo pacman -Sy --noconfirm {app_name}',
            'N': lambda app_name: f'sudo npm install {app_name} -g',
            'P': lambda app_name: f'sudo pip install {app_name}',
            'A': lambda app_name: f'yay -Sy --noconfirm {app_name}'
        }
        for tag, app_name, description in data:
            call(['clear'], shell=True)
            if tag in tags:
                print_app_profile(app_name, description)
                call(installer[tag](app_name), shell=True)
            if tag == 'G':
                continue
                path_app = app_name.split('/')[-1].split('.')[0]
                print_app_profile(path_app, description)
                if not git_programs_location.exists():
                    git_programs_location.mkdir(parents=True, exist_ok=True)
                call(
                    f'pushd {git_programs_location};git clone {app_name};pushd {path_app};sudo make install;popd; popd', shell=True)

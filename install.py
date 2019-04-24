import csv
from subprocess import call
from pathlib import Path

# Global Variables
# file = f'/tmp/program-dotfiles.csv'
file_test = f'./test/test.csv'
git_programs_location = f'$HOME/Documents/programs'
git_programs_test = f'$HOME/Documents/test'


def print_app_profile(app_name, description):
    print(f'|{app_name:<30}| {description}')


with open(file=file_test) as p_file:
    data = csv.reader(p_file, delimiter=',', quotechar='"')
    tags = ['', 'A', 'P', 'N']
    installer = {
        '': lambda app_name: f'sudo pacman -Sy --noconfirm {app_name}',
        'N': lambda app_name: f'sudo npm install {app_name} -g',
        'P': lambda app_name: f'sudo pip install {app_name}',
        'A': lambda app_name: f'yay -Sy --noconfirm {app_name}'
    }
    for tag, app_name, description in data:
        if tag in tags:
            print_app_profile(app_name, description)
            call(installer[tag](app_name), shell=True)
        if tag == 'G':
            git_programs_path = Path(git_programs_test)
            # print(app_name)
            if git_programs_path.exists():
                call(
                    f'pushd ;git clone {app_name}; popd;popd', shell=True)
                print('Yes')
            else:
                print('NO')


def main():
    pass


if __name__ == '__main__':
    main()

import re
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlopen

base_url = 'http://docs.beyondshop.cloud/'
start_file = 'api.raml'


_re_include = re.compile(r"!include '?([^\n']+)'?\n")


def download_file(url: Path, destination: Path):
    with urlopen(url) as resp, destination.open('wb')  as output:
        shutil.copyfileobj(resp, output)


def extract_includes(text):
    for match in _re_include.finditer(text):
        yield match.group(1)


def process(relpath, root_folder):
    path = root_folder / relpath
    path.parent.mkdir(exist_ok=True)
    
    parent_relative  = path.parent.relative_to(root_folder)
     
    url = '{}{}'.format(base_url, relpath)
    download_file(url, path)
    
    if path.suffix == '.json':
        return
    
    with path.open('r') as f:
        content = f.read()

    for include in extract_includes(content):
        process(parent_relative / include, root_folder)


def generate_code():
    pass


def patch_code():
    pass
   

def main():
    with TemporaryDirectory() as tmp:
        root_folder = Path(tmp)
        process(start_file, root_folder)
        generate_code()
        patch_code()

if __name__ == '__main__':
    main()

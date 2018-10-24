import re
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from subprocess import call

base_url = 'http://docs.beyondshop.cloud/'
start_file = 'api.raml'

_here = Path(__file__).parent.resolve()
go_raml_path = _here / 'go-raml'
generted_code_path = _here.parent / 'epages_client'

_re_include = re.compile(r"!include '?([^\n']+)'?\n")


def download_file(url, destination: Path):
    print("DOWNLOADING", url, ' to ', destination)
    with urlopen(url) as resp, destination.open('wb')  as output:
        shutil.copyfileobj(resp, output)


def extract_includes(text):
    for match in _re_include.finditer(text):
        yield match.group(1)


def recursive_download(relpath, root_folder):
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
        recursive_download(parent_relative / include, root_folder)


def generate_code(root_folder):
    print("REMOVING: ", generted_code_path)
    shutil.rmtree(generted_code_path, ignore_errors=True)
    call([go_raml_path, 'client', '--language', 'python', '--dir', generted_code_path, '--ramlfile', root_folder / start_file])


def patch_code():
    file_path = (generted_code_path / 'shops_service.py')
    print("PATCHING: " , file_path)
    text = file_path.read_text()
    patched = text.replace(' status.provisioningCompleted', ' status_provisioningCompleted')
    file_path.write_text(patched)
   

def main():
    with TemporaryDirectory() as tmp:
        root_folder = Path(tmp)
        recursive_download(start_file, root_folder)
        generate_code(root_folder)
        patch_code()

if __name__ == '__main__':
    main()

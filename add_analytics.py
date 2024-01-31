import os;
from bs4 import BeautifulSoup;

def process_html_files(folder):
    # Loop through all the files and subfolders in the folder
    for entry in os.scandir(folder):
        # If the entry is a file and has a .html extension
        if entry.is_file() and entry.name.endswith(".html"):
            # Open the file in read mode
            with open(entry.path, "r") as file:
                # Read the file content
                content = file.read()
                soup = BeautifulSoup(content)
                script_first = soup.new_tag('script', src="https://www.googletagmanager.com/gtag/js?id=G-1NJ6SJZJK2")
                script_first.attrs['async'] = None
                script_second = soup.new_tag('script')
                script_second.string = 'window.dataLayer = window.dataLayer || []; \n function gtag(){dataLayer.push(arguments);} \ngtag(\'js\', new Date()); \n gtag(\'config\', \'G-1NJ6SJZJK2\');'
                soup.head.insert(0, script_first)
                soup.head.insert(1, script_second)
                print(soup.prettify)
            
            with open (entry.path, 'w') as destination:
                destination.write(soup.prettify(formatter='html'))
        # If the entry is a subfolder
        elif entry.is_dir():
            # Recursively call the function on the subfolder
            process_html_files(entry.path)

# Call the function on the current folder
process_html_files(".")

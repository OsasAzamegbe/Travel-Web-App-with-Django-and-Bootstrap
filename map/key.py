import os


def get_key():
    # modify to the directory where the text document containing your key is stored
    # modify to the document's name
    file_dir = r"C:\Users\Osamudiamen\Documents\Vscode Projects"

    file_name = r"\googleAPIkey.txt"

    doc = open(file_dir + file_name, mode='r')
    key = doc.read()
    doc.close()
    return key
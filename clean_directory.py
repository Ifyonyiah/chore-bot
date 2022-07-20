import os
import argparse


def Clean():
    parser = argparse.ArgumentParser(description = "Clean up directory and sort files into folders.")
    parser.add_argument("--path", type = str, default='.', help="Directory path to be cleaned")
    args = parser.parse_args()
    path = args.path

    print(f"cleaning up directory {path}")

    dir_content = os.listdir(path)

    path_dir_content = [os.path.join(path,doc) for doc in dir_content]

    docs = [doc for doc in path_dir_content if os.path.isdir(doc)]
    folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

    moved = 0
    created_folders = []
    print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")
    for doc in docs:
        full_doc_path, filetype = os.path.splitext(doc)
        doc_path = os.path.dirname(full_doc_path)
        doc_name = os.path.basename(full_doc_path)

        print(filetype)
        print(full_doc_path)
        print(doc_path)
        print(doc_name)
        break


        if doc_name == "clean_directory" or doc_name.startswith('.'):
            continue

    subfolder_path = os.path.join(path, filetype[1:].lower())
    if subfolder_path not in folders:
        #create folder
        try:
            os.mkdir(subfolder_path)
            created_folders.append(subfolder_path)
            print(f"Folder {subfolder_path} created.")
        except FileExistsError as err:
            print(f"Folder already exists at {subfolder_path}... {err}")

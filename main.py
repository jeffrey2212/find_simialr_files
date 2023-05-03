import os,sys 
import argparse
from difflib import SequenceMatcher

def is_similar(a, b, threshold=0.8):
    s = SequenceMatcher(None, a, b)
    return s.ratio() > threshold

def find_similar_files(folder, extensions):
    files = [f for f in os.listdir(folder) if any(f.endswith(ext) for ext in extensions)]
    similar_files = []

    for i, file1 in enumerate(files):
        for j, file2 in enumerate(files[i + 1:]):
            if is_similar(file1, file2):
                similar_files.append((file1, file2))

    return similar_files

def main():
    parser = argparse.ArgumentParser(description='Find similar filenames in a folder')
    parser.add_argument('-folder', type=str, required=True, help='Folder to search for similar filenames')
    parser.add_argument('-ext', type=str, required=True, help='Comma-separated list of file extensions to search for (e.g., ".ckpt,.safetensors")')
    parser.add_argument('-threshold', type=float, default=0.8, help='Threshold for similarity (default: 0.8)')

    args = parser.parse_args()

    folder = args.folder
    extensions = args.ext.split(',')
    threshold = args.threshold

    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        sys.exit(1)

    similar_files = find_similar_files(folder, extensions)

    if similar_files:
        print(f"Similar files in folder '{folder}' with extensions {extensions}:")
        for file1, file2 in similar_files:
            print(f"{file1} - {file2}")
    else:
        print(f"No similar files found in folder '{folder}' with extensions {extensions}.")

if __name__ == "__main__":
    main()

#Sample usage
# python find_similar_files.py -folder /path/to/your/folder -ext .ckpt,.safetensors

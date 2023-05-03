# Find Similar Filenames

This script is used to find pairs of similar filenames in a folder. It supports searching for multiple file extensions.

## Usage

1. Install Python 3.x if you haven't already.

2. Run the script using the following command:

'''
    python find_similar_files.py -folder /path/to/your/folder -ext .ckpt,.safetensors
'''

Replace `/path/to/your/folder` with the path to the folder you want to search in, and `.ckpt,.safetensors` with a comma-separated list of file extensions you want to search for. You can also adjust the similarity threshold by adding the `-threshold` argument, followed by a float value (e.g., `-threshold 0.9`).

## Example

'''
    python find_similar_files.py -folder /path/to/your/folder -ext .ckpt,.safetensors -threshold 0.9
'''


This command will list pairs of similar filenames with any of the specified extensions (`.ckpt` and `.safetensors`) in the specified folder, using a similarity threshold of 0.9.

## Note

This script uses a simple string comparison method to determine the similarity between filenames. It may not be perfect for all use cases, but it should be helpful for detecting similar filenames in most situations.

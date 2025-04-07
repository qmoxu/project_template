import pandas as pan
def input_from_console():
    """
    Read input from the console.

    Returns:
        str: Entered by the user input.
    """
    return input("Enter text: ")

def input_from_file(file_path):
    """
    Read input from a file using built-in file handling.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def input_from_file_pandas(file_path):
    """
    Read input from a file using the pandas lib.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    df = pan.read_csv(file_path, sep ="\t", header=None, skip_blank_lines=True)
    return df.to_string(index=False, header = False)
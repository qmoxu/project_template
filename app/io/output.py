def output_to_console(given_text):
    """
    Outputs text to the console.

    Args:
        given_text (str): The text to be printed.
    """
    print(given_text)

def output_to_file(file_name, text):
    """
    Writes text to a file using built-in file handling.

    Args:
        text (str): The text to be written to the file.
        filename (str): The name of the file to write to.
    Returns:
        file_name (str): The name of the file where the text was written.
    """
    with open(file_name, 'w') as file:
        file.write(text)
    return file_name
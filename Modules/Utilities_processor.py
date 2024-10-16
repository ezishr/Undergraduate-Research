from Packages import *

def read_directory_contents(path):
    """
    Read the contents of a directory
    @param path String: the path of the directory to be processed
    @return: a list
    """
    # Get list of contents in the folder
    contents = os.listdir(path)
    return contents


def write_string_to_file(text, file_name):
    """
    Writes a string to a file.

    @param text string: The string to write.
    @param file_name: The name of the file to write to.
    @return bool: True if file was written, False if an exception was thrown
    """
 
    status = True
    try:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        '''The try block is used to catch any exceptions that might occur during the file writing process.
        os.makedirs(os.path.dirname(file_name), exist_ok=True) ensures that the directory for the file exists. If it doesn’t, it creates the directory. The exist_ok=True parameter prevents an error if the directory already exists.'''

        # Open the file in write mode  
        with open(file_name, 'w', encoding='utf-8') as file: 
            '''The file is opened in write mode ('w'). If the file does not exist, it will be created. If it does exist, its contents will be overwritten.'''
            file.write(text) # writes the string text to the file
        #print(f"String written to file: {filename}")
        
    except Exception as e:
        status = False
        print(f"Utilities.write_string_to_file(): Error writing to {file_name}: {e}")
        
    return status
# file_detector.py

def detect_file_type(filename):
    """
    Detects the file type based on extension.
    
    Args:
        filename (str): The name of the file
        
    Returns:
        str: The file type/extension
    """
    extension = filename.split('.')[-1]
    return extension.lower()

if __name__ == '__main__':
    # Test the function
    test_file = 'example.pdf'
    file_type = detect_file_type(test_file)
    print(f'File type: {file_type}')

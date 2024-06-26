import argparse


def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
        None
    Returns:
        parse_args() -data structure that stores the command line arguments object
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Argument 1: path to folder
    parser.add_argument('--dir', type=str, default='pet_images/', help='path to folder of pet images')

    # Argument 2: CNN model architecture to use
    choices = ['vgg', 'alexnet', 'resnet']
    parser.add_argument('--arch', type=str, default='vgg', choices=choices, help='CNN model architecture to use')

    # Argument 3: file that contains dognames
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='filename')

    return parser.parse_args()

import os
import json
import logging


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
 
logger.setLevel(logging.DEBUG)


def read_json(filepath:str) -> dict:
    """This function takes filepath of a JSON file as a parameters, reads the file and returns the json object

    Args:
        filepath (str): Filepath to a JSON file

    Returns:
        dict: JSON object read from the JSON file
    """
    try:
        with open(filepath, "r") as file:
            obj = json.load(file)
            logging.debug("JSON file exists...")
            return obj
    except FileNotFoundError:
        logging.debug("JSON file not found")




def main():
    pass



if __name__ == "__main__":
    main()
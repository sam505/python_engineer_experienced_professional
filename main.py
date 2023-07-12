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
            logger.debug("JSON file exists...")
            return obj
    except FileNotFoundError:
        logger.debug("JSON file not found")


def generate_schema(obj: dict) -> dict:
    """Function takes a JSON object and returns the schema of the JSON object

    Args:
        obj (dict): JSON object

    Returns:
        dict: JSON object representing the schema of the JSON object passed to the function
    """
    TYPES = {
        type(1): 'integer',
        type(1.2): 'float',
        type("abc"): 'string',
        type(True): 'boolean',
        type([]): 'enum',
        type({}): 'array',
        }

    logger.debug("Generating schema...")
    schema = {}

    schema_format = {
        "type": "",
        "tag": "",
        "description": "",
        "required": False
    }

    for obj_key in obj:
        schema_format["type"] = TYPES[type(obj[obj_key])]
        schema[obj_key] = schema_format

    return schema



def main():
    folder = "data"
    for filename in os.listdir(folder):
        read_json(os.path.join(folder, filename))

    pass



if __name__ == "__main__":
    main()
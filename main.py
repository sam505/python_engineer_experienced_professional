import os
import json
import logging

# add logger to help with debugging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')
logger = logging.getLogger()
 
logger.setLevel(logging.DEBUG)

# Data types to be used when generating schema
TYPES = {
        type(1): 'integer',
        type(1.2): 'float',
        type("abc"): 'string',
        type(True): 'boolean',
        type([]): 'array',
        type({}): 'object',
        }


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
            logger.debug(f"JSON file {filepath} exists...")
            return obj
    except FileNotFoundError:
        logger.error("JSON file not found")


def generate_schema(obj: dict) -> dict:
    """Function takes a JSON object and returns the schema of the JSON object

    Args:
        obj (dict): JSON object

    Returns:
        dict: JSON object representing the schema of the JSON object passed to the function
    """
    
    logger.debug(f"Generating schema for {obj}...")
    schema = {}
    try:
        for obj_key in obj.keys():
            # initialize a skeleton with the required keys and required key set to false
            schema_format = {
            "type": "",
            "tag": "",
            "description": "",
            "required": False
            }
            new_obj = obj[obj_key]
            logger.debug(f"Generating for key: {obj_key}")

            attribute_type = TYPES[type(new_obj)]

            # only captute attributes ONLY in message key
            if attribute_type in ["array", "object"] and obj_key != "attributes":
                logger.info(f"Getting schema through loop for {new_obj}...", )
                if attribute_type == "object":
                    schema_format["properties"] = generate_schema(new_obj)
                else:
                    schema_format["items"] = generate_schema(new_obj)
            
            schema_format["type"] = attribute_type
            schema[obj_key] = schema_format

    except AttributeError:
        schema = []
        for new_obj in obj:
            # initialize a skeleton with the required keys and required key set to false
            schema_format = {
            "type": "enum",
            "tag": "",
            "description": "",
            "required": False
            }

            attribute_type = TYPES[type(new_obj)]

            # only captute attributes ONLY in message key
            if attribute_type in ["array", "object"]:
                logger.info(f"Getting schema through loop for {new_obj}...", )
                schema_format["properties"] = generate_schema(new_obj)
                schema_format["type"] = "array"
            
            schema.append(schema_format)
        
    
    return schema


def save_schema(obj: dict, filename: str) -> str:
    """Gets the generated schema object and the filename of the JSON file and then dumps the JSON object in the schema folder

    Args:
        obj (dict): generated schema dictionary object
        filename (str): filename of the JSON file

    Returns:
        str: path of the saved JSON schema file 
    """
    schema_dir = "schema"

    # check if schema dir exists and create if it does not exist
    if not os.path.isdir(schema_dir):
        os.mkdir(schema_dir)

    new_filename = filename.replace("data", "schema")
    filepath = os.path.join(schema_dir, new_filename)
    with open(filepath, "w") as file:
            json.dump(
                {
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "type": "object",
                    "properties": obj
                }
                , file, indent=4)
    logger.debug(obj)

    return None


def main():
    data_folder = "data"
    for filename in os.listdir(data_folder):
        json_obj = read_json(os.path.join(data_folder, filename))
        schema = generate_schema(json_obj)
        save_schema(schema, filename)



if __name__ == "__main__":
    main()
import json
from typing import Any, Dict

def save_dict_to_file(dictionary: Dict[Any, Any], filename: str) -> None:
    """
    Saves a dictionary to a file in JSON format.
    
    Args:
        dictionary (Dict[Any, Any]): The dictionary to save.
        filename (str): The path of the file to save the dictionary.
    """
    with open(filename, 'w') as file:
        json.dump(dictionary, file, indent=4)
    print(f"Dictionary saved to {filename}")

def load_dict_from_file(filename: str) -> Dict[Any, Any]:
    """
    Loads a dictionary from a JSON file.
    
    Args:
        filename (str): The path of the file to load the dictionary from.
        
    Returns:
        Dict[Any, Any]: The loaded dictionary.
    """
    try:
        with open(filename, 'r') as file:
            dictionary = json.load(file)
        print(f"Dictionary loaded from {filename}")
        return dictionary
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {filename}.")
        return {}

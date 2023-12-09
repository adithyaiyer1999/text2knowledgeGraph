import json
import yaml

def add_color_to_node(json_obj, path, color="red"):
    """
    Add color attribute to the node at the specified path in a JSON object.
    Handles cases where the path points to an item within a list.
    """
    keys = path.split('/')
    for key in keys[:-1]:
        if isinstance(json_obj, list):
            key = int(key)  # Convert to integer for list indices
        json_obj = json_obj.setdefault(key, {})

    last_key = keys[-1]
    if isinstance(json_obj, list):
        last_key = int(last_key)  # Convert to integer for list indices

    # Check if the last key points to a dictionary or a list of dictionaries
    target_node = json_obj.get(last_key)
    if isinstance(target_node, dict):
        target_node["color"] = color
    elif isinstance(target_node, list):
        for item in target_node:
            if isinstance(item, dict):
                item["color"] = color
            else:
                # Handle the case where the item in the list is not a dictionary
                print(f"Cannot add color to the item in the list at path: {path}. Item is not a dictionary.")
    else:
        # Handle the case where the target is neither a dictionary nor a list of dictionaries
        print(f"Cannot add color to the path: {path}. Target is not a dictionary or a list of dictionaries.")


def find_differences(json1, json2, path=''):
    differences = []
    for key in json2:
        new_path = f"{path}/{key}" if path else key
        if key not in json1:
            differences.append(new_path)
        elif isinstance(json1[key], dict) and isinstance(json2[key], dict):
            # Recurse into dictionaries
            differences.extend(find_differences(json1[key], json2[key], new_path))
        elif json1[key] != json2[key]:
            # Different value for the same key
            differences.append(new_path)
    return differences

def update_json_with_color(json_obj, differences):
    """
    Update JSON object by adding color to the specified paths.
    """
    for path in differences:
        add_color_to_node(json_obj, path)

def find_difference_change_color(oldjson, updatedjson):
    if isinstance(oldjson, str):
        oldjson = yaml.safe_load(oldjson)
    updatedjson = yaml.safe_load(updatedjson)
    print("oldjson::\n",oldjson)
    print("updatedjson::\n",updatedjson)
    differences = find_differences(oldjson, updatedjson)
    update_json_with_color(updatedjson, differences)
    return updatedjson

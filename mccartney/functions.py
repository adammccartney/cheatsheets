
def make_key_function_list(ordered_dict):
    """
    Takes an abjad.OrderedDict 
    returns a list of the keys
    """
    key_functions = []
    keys = ordered_dict.keys()
    for key in keys:
        key_functions.append(key)
    return key_functions

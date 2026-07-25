# First FreeCodeCamp project 
# works on creating a code that allows a fictional user to modify a pre-defined set of configurations

def add_setting(dictionary, input_tuple):
    key, value = tuple(i.lower() if isinstance(i, str) else i for i in input_tuple)

    if key in dictionary:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else: 
        dictionary[key] = value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'

def update_setting(dictionary, input_tuple):
    key, value = tuple(i.lower() if isinstance(i, str) else i for i in input_tuple)

    if key in dictionary:
        dictionary[key] = value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(dictionary, input_key):
    key = input_key.lower() if isinstance(input_key, str) else input_key
    
    if key in dictionary:
        del dictionary[key]
        return f'Setting \'{key}\' deleted successfully!'
    else:
        return 'Setting not found!'

def view_settings(dictionary):
    if dictionary == dict():
        return 'No settings available.'
    else:
        final_string = 'Current User Settings:\n'
        for k, v in dictionary.items():
            final_string += f'{k.capitalize()}: {v}\n'
        return final_string


test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}



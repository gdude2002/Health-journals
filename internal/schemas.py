__author__ = 'Gareth Coles'

import datetime

USER = {
    "username": str,  # Username of the user
    "salt": str,  # Salt used to create password hash
    "hash": str,  # The password hash (password, salt and hashing algorithm)
    "email": str,  # Email address.
    "gender": str,  # Gender. This is a custom field, not a set of options.
    "dob": datetime.datetime,  # Date of birth.
    "menstruates": bool,  # Because trans, etc.
    "cur_target": str,  # Weight gain, loss, etc.
    "cur_target_params": dict,  # Depends on the type of target.
    "public": bool,  # If you need privacy, you got it.
}

TARGET = {
    "type": str,  # Type of target.
    "params": list,  # List of needed parameters.
    "entry_params": list,  # List of entry-specific params.
}

ENTRY = {
    "username": str,
    "meals": list,
    "date": datetime.datetime,
    "target": str,
    "target_params": dict,
}

schemas = {
    "users": USER,
    "targets": TARGET,
    "entries": ENTRY,
}

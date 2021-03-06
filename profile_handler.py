import json, os

_PROFILE_DIR = 'profiles/'
_PROFILE_EXT = '.profile'
PROFILE_KEY_NAME = 'NAME'
PROFILE_KEY_SOURCES = 'SOURCES'

# TODO: handle case of null profiles! e.g. when trying to delete one
# TODO: optimise
# TODO: ensure consistent use of variable names, underscores etc throughout entire project
# TODO: improve use of just passing round loaded_profiles dict -- MAKE A CLASS

if not os.path.isdir(_PROFILE_DIR):
    os.mkdir(_PROFILE_DIR)

def get_profile_files():
    profile_list = list()
    dirlist = os.listdir(_PROFILE_DIR)
    for item in dirlist:
        path = _PROFILE_DIR + item
        if os.path.isfile(path):
            if path.endswith(_PROFILE_EXT):
                profile_list.append(path)
    return profile_list

def write_profiles(loaded_profiles):
    to_delete = list()
    for profile_name in loaded_profiles.keys():
        profile = loaded_profiles[profile_name]
        file_path = _PROFILE_DIR + profile_name + _PROFILE_EXT
        if profile[PROFILE_KEY_NAME] != "":
            f = open(file_path, 'w')
            json.dump(profile, f)
            f.close()
        else:
            os.remove(file_path)
            to_delete.append(profile_name)
    for profile_name in to_delete:
        del loaded_profiles[profile_name]

def load_profiles():
    loaded_profiles = dict()
    profiles = get_profile_files()

    for profile in profiles:
        f = open(profile, 'r')
        str = f.read()
        raw = json.loads(str)
        name = raw[PROFILE_KEY_NAME]
        loaded_profiles[name] = raw
        f.close()
    return loaded_profiles

def add_profile(loaded_profiles, name, sources_active):
    profile_dict = dict()
    profile_dict[PROFILE_KEY_NAME] = name
    profile_dict[PROFILE_KEY_SOURCES] = sources_active
    loaded_profiles[name] = profile_dict

def edit_profile(loaded_profiles, name, new_profile):
    if name not in loaded_profiles:
        raise ValueError('Cannot edit profile by the name %s as it does not exist!' % name)
    loaded_profiles[name] = new_profile



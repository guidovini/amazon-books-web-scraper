# ─── LIBRARIES ──────────────────────────────────────────────────────────────────
import re


regex = re.compile(r"[\[\]'\",]+|[\\]|\bn\b|[\\]|\bt\b")


# ─── PROGRAM ────────────────────────────────────────────────────────────────────
def filter_url_strings(raw_data):
    # regex_filter = regex.split(raw_data)
    regex_filter = raw_data
    string_filter = ' '.join(''.join(regex_filter).split()) if regex_filter else None
    return string_filter


def filter_url_lists(list_data):
    new_list = []

    for i in range(len(list_data)):
        new_value = filter_url_strings(list_data[i])      
        if new_value:
            new_list.append(new_value)
            
    return new_list

## Filter recives either a string or a list of strings.
def filter_values(data, id):
    if isinstance(data, str):
        list_data = data.split('\'')
    else:
        list_data = data

    new_list = filter_url_lists(list_data)

    if id == 's':
        return ' - '.join(new_list)
    elif id == 'f':
        if len(new_list) == 1:
            return ' - '.join(new_list)
        elif new_list == []:
            return []
        else:
            return new_list[0] 
    elif id == 'l':
        return new_list
    else:
        return new_list

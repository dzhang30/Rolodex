import re
import collections
import json


def get_entries_from_file(filename):
    """
    Get the raw list of personal info entries from the given file
    :param filename: path to data file
    :return: list of personal info entries
    """
    entries = []
    with open(filename, mode='r') as data_file:
        for entry in data_file:
            entry = entry[:-1]                 # strip the newline character at the end of each entry string/line
            entries.append(entry.split(', '))  # convert each entry string into a list and append to entries

    return entries


def normalize_entries(file_entries):
    """
    Return a valid, formatted dictionary object with entries from the file
    :param file_entries: list of personal information entries (list of lists)
    :return: valid, formatted dictionary object with 'entries' and 'errors' as keys
    """
    data = {'entries': [], 'errors': []}
    rx = _create_regex_matches()

    for index, entry in enumerate(file_entries):
        entry_length = len(entry)
        if entry_length == 5 and rx['lastname'].match(entry[0]) and rx['firstname'].match(entry[1]) and \
                rx['phone1'].match(entry[2]) and rx['color'].match(entry[3]) and rx['zipcode'].match(entry[4]):
            # 1st input format in the readme_instructions pdf (Lastname, Firstname, (703)-742-0996, Blue, 10013)
            _update_data(entry, data, 1)
        elif entry_length == 5 and rx['firstname'].match(entry[0]) and rx['lastname'].match(entry[1]) and \
                rx['zipcode'].match(entry[2]) and rx['phone2'].match(entry[3]) and rx['color'].match(entry[4]):
            # 3rd input format in the readme_instructions pdf (Firstname, Lastname, 10013, 646 111 0101, Green)
            _update_data(entry, data, 3)
        elif entry_length == 4 and rx['fullname'].match(entry[0]) and rx['color'].match(entry[1]) and \
                rx['zipcode'].match(entry[2]) and rx['phone2'].match(entry[3]):
            # 2nd input format in the readme_instructions pdf (Firstname Lastname, Red, 11237, 703 955 0373)
            _update_data(entry, data, 2)
        else:
            data['errors'].append(index)

    data['entries'].sort(key=lambda e: (e['lastname'], e['firstname']))  # (ascending) sort by last name then first name

    return data


def _create_regex_matches():
    """
    Creates a dictionary that helps to check if each entry attribute matches the correct syntax/input format.
    :return: a dictionary of regex matching for each entry attribute based on the different input formats
    """
    regex_matches = {
        'firstname': re.compile('^[A-Z][a-z]+$|^[A-Z][a-z]+ [A-Z]\.$'),  # first name format: 'Daniel' or 'Daniel T.'
        'lastname': re.compile('^[A-Z][a-z]+$'),                         # last name format: 'Zhang'
        'fullname': re.compile('^[A-Z][a-z]+ [A-Z][a-z]+$|^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'),  # 'Daniel Zhang' or 'Daniel T. Zhang'
        'phone1': re.compile('^\([0-9]{3}\)-[0-9]{3}-[0-9]{4}$'),        # phone number format: (111)-222-3333
        'phone2': re.compile('^[0-9]{3} [0-9]{3} [0-9]{4}$'),            # phone number format: 111 222 333
        'color': re.compile('^[a-z]+$|^[a-z]+ [a-zA-Z]+$'),              # color format: 'aqua' or 'aqua marine'
        'zipcode': re.compile('^[0-9]{5}$')                              # zipcode format: 60647
    }

    return regex_matches


def _update_data(entry, data, input_format_number):
    """
    Updates our data dictionary with the correctly formated entry
    :param entry: a personal information entry (list)
    :param data: our dictionary object with 'entries' and 'errors' as keys (dict)
    :param input_format_number: the input format number based on the PDF (int)
        1). Lastname, Firstname, (703)-742-0996, Blue, 10013
        2). Firstname Lastname, Red, 11237, 703 955 0373
        3). Firstname, Lastname, 10013, 646 111 0101, Green
    """
    if input_format_number == 1:
        entry = {
            'lastname': entry[0],
            'firstname': entry[1],
            'phonenumber': _normalize_phone_number(entry[2]),
            'color': entry[3],
            'zipcode': entry[4]
        }
    elif input_format_number == 2:
        entry = {
            'firstname': entry[0].split()[0],
            'lastname': entry[0].split()[1],
            'color': entry[1],
            'zipcode': entry[2],
            'phonenumber': _normalize_phone_number(entry[3])
        }
    elif input_format_number == 3:
        entry = {
            'firstname': entry[0],
            'lastname': entry[1],
            'phonenumber': _normalize_phone_number(entry[3]),
            'zipcode': entry[2],
            'color': entry[4]
        }

    sorted_entry = collections.OrderedDict(sorted(entry.items()))  # sort each dictionary/entry by key (alphabetically)
    data['entries'].append(sorted_entry)


def _normalize_phone_number(phone_number):
    """
    Transform the different acceptable phone number strings into the correct format based in the PDF
    '(111)-222-3333' -> '111-222-3333'
    '111 222 3333' -> '111-222-3333'
    :param phone_number: phone number string
    :return: normalized phone number string that matches with whats given in the readme_instructions PDF
    """
    rx = _create_regex_matches()
    if rx['phone1'].match(phone_number):
        phone_number = phone_number.replace('(', '')
        phone_number = phone_number.replace(')', '')
    elif rx['phone2'].match(phone_number):
        phone_number = phone_number.replace(' ', '-')

    return phone_number


def run_percolate_app():
    """
    write a valid, formatted JSON object to result.out.
    The JSON representation should be indented with two spaces and the keys should be sorted in ascending order.
    """
    entries = get_entries_from_file('data/data.in')
    normalized_entries = normalize_entries(entries)
    normalized_json_entries = json.dumps(normalized_entries, sort_keys=True, indent=2)  # convert entries to json format

    with open('data/result.out', 'w+') as outfile:
        outfile.write(normalized_json_entries)

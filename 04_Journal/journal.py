"""
This is the journal module
"""

import os

def load(name):
    """
    This method creates and loads a new journal.

    :param name: This Base name of the journal to load.
    :return: A new journal structure to populatee with the file data.
    """
    data = []
    filename = get_full_pathname(name)
    if(os.path.exists(filename)):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def save(name, journal_data):
    """
    This Method saves a journal strucutre

    :param name: This Base name of the journal to save.
    :param journal_data: Journal Data to save
    :return: None
    """

    filename = get_full_pathname(name)
    print("...... speichern unter {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join(".", "journals/", name + ".jrl"))
    return filename


def add_entry(text, data):
    return data.append(text)
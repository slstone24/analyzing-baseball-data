import csv

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table

# print(read_csv_as_nested_dict('master1.csv', 'player' , ',', '"'))
# print("")

def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    data = read_csv_as_nested_dict(info["masterfile"], info["playerid"],
                                    info["separator"], info["quote"])
    name_stat_list = []
    for item in top_ids_and_stats:
        playerid = item[0]
        num = '{:.3f}'.format(item[1])
        if playerid in data:
            firstname = data[playerid]['firstname']
            lastname = data[playerid]['lastname']
            line = "{} --- {} {}".format(num, firstname, lastname)
            name_stat_list.append(line)
    return name_stat_list




print(lookup_player_names({'masterfile': 'master1.csv', 'battingfile': '', 'separator': ',', 'quote': '"',
'playerid': 'player', 'firstname': 'firstname', 'lastname': 'lastname', 'yearid': 'year',
'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles', 'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks',
'battingfields': ['atbats', 'hits', 'doubles', 'triples', 'homers', 'walks']},
[('player0', 0.1)]))

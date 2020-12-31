
import csv

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sep', 'Oct', 'Nov', 'Dec')

def dictparse(csvfilename, keyfield):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True)
        for row in csvreader:
            table[row[keyfield]] = row
    return table

print(dictparse('master1.csv', 'player'))


with open('master1.csv', 'r', newline = '') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        print(row)


# TEST EXAMPLES

# print(top_player_ids({'masterfile': '', 'battingfile': '', 'separator': ',', 'quote': '"',
# 'playerid': 'player', 'firstname': 'firstname', 'lastname': 'lastname', 'yearid': 'year',
# 'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles', 'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks',
# 'battingfields': ['atbats', 'hits', 'doubles', 'triples', 'homers', 'walks']},
# [{'player': 'player0', 'homers': '5', 'doubles': '20', 'walks': '25', 'atbats': '300', 'triples': '1', 'year': '2020', 'hits': '108'},
# {'player': 'player1', 'homers': '4', 'doubles': '5', 'walks': '10', 'atbats': '499', 'triples': '3', 'year': '2020', 'hits': '170'},
# {'player': 'player2', 'homers': '20', 'doubles': '18', 'walks': '85', 'atbats': '513', 'triples': '5', 'year': '2020', 'hits': '129'},
# {'player': 'player5', 'homers': '22', 'doubles': '3', 'walks': '37', 'atbats': '197', 'triples': '2', 'year': '2020', 'hits': '67'},
# {'player': 'player6', 'homers': '18', 'doubles': '33', 'walks': '25', 'atbats': '542', 'triples': '7', 'year': '2020', 'hits': '166'},
# {'player': 'player7', 'homers': '10', 'doubles': '19', 'walks': '27', 'atbats': '500', 'triples': '2', 'year': '2020', 'hits': '161'},
# {'player': 'player8', 'homers': '25', 'doubles': '42', 'walks': '30', 'atbats': '589', 'triples': '13', 'year': '2020', 'hits': '176'}],
# batting_average, 1))

# print(lookup_player_names({'masterfile': 'master1.csv', 'battingfile': '', 'separator': ',', 'quote': '"',
# 'playerid': 'player', 'firstname': 'firstname', 'lastname': 'lastname', 'yearid': 'year',
# 'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles', 'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks',
# 'battingfields': ['atbats', 'hits', 'doubles', 'triples', 'homers', 'walks']},
# [('player0', 0.1)]))
#
# print("")
#
# print(lookup_player_names({'masterfile': 'master2.csv', 'battingfile': '', 'separator': ',', 'quote': '"',
# 'playerid': 'playerID', 'firstname': 'nameFirst', 'lastname': 'nameLast', 'yearid': 'yearID',
# 'atbats': 'AB', 'hits': 'H', 'doubles': '2B', 'triples': '3B', 'homeruns': 'HR', 'walks': 'BB',
# 'battingfields': ['AB', 'H', '2B', '3B', 'HR', 'BB']},
# [('guerrvl01', 0.88385), ('berkmla01', 0.2832854)]))

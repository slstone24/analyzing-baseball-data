def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    dict_of_dict = {}
    for row in statistics:
        if row[playerid] not in dict_of_dict.keys():
            inner_dict = {field:int(row[field]) for field in fields}
            inner_dict[playerid] = row[playerid]
            dict_of_dict[row[playerid]]= inner_dict

        else:
            exis_inner_dict = dict_of_dict[row[playerid]]
            curr_inner_dict = {field:int(row[field]) for field in fields}
            dict_combined = {field: (exis_inner_dict.get(field, 0) +
            curr_inner_dict.get(field, 0)) for field in fields}
            dict_combined[playerid]= row[playerid]
            dict_of_dict[row[playerid]]= dict_combined
    return dict_of_dict

# statistics =   [
#        {'player': '1', 'stat1': '3', 'stat2': '4', 'stat3': '5'},
#        {'player': '1', 'stat1': '2', 'stat2': '1', 'stat3': '8'},
#        {'player': '1', 'stat1': '5', 'stat2': '7', 'stat3': '4'},
#        {'player': '2', 'stat1': '6', 'stat2': '8', 'stat3': '10'},
#        {'player': '2', 'stat1': '4', 'stat2': '2', 'stat3': '16'},
#        {'player': '2', 'stat1': '10', 'stat2': '14', 'stat3': '8'}
#        ]
#
# playerid = 'player'
#
# fields = ['stat1', 'stat2']
#
#
# print(aggregate_by_player_id(statistics, playerid, fields))

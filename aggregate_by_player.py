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
    nested_dict = {}
    aggr_stats_dict = {}
    num = 0
    for dict in statistics:
        for item in dict:
            aggr_stats_dict[playerid] = dict[playerid]
        for statid in fields:
            if statid in dict:
                num += int(dict[statid])
                aggr_stats_dict[statid] = num
    nested_dict[dict[playerid]] = aggr_stats_dict
    return nested_dict

print(aggregate_by_player_id([{'player': '1', 'stat1': '3', 'stat2': '4', 'stat3': '5'},
{'player': '1', 'stat1': '2', 'stat2': '1', 'stat3': '8'},
{'player': '1', 'stat1': '5', 'stat2': '7', 'stat3': '4'}],
'player', ['stat1']))

print(aggregate_by_player_id([{'player': '1', 'stat1': '3', 'stat2': '4', 'stat3': '5'},
{'player': '1', 'stat1': '2', 'stat2': '1', 'stat3': '8'},
{'player': '1', 'stat1': '5', 'stat2': '7', 'stat3': '4'}],
'player', ['stat1', 'stat2']))


statistics =   [
   {'player': '1', 'stat1': '3', 'stat2': '4', 'stat3': '5'},
   {'player': '1', 'stat1': '2', 'stat2': '1', 'stat3': '8'},
   {'player': '1', 'stat1': '5', 'stat2': '7', 'stat3': '4'},
   {'player': '2', 'stat1': '6', 'stat2': '8', 'stat3': '10'},
   {'player': '2', 'stat1': '4', 'stat2': '2', 'stat3': '16'},
   {'player': '2', 'stat1': '10', 'stat2': '14', 'stat3': '8'}
   ]

playerid = 'player'

fields = ['stat1']


print(aggregate_by_player_id(statistics, playerid, fields))

def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    input_data = read_csv_as_list_dict(info['battingfile'], info['separator'],
                                                                info['quote'])
    player_id = info['playerid']
    player_fields = info['battingfields']
    aggr_stats = aggregate_by_player_id(input_data, player_id, player_fields)
    top_stats = top_player_ids(info, aggr_stats, formula, numplayers)
    stat_list = lookup_player_names(info, top_stats)
    return stat_list

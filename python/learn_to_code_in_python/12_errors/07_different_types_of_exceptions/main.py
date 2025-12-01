"""
Assignment:
Take a look at the get_player_record function. It raises an exception for negative player_ids.

Complete the process_player_record() function so that it:

1. Calls get_player_record(player_id) and returns its result if no error occurs.
2. If an IndexError is raised, returns the string: index is too high.
3. If any other exception happens, returns the error object itself.
"""

def process_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e


# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

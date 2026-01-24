"""
Assignment:
Fix the get_player_record function. If the given player_id doesn't exist, it currently just passes. 
Instead, it should raise (but not handle) an error to alert the caller that the player doesn't exist. The exception should say player id not found.

The tests will call the get_player_record function, and will handle the exception you raise.
"""

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    else:
        raise Exception("player id not found")

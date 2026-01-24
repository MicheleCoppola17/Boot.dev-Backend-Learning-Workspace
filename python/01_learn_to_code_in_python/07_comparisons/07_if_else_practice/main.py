"""
Assignment:
There is a bug in the check_high_score function! Add the proper conditional statement to fix the bug. If the names match, return the string:

'You are the highest scoring player!'

Otherwise, return:

'You are not the highest scoring player!'

(The <= operator compares strings alphabetically and works when names are equal (e.g., "lane" <= "lane" is True).)
"""

def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"

"""
A "guild" is a team of 2-4 players. Here are the guild-specific permissions:

- can_invite - Leftmost bit (0b1000)
- can_kick - Second to leftmost bit (0b0100)
- can_enter_dungeon - Second to rightmost bit (0b0010)
- can_surrender - Rightmost bit (0b0001)
When players are in a guild together, they gain all the permissions of all the other members of the guild!

For example, if:

- Jack has the can_invite permission: 0b1000
- Jill has the can_kick permission: 0b0100
Then, when they are partied together, they should both have the can_invite and can_kick permissions: 0b1100.

ASSIGNMENT:
Complete the calculate_guild_perms function. 
It takes as input four binary numbers representing the separate permissions of each member of the guild: glorfindel, galadriel, elendil and elrond. 
It should return a single binary number that represents the combined permissions of all the members of the guild.

Use a series of bitwise "or" operations to calculate the superset of all the member's permissions.
"""

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond

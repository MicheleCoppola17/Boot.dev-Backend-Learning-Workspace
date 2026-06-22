"""
Assignment
We need to display a user's last job title on their profile.

Implement the last_work_experience function. 
It takes a list of our user's work history (strings) and returns the last place they worked.

Assume the list is ordered from oldest to most recent.
If the list is empty, return None.
"""

def last_work_experience(work_experiences: list[str]) -> str | None:
    if len(work_experiences) > 0:
        return work_experiences[len(work_experiences) - 1]
    return None
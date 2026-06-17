"""
Assignment
Implement the count_marketers function. It should accept a list of strings (job titles) and return the number of users who've set their title to "marketer". 
LockedIn users sometimes use different casing in their titles, so make sure to account for that.

count = count_marketers(['programmer', 'marketer', 'doctor', 'marketer'])
print(count)
# prints "2"
"""

def count_marketers(job_titles: list[str]) -> int:
    counter = 0
    for title in job_titles:
        if title.lower() == 'marketer':
            counter += 1
    return counter

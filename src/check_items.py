# Gets and checks the current items
from projectv2.project import Project
import os

# Get the environment variable for the API token
api_key = os.environ.get("GH_API_KEY")
print("API Key: %s" % api_key[0:5])

p = Project()
p.get("psecio", 1)

# for each of the items in the project, check to see if all of the tracks are closed
items = p.get_items()
for item in items:
    # print(item.title)
    tracks = item.trackedIssues

    # if the length of the tracks is 0, then we can skip this item
    if len(tracks) == 0:
        print('Not tracking any issues for %s' % item.title)
        continue

    all_closed = True
    for track in tracks:
        if not track.closed:
            all_closed = False  

    if all_closed:
        print("All tracks closed for %s" % item.title)
        item.close()
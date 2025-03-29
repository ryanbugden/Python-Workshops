lunch_votes = {
    "Xinyuan": "Shake Shack",
    "Roberto": "",
    "Hay": "Ramen",
    "Yihuang": "",
    "Ryan": "Shake Shack"
    }
    
votes = {}

for student_name, lunch_place in lunch_votes.items():
    if lunch_place in votes.keys():
        votes[lunch_place] += 1
    else:
        votes[lunch_place] = 1
        
print(votes)
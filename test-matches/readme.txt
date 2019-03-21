-1st 5 objects in match.participants are team 100 (blue team)
-2nd 5 objects in match.participants are team 200 (red team)

match.participants[0] through match.participants[4]
match.participants[5] through match.participants[9]


for participant in match.participants
    participant.timeline.lane == "TOP"
    participant.timeline.lane == "JUNGLE"
    participant.timeline.lane == "MIDDLE"
    participant.timeline.lane == "BOTTOM" && participant.timeline.role == "DUO_CARRY"
    participant.timeline.lane == "BOTTOM" && participant.timeline.lane == "SUPPORT"
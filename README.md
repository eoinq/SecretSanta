# Secret Santa

This python programme will randomly assign gift givers and receivers among a group of participants subject to
- no two people belonging to the same group are matched
- no giver will have the same recipient in from the previous max_no_years, if it is not possible to find a valid match max_no_years will be recursively decreased by 1 until a valid set of pairings is found.

# Secret Santa

A python programme to perform an annual random pairing of givers and receivers among a group of participants. 


There are two optional constraints on the pairings:
* No giver will be assigned a recipient who they had in the previous max_no_years. The programme automatically records the pairing each year, os that in subsequent   in a given year for 
* 

subject to two constraints:
- no giver is assigned a recipient which they   previous max_no_years. If max_no_years is too high, it is not possible to find a valid match max_no_years will be recursively decreased by 1 until a valid set of pairings is found.



This python programme will randomly assign gift givers and receivers among a group of participants subject to
- no two people belonging to the same group are matched
- no giver will have the same recipient in from the previous max_no_years, if it is not possible to find a valid match max_no_years will be recursively decreased by 1 until a valid set of pairings is found.

# Secret Santa

A python programme to perform the annual Secret Santa ritual. The code generates a random pairing of givers and receivers among a collection of participants, automatically emailing each giver with news of their recipient, and saves a record to file so that in subsequent years we can inforce variety upon who gets who. 

The code allows for two optional constraints on the pairings:
* Each participant may be assigned a `group`, such that no two participants belonging to the same `group` are paired. This can be useful if there are couples or family units among the participants, and it is desired that pairings within these are avoided. 
* A parameter `max_no_years` may be set, so that no giver will be re-assigned a recipient they had in the previous `max_no_years` years. If `max_no_years` is too high for a valid match to be found within reasonable time, the programme recursively decreases `max_no_years` by 1 until a valid set of pairings is obtained.

This code programme requires configuration of SMTP settings for an email address to distribute the mails. One option is to use a gmail account, in which case it is necessary to turn on 2-step verification in order to set up a custom password for the SMTP settings.

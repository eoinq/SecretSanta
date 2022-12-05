# Secret Santa

A python programme to perform an annual random pairing of givers and receivers among a collection of participants. The givers are automatically emailed with news of their recipient, and a record is saved to file. 

There are two optional constraints on the pairings:
* Each participant may be assigned a group, such that no two participants belonging to the same group are paired.
* No giver will be re-assigned a recipient they had in the previous `max_no_years` years. If `max_no_years` is too high for a valid match to be found, the programme recursively decreases `max_no_years by 1 until a valid set of pairings is obtained.

This code programme requires configuration of SMTP settings for an email address to distribute the mails. One option is to use a gmail account, in which case it is necessary to turn on 2-step verification in order to set up a custom password.

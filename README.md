# Secret Santa

A python programme to perform the annual Secret Santa ritual. The code generates a random pairing of givers and receivers among a collection of participants, automatically emailing each giver with news of their recipient, and saves a record to file so that in subsequent years we can inforce variety upon who gets who. 

The code allows for two optional constraints on the pairings:
* Each participant may be assigned a `group`, such that no two participants belonging to the same `group` are paired. This can be useful if there are couples or family units among the participants, and it is desired that pairings within these are avoided. 
* A parameter `max_no_years` may be set, so that no giver will be re-assigned a recipient they had in the previous `max_no_years` years. If `max_no_years` is too high for a valid match to be found within reasonable time, the programme recursively decreases `max_no_years` by 1 until a valid set of pairings is obtained.

The code programme requires configuration of SMTP settings for an email address to distribute the mails. One option is to use a gmail account, in which case it is necessary to turn on 2-step verification in order to set up a custom password for the SMTP settings.


# Setup

The programme is configured by editing the `config.py` file. The entries required here are:
* `participants`: a list of participants, with each specified by a python dictionary with entries for `name` and `email`. In addition one can optionally specify a `group` entry for a participant if it is wished that no two participants with the same `group` value are paired.
* `max_no_years`: a non-negative integer specifying the number of intervening years for which a giver cannot get the same recipient twice. If not specified the default value is zero. If `max_no_years` is too high for a match to be found it will be recursively decreased  by 1 until a valid set of pairings is obtained.
* `message_settings`: a python dictionary containing the specifications of the Secret Santa mail, namely 'message_from', 'message_subject', and 'message_text'.
* `mail_settings`: a python dictionary specifying the SMTP settings for the email address used to distribute the Secret Santa mails, namely `host`, `port`, `mail` and `password`.


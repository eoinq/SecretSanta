# Secret Santa

A python programme to perform an annual Secret Santa ritual. The code generates a random pairing of givers and receivers among a collection of participants, automatically emails each giver with news of their recipient, and saves a record to file.

The code allows for two optional constraints on the pairings:
* Each participant may be assigned a `group`, such that no two participants belonging to the same `group` are paired. This can be useful if there are couples or family units among the participants, and it is desired that pairings within these are avoided. 
* A parameter `max_no_years` may be set, such that no giver will be re-assigned a recipient they had in the previous `max_no_years` years. If `max_no_years` is too high for a valid match to be found within reasonable time, the programme recursively decreases `max_no_years` by 1 until a valid set of pairings is obtained.

The code programme requires configuration of SMTP settings for an email address to distribute the mails. One option is to use a gmail account, in which case it is necessary to turn on 2-step verification in order to set up a custom password for the SMTP settings.


# Setup

The programme is configured by editing the `config.py` file. The entries required here are:
* `participants`: a list of participants, with each specified by a python dictionary with entries for `name` and `email`. In addition one can optionally specify a `group` entry for a participant if it is wished that no two participants with the same `group` value are paired.
* `max_no_years`: a non-negative integer specifying the number of intervening years for which a giver cannot get the same recipient twice. If `max_no_years` is too high for a match to be found it will be recursively decreased  by 1 until a valid set of pairings is obtained.
* `message_settings`: a python dictionary containing the specifications of the Secret Santa mail, namely 'message_from', 'message_subject', and 'message_text'.
* `mail_settings`: a python dictionary specifying the SMTP settings for the email address used to distribute the Secret Santa mails, namely `host`, `port`, `mail` and `password`.


# Execution

There are four execution options as follows.

### Random pairing

```
$ python secretsanta.py --random-pairing
```

Samples a random valid pairing, and prints the result for inspection.


### Send a test email to ensure SMTP settings are working

```
$ python secretsanta.py --test-mail test_address@mail.com
```

Sends a test email to `test_address@mail.com` to ensure that the SMTP setting are correctly configured. Also allows for inspection of formatting of the Secret Santa mail

### Official

```
$ python secretsanta.py --official
```

Performs the official run. Generates a valid pairing, sends out the notification mails to the participants, and saves a record to file in a folder called `previous` (creating it if necessary).


### Retrieve pairing 

```
$ python secretsanta.py --retrieve-pairing year
```

Allows one to check the official pairing from a given `year`. The user will be prompted for the `name` of the giver of interest, and can access the complete pairing by entering ALL.

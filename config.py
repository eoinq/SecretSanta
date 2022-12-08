################################################################################
# The participants are specified as a list of python dictionaries. Each 
# participant must have 'name' and 'email' entries. One can also optionally 
# enter a 'group' for a participant, such that no two participants with the same
# value of group will be matched. 
################################################################################ 

participants = [
    {'name':'John', 'email':'john@mail.com', 'group':'JM'},
    {'name':'Mary', 'email':'mary@mail.com', 'group':'JM'},
    {'name':'Fiachra', 'email':'fiachra@mail.com', 'group':'FN'},
    {'name':'Niamh', 'email':'niamh@mail.com', 'group':'FN'},
    {'name':'Eamonn', 'email':'eamonn@mail.com', 'group':'ES'},
    {'name':'Sarah', 'email':'sarah@mail.com', 'group':'ES'},
    {'name':'Tom', 'email':'tom@mail.com', 'group':'TL'},
    {'name':'Lucia', 'email':'lucia@mail.com', 'group':'TL'},
    {'name':'Seamus Nolan', 'email':'seamusn@mail.com', 'group':'SKB'},
    {'name':'Kevin', 'email':'kevin@mail.com', 'group':'SKB'},
    {'name':'Belinda', 'email':'belinda@mail.com', 'group':'SKB'},
    {'name':'Seamus Flynn', 'email':'seamus@mail.com', 'group':'SFlynn'},
    {'name':'Maeve', 'email':'maeve@mail.com'},
    {'name':'Gwen', 'email':'gwen@mail.com'},
]    
    
################################################################################
# A non-negative integer specifying the number of intervening years for which a
# giver cannot get the same recipient twice. If max_no_years is too high for a 
# match to be found it will be recursively decreased by 1 until a valid set of 
# pairings is obtained. To turn this option off set max_no_years to 0.
################################################################################    

max_no_years = 5


################################################################################
# Settings for the official Secret Santa email. Here {year}, {giver_name} and
# {receiver_name} will be replaced by their real values.
################################################################################

message_settings = {
    'message_from': "Mr. Elf",
    'message_subject': "Secret Santa {year}!",
    'message_text': """\
Dear {giver_name},

Congratulations, this year you are Secret Santa for {receiver_name}.

Happy searching!
"""
}


################################################################################
# SMTP configuration settings.
################################################################################

mail_settings = {
        'host': "smtp.example_mail.com",
        'port': 587,
        'mail': "secretsanta@mail.com",
        'password': "pwd12345"
}




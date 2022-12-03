participants = [
    {'name':'John', 'group':'JM', 'email':'john@mail.com'},
    {'name':'Mary', 'group':'JM', 'email':'mary@mail.com'},
    {'name':'Fiachra', 'group':'FN', 'email':'fiachra@mail.com'},
    {'name':'Niamh', 'group':'FN', 'email':'niamh@mail.com'},
    {'name':'Seamus', 'group':'Se', 'email':'seamus@mail.com'},
    {'name':'Maeve', 'group':'Ma', 'email':'maeve@mail.com'},
    {'name':'Eamonn', 'group':'ES', 'email':'eamonn@mail.com'},
    {'name':'Sarah', 'group':'ES', 'email':'sarah@mail.com'},
]    
    

max_no_years = 5


message_settings = {
    'message_from': "Mr. Elf",
    'message_subject': "Secret Santa!",
    'message_text': """\
Dear {giver_name},

Congratulations, this year you are Secret Santa for {receiver_name}.

Happy searching!
"""
}


mail_settings = {
        'host': "smtp.example_mail.com",
        'port': 587,
        'mail': "secretsanta@mail.com",
        'password': "pwd12345"
}




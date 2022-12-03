participants = [
    {'name':'John', 'group':'JM', 'email':'john@mail.com'},
    {'name':'Mary', 'group':'JM', 'email':'mary@mail.com'},
    {'name':'Fiachra', 'group':'FN', 'email':'fiachra@mail.com'},
    {'name':'Niamh', 'group':'FN', 'email':'niamh@mail.com'},
    {'name':'Seamus Flynn', 'group':'Se', 'email':'seamus@mail.com'},
    {'name':'Maeve', 'group':'Ma', 'email':'maeve@mail.com'},
    {'name':'Eamonn', 'group':'ESTL', 'email':'eamonn@mail.com'},
    {'name':'Sarah', 'group':'ESTL', 'email':'sarah@mail.com'},
    {'name':'Tom', 'group':'ESTL', 'email':'tom@mail.com'},
    {'name':'Lucia', 'group':'ESTL', 'email':'lucia@mail.com'},
    {'name':'Seamus Nolan', 'group':'SKB', 'email':'seamusn@mail.com'},
    {'name':'Kevin', 'group':'SKB', 'email':'kevin@mail.com'},
    {'name':'Belinda', 'group':'SKB', 'email':'belinda@mail.com'},
    {'name':'Gwen', 'group':'Gw', 'email':'gwen@mail.com'},
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




participants = [
    {'name':'John', 'email':'john@mail.com', 'group':'JM'},
    {'name':'Mary', 'email':'mary@mail.com', 'group':'JM'},
    {'name':'Fiachra', 'email':'fiachra@mail.com', 'group':'FN'},
    {'name':'Niamh', 'email':'niamh@mail.com', 'group':'FN'},
    {'name':'Eamonn', 'email':'eamonn@mail.com', 'group':'ESTL'},
    {'name':'Sarah', 'email':'sarah@mail.com', 'group':'ESTL'},
    {'name':'Tom', 'email':'tom@mail.com', 'group':'ESTL'},
    {'name':'Lucia', 'email':'lucia@mail.com', 'group':'ESTL'},
    {'name':'Seamus Nolan', 'email':'seamusn@mail.com', 'group':'SKB'},
    {'name':'Kevin', 'email':'kevin@mail.com', 'group':'SKB'},
    {'name':'Belinda', 'email':'belinda@mail.com', 'group':'SKB'},
    {'name':'Seamus Flynn', 'email':'seamus@mail.com', 'group':'SFlynn'},
    {'name':'Maeve', 'email':'maeve@mail.com'},
    {'name':'Gwen', 'email':'gwen@mail.com'},
]    
    

max_no_years = 5


message_settings = {
    'message_from': "Mr. Elf",
    'message_subject': "Secret Santa {year}!",
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




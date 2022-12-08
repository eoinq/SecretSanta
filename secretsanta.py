#!/usr/bin/env python3

import argparse
import datetime
from random import sample
import os
import pickle
import smtplib

year = datetime.date.today().year


def unique_names_check(participants):
    unique_names = set([participant['name'] for participant in participants])
    assert len(unique_names) == len(participants), "ERROR: There are duplicate names among the participants."


class Pairing():
    
    def __init__(self, participants):
        shuffled_participants = sample(participants, len(participants))
        self.pairs = list(zip(participants, shuffled_participants))
        
    def no_group_matches(self):
        for (giver, receiver) in self.pairs:
            try:
                if giver['group'] == receiver['group']:
                    return False
            except:
                if giver['name'] == receiver['name']:
                    return False
        return True
                
    def no_recent_matches(self, recent_matches):
        for (giver, receiver) in self.pairs:
            if receiver['name'] in recent_matches[giver['name']]:
                return False
        return True
    
    def write_to_file(self):
        folder_name = 'previous'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        pickle.dump(self.pairs, open(f"{folder_name}/pairs_{year}.dat", "wb"))
            
    def send_secret_santa_mails(self, mail):
        for (giver, receiver) in self.pairs:
            print("Need to uncomment send_secret_santa_mails!")
            mail.send_secret_santa_mail(giver, receiver)
    
    
def create_pairing(participants, max_no_years, counter_cutoff=100000):
    
    if max_no_years == -1:
        raise Exception("ERROR: no pairing found")
    
    recent_matches = collect_recent_matches(participants, max_no_years)
    
    for counter in range(counter_cutoff):        
        pairing = Pairing(participants)
        if pairing.no_group_matches() and pairing.no_recent_matches(recent_matches):
            print(f"Match found at attempt {counter} with no repeat matches from previous {max_no_years} years.")
            return pairing
    
    print(f"No pairing found with no repeat matches from previous {max_no_years} years. May need to increase counter_cutoff.")
    pairing = create_pairing(participants, max_no_years-1)
    return pairing


def collect_recent_matches(participants, max_no_years):
    
    recent_matches = dict()
    for participant in participants:
        recent_matches[participant['name']] = []

    for i in range(max_no_years):
            previous_year = year-1-i
            try:
                previous_pairing = pickle.load( open(f"previous/pairs_{previous_year}.dat", "rb" ) )
                for (giver, receiver) in previous_pairing:
                    recent_matches[giver['name']].append(receiver['name'])
            except:
                print(f"Missing file for {previous_year}")
                continue
                
    return recent_matches


def retrieve_pairing(retrieve_year):
    try:
        pairs = pickle.load( open(f"previous/pairs_{retrieve_year}.dat", "rb" ) )
        names = {giver['name']: receiver['name'] for (giver, receiver) in pairs}
        input_name = str(input("If pairing for a single giver is wanted enter their name, otherwise enter ALL:\n"))
        if input_name == 'ALL':
            for name in names:
                print(f"{name} -> {names[name]}")
        else:
            try:
                print(f"{input_name} -> {names[input_name]}")
            except:
                print(f"No entry for a participant named: {input_name}")                
    except:
        print(f"No file found file for {retrieve_year}")


class Mail():

    def __init__(self, mail_settings, message_settings):
        self.port = mail_settings['port']
        self.smtp = mail_settings['host']
        self.email = mail_settings['mail']
        self.password = mail_settings['password']
        self.message_from = message_settings['message_from']
        self.message_subject = message_settings['message_subject']
        self.message_text = message_settings['message_text']
        
    def compose_message(self, giver, receiver): 
        giver_name = giver['name']
        giver_email = giver['email']
        receiver_name = receiver['name']
        
        message = \
            f'From: {self.message_from} <{self.email}>\n' \
            f'To: {giver_name} <{giver_email}>\n' \
            f'Subject: {self.message_subject}"\n\n' \
            f'{self.message_text}\n'

        message = message.replace('{year}', str(year))
        message = message.replace('{giver_name}', giver_name)
        message = message.replace('{receiver_name}', receiver_name)

        return message
 
    def send_mail(self, email, message, flag):        
        try:
            server = smtplib.SMTP(self.smtp, self.port)
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, email, message.encode('utf-8'))
            server.close()       
            print(f'{flag}: Successfully mailed {email}')
        except Exception as e:
            print(f'{flag}: FAILED to mail {email}\n{e}')

    def send_secret_santa_mail(self, giver, receiver):
        message = self.compose_message(giver, receiver)
        self.send_mail(giver['email'], message, flag='Official mail')
        
    def send_test_mail(self, email):
        giver = {'name': 'Tester', 'email': email}
        receiver = {'name': 'Santa'}
        message = self.compose_message(giver, receiver)
        self.send_mail(email, message, flag='Test')

        
def parse_arguments():
    parser = argparse.ArgumentParser(description='Secret Santa')

    parser.add_argument('--official',
        dest='official',
        action='store_true',
        help='Officially send out all the secret santa emails')

    parser.add_argument('--test-mail',
        dest='testmail',
        type=str,
        help='Send a test email to EMAIL to check SMTP settings')
    
    parser.add_argument('--random-pairing',
        dest='randompairing',
        action='store_true',
        help='Print out a sampled valid pairing')
    
    parser.add_argument('--retrieve-pairing',
        dest='retrievepairing',
        type=int,
        help='Retrieve pairing record for a given YEAR')

    return parser.parse_args()
        
        
if __name__ == '__main__':
    
    import config
    args = parse_arguments()
    
    unique_names_check(config.participants)                  
    
    if args.official:
        pairing = create_pairing(config.participants, config.max_no_years)
        
        pairing.write_to_file()
        
        mail = Mail(config.mail_settings, config.message_settings)
        pairing.send_secret_santa_mails(mail)
        
    if args.testmail:
        mail = Mail(config.mail_settings, config.message_settings)
        mail.send_test_mail(args.testmail)
    
    if args.randompairing:
        pairing = create_pairing(config.participants, config.max_no_years)
        for (giver, receiver) in pairing.pairs:
            print(f"{giver['name']} -> {receiver['name']}")
            
    if args.retrievepairing:
        retrieve_year = args.retrievepairing
        retrieve_pairing(retrieve_year)

        
 

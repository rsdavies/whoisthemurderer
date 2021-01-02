#!/usr/bin/env python3
import pandas as pd
import os
import pickle
from email.mime.text import MIMEText
from apiclient import errors
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import argparse

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']


def make_email(email_text, addressee):
    """
    Makes the email to send
    :param addressee: The address of the person you are sending this email to
    :return: An object containing a base64url encoded email object.
    """

    message = MIMEText(email_text)
    message['to'] = addressee
    message['from'] = 'me'
    message['subject'] = "Important Murder Mystery Party Information"

    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_email(message):
    """
    Sends an email using the gmail api
    :return:
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_id.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    try:
        message = (service.users().messages().send(userId='me', body=message)
                   .execute())
        print('Message Sent - Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def main(email_csv):
    """
    Reads the csv of email address, randomly selects a murderer
    and emails participants to tell them if they are the murder!
    :param email_csv: The csv file containing the email addresses of participants
    :return:
    """
    email_text_murderer = """You are the MURDERER! Can you convince the other guests you're innocent?"""

    email_text_participant = """You are an innocent bystander! Can you work out who the murder is?"""

    emails = pd.read_csv(email_csv, header=None, names=['email'])

    the_murderer = emails.sample(n=1)

    the_suspects = emails[~emails.index.isin(the_murderer.index)]

    murderer_message = make_email(email_text_murderer, the_murderer['email'].values[0])

    send_email(murderer_message)

    for id, suspect in the_suspects.iterrows():
        suspect_message = make_email(email_text_participant, suspect['email'])
        send_email(suspect_message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Randomly pick a murderer and email them")
    parser.add_argument('emails', metavar="FILE", type=str, help="text file with email per row")

    args = parser.parse_args()
    main(args.emails)

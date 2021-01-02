# whoisthemurderer
A program to randomly select a murder from your murder mystery party attendees. 

You'll need to set yourself up to use the gmail api, following [this google tutorial](https://developers.google.com/gmail/api/quickstart/python)
Should give you a `credentials.json` which needs to be in the `whoisthemurderer` directory. 

Alternatively you can go and create a new google developer project and get a `client_id.json`

Next populate the `participant_emails.csv` with the addresses of your participants.

Finally run the program using `python email_sender.py`. 

The first time it should open a browser and ask you to authenticate. 

Note you'll be able to see the emails in your sent folder, so be good and don't cheat!



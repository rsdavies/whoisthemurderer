# whoisthemurderer
A program to randomly select a murder from your murder mystery party attendees. 
Required: A gmail account and a python 3 environment. 

You'll need to set yourself up to use the gmail api, following [this google tutorial](https://developers.google.com/gmail/api/quickstart/python)
Should give you a `credentials.json` which needs to be in the `whoisthemurderer` directory. 
Alternatively you can go and create a new google developer project and get a `client_id.json`

Make `email_sender.py` executable using `chmod +x email_sender.py`. 
Now make a text file with each participant's email in it, one per line. 
See `participant_emails.csv` for an example. 

Now run the program with `./email_sender.py <email_file>`

The first time it should open a browser and ask you to authenticate. 

Note you'll be able to see the emails in your sent folder, so be good and don't cheat!



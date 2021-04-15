# $ docker run -it python:3.8 bash
# Start a dummy smtp server
# $ python -m smtpd -n -c DebuggingServer localhost:1025&
# Execute the script to see the output on screen of mails being sent to each member in the specified groups
# $ python email_sending_to_groups.py

import smtplib
from email.mime.text import MIMEText
from contextlib import suppress

def send_email(
    subject,
    message,
    from_addr,
    *to_addrs,
    host="localhost",
    port=1025,
    headers=None
):
    '''
    Method to send mail to specified emails
    '''
    headers = headers if headers else {}

    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email["To"]
        email["To"] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()

from collections import defaultdict

class MailingList:
    """Manage groups of e-mail addresses for sending e-mails."""
    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()

    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)

    def save(self):
        with open(self.data_file, "w") as file:
            for email, groups in self.email_map.items():
                file.write("{} {}\n".format(email, ",".join(groups)))

    def load(self):
        self.email_map = defaultdict(set)
        with suppress(IOError):
            with open(self.data_file) as file:
                for line in file:
                    email, groups = line.strip().split(" ")
                    groups = set(groups.split(","))
                    self.email_map[email] = groups

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups): 
        groups = set(groups) 
        emails = set() 
        for e, g in self.email_map.items(): 
            if g & groups: 
                emails.add(e) 
        return emails

    def send_mailing(
        self, subject, message, from_addr, *groups, headers=None
    ):
        emails = self.emails_in_groups(*groups)
        send_email(
            subject, message, from_addr, *emails, headers=headers
        )

if __name__ == "__main__":
        with MailingList("emails.db") as m: 
        # Then, create a few fake email addresses and groups, along the lines of:

            m.add_to_group("friend1@example.com", "friends")
            m.add_to_group("friend2@example.com", "friends")
            m.add_to_group("family1@example.com", "family")
            m.add_to_group("pro1@example.com", "professional")  
            # Finally, use a command like this to send emails to specific groups:
            
            m.send_mailing("A Party",
            "Friends and family only: a party", "me@example.com", "friends",
            "family", headers={"Reply-To": "me2@example.com"})
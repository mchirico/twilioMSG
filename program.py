
from twilio.rest import Client
import os


# Get environment variables
account_sid = os.getenv('TWILIO_API_KEY')
auth_token = os.environ.get('TWILIO_API_SECRET')

client = Client(account_sid, auth_token)

def main():
    count = 0
    for sms in client.messages.list():
        print(f"{sms.date_sent}: {sms.from_}")
        print(f"  {sms.body}\n\n")
        count += 1

        if count > 30:
            return
        


if __name__ == "__main__":
    # execute only if run as a script
    main()




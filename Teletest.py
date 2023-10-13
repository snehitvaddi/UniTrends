import pandas as pd
import re
from telethon.sync import TelegramClient
import datetime
import time

# Your API credentials
api_id= 'API'
api_hash= 'HASH'
chats = ['f1interviewreviews']


client = TelegramClient('TeleDaEng', api_id, api_hash)

# Defining the fields and initializing the dataframe
fields = [
    "College", "Interview Outcome", "Visa Attempt Number", "Interview Date",
    "Interview Time", "Interview City", "Interview Country", "Exam Type",
    "Exam Score", "English Test Type", "English Test Score", "Grad Level",
    "Grad Major", "Grad GPA", "Grad Institute", "Grad Country", "Job Type", "Job Years"
]
df = pd.DataFrame(columns=["group", "sender", "date"] + fields)

for chat in chats:
    with TelegramClient('test', api_id, api_hash) as client:
        messages_fetched = 0
        last_date_fetched = None
        while messages_fetched < 100:
            current_messages = []
            for message in client.iter_messages(chat, offset_date=last_date_fetched, limit=100, reverse=False):
                current_messages.append(message)
            
            for message in current_messages:
                if(message.text):
                    # Truncate the message after "Job Years"
                    truncate_point = message.text.find("**Job Years**")
                    truncated_message = message.text[:truncate_point + len("**Job Years**")] + message.text[truncate_point:].split('\n', 1)[0]
                    
                    # Extracting information using regex from the truncated message
                    data = {"group": chat, "sender": message.sender_id, "date": message.date}
                    for field in fields:
                        pattern = rf"\*\*{field}\*\*:\s(.*?)\s*(?=\*\*|\Z)"
                        match = re.search(pattern, truncated_message, re.DOTALL)
                        if match:
                            data[field] = match.group(1).strip()
                            is_valid = True
                        else:
                            data[field] = None

                    # Append the extracted data to the dataframe only if valid data was extracted
                    if is_valid:
                        df = df.append(data, ignore_index=True)
                        messages_fetched += 1
                    
                    # Stop if we've fetched 100 messages
                    if messages_fetched >= 100:
                        break
                    print(messages_fetched)

            # If less than 100 messages were returned, we've fetched all available messages
            if len(current_messages) < 100:
                break

            # Set the last_date_fetched to the date of the last message in the current batch
            last_date_fetched = current_messages[-1].date

# Save the dataframe to CSV
csv_file_path = "extracted_data.csv"
df.to_csv(csv_file_path, index=False)

print(f"Data saved to {csv_file_path}")

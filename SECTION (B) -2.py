import datetime

def create_topic():
    topic_id = "0.0.34567"  
    print(f"Topic Created: {topic_id}")
    return topic_id

def send_messages(topic_id):

    messages = [
        "Hello, Hedera!",
        "Learning HCS",
        "Message 3"
    ]
    
    sent_messages = []
    for msg in messages:
        timestamp = datetime.datetime(2024, 12, 27, 10, 0 + len(sent_messages), 0) 
        sent_messages.append((msg, timestamp))
    
    print("\nMessages Sent:")
    for i, (msg, timestamp) in enumerate(sent_messages, 1):
        print(f"{i}. \"{msg}\" at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    
    return sent_messages

def retrieve_messages(sent_messages):
    print("\nMessages Received:")
    for i, (msg, timestamp) in enumerate(sent_messages, 1):
        print(f"{i}. \"{msg}\" at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

def main():

    topic_id = create_topic()

    sent_messages = send_messages(topic_id)
 
    retrieve_messages(sent_messages)

if __name__ == "__main__":
    main()

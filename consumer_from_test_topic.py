import pandas as pd
from kafka import KafkaConsumer

def main():
    parsed_topic_name = 'test'
    
    consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    
    for msg in consumer:
        tuit_p = TextBlob(tuit)
        polarity = tuit_p.polarity # Extract the polarity
        sentiment = 'positive' if polarity >= 0 else 'negative'
        print(f'The tuit: "{tuit}" is {sentiment}. The polatiry is: {polarity}')

if __name__ == '__main__':
    main()

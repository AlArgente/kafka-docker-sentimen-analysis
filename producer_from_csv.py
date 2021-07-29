import pandas as pd
from kafka import KafkaProducer

def get_data(path_name):
    """Function that take thata from Twitter Api. 
    Temporally: read data from CSV.

    Args:
        path_name (str): path to a Pandas DataFrame with a col name (text) that contain tuits.
    Returns:
        List of tuits.
    """
    
    data = pd.read_csv(path_name)
    return data['text'].to_list()

def publish_message(producer_instance, topic_name, key, value):
    """Publish a message in a kafka topic

    Args:
        producer_instance (KafkaProducer): Kafka producer instance
        topic_name (str): Topic to write the items produced
        key (str): Kay value for the message to publish
        value ([type]): Message we want to publish.
    """
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published succesfully.')
    except Exception as ex:
        print('Exception while publishing message.')
        print(str(ex))

def connect_kafka_producer():
    """Function that create the Kafka Producer.

    Returns:
        KafkaProducer: Kafka producer object.
    """
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka.')
        print(str(ex))
    finally:
        return _producer

def main():
    tweets = get_data('kaggle_sa.csv')
    if len(tweets) > 0:
        topic_name = 'test' # In this example I'm writing at test topic
        kafka_producer = connect_kafka_producer()
        # As an example I only write the first 10 tuits.
        for tweet in tweets[:10]:
            publish_message(kafka_producer, topic_name, 'tuit', tweet.strip())
        if kafka_producer is not None:
            kafka_producer.close()

if __name__ == '__main__':
    main()

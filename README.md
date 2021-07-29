# kafka-docker-sentimen-analysis

Basic Kafka installation using Docker. As an example, I use KafkaProducer to read a CSV with some tuits from [Kaggle](https://www.kaggle.com/kazanova/sentiment140) and write them into a topic named test. Then the Kafka Consumer will read the tuits from the topic and will calculate the sentiment value using the [TextBlob](https://textblob.readthedocs.io/en/dev/). 

The python version used in this project is 3.8.10. 

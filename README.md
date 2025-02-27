# Kafka_project
A sample confluent kafka project to highlight a working understanding of stream processing

# In this Project I attempt too replicate a kafka producer consumer stream by dockerizing zookeeper and kafka services
In order to run this project please utiltize docker-compose up --build -d
This will run the project and spin up four containers
To check the producer and consumer please check their logs either in docker desktop or on the command line. 

As the stream producer generates messages to the topic our consumer will slowly consume and write out to the logs.

# Debuggin
Debug commands are hosted in kafka_commands.txt

# Mimiccing-Kafka
Yet Another Kafka
 
It involves setting up a mini-Kafka on a student's system, complete with a Producer, Subscriber and a Publish-Subscribe architecture.
  At the end of this project, you will be able to setup a mini-Kafka on your system; complete with a mini-zookeeper, multiple Kafka Brokers, Producers and Consumers.
Technologies/Languages Used                                                                                                                                         
Python                                                                                                                                                              
JSON
 ![image](https://github.com/phalgunagopal/Mimiccing-Kafka/assets/59923496/8ca0d3a1-f063-4a1e-8ccc-8aee4e0fb95a)

mini-Zookeeper:


  The main purpose of the mini-Zookeeper is to monitor the health of the Kafka Brokers and keep a track of the Leader.
  
  The method of health monitoring is up to you, but it must be able to detect a failure of a Kafka Broker.
  
Some examples are: Heartbeats, Polling, etc.

In case of a failure of a Kafka Broker, the mini-Zookeeper must elect a new Leader. The choice of a Leader Election algorithm is given to you.

An assumption that is being made is that the mini-Zookeeper is always running and will never fail.


Kafka Brokers:


The Kafka Brokers are responsible for creating and managing topics.

They are also responsible for registering/de-registering any Producers and Consumers.

  In case a topic does not exist when a Producer/Consumer has been started, the Broker must create one.
  
  The Broker is also in charge of storing the messages that are being published by the Producers.
  
The Topics must be stored as directories in a file-system.

Required to also dynamically create partitions for each Topic. Partition function will be used .

They are also in charge of keeping track of which messages have reached a particular consumer and which have not.

 3 Kafka Brokers.
 
The Leader is responsible for handling all Publish Operations. Consume Operations can be handled through either the Leader, or any one of the replicas.

    The Leader maintains a log of all operations which must be replicated on the Followers as well.
    
    In case a publish or a consume operation is encountered when the Leader has died, the remaining Kafka Brokers must be able to handle this situation.

    
Kafka Producer:


The Producer is responsible for publishing messages to a Kafka Topic.

The Producer should be able to register to any Kafka Topic or should notify the Broker to create one if necessary.

  The Producer must co-ordinate with the Broker to keep track of all the messages that a Broker has received.
  
  In case the Broker does not receive a message, it must re-transmit the message.
  
  This can be done by obtaining an acknowledgement from the Broker, on receiving a message.

  
Kafka Consumer:


  The Consumer is responsible for receiving messages from a Kafka Topic..
  
The Consumer should be able to register to any Kafka Topic or should notify the Broker to create one if necessary.

  The Consumer must co-ordinate with the Broker to keep track of all the messages that it has received.
  
  This can be done by sending an acknowledgement to the Broker on receiving a message.


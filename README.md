# 🌐 UniTrends: Analyzing US VISA Trends with Data Engineering! 🎓
This project revolves around analyzing chats from the "US F1 VISA experiences" group on Telegram to derive insights on universities' demand and acceptance rates. The primary motivation is to aid content creation for a YouTube channel focused on the same topic. The project not only achieved its primary goal of generating actionable insights but also served as a hands-on exploration of data engineering.
<p align="center">
<img src="./Project%20Flow.png" alt="Project Flow" width="500" align="center"/>
</p>

### Installation & Setup
#### Prerequisites
- Python
- Kafka
- AWS Account (for S3, Glue, and Athena)

#### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/snehitvaddi/UniTrends
   ```
2. Navigate to the project directory:
   ```bash
   cd UniTrends
   ```
3. Follow individual setup guides for:
   - Setting up Kafka
   - Configuring AWS services (S3, Glue, Athena)
   - Setting up the Telegram API for data extraction
  
### Setting up Kafka on EC2
```markdown   
   First, download and extract Kafka:
   
   wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz
   tar -xvf kafka_2.12-3.3.1.tgz
   
   Install Java and navigate to the Kafka directory:
   
   java -version
   sudo yum install java-1.8.0-openjdk
   java -version
   cd kafka_2.12-3.3.1
   
   Starting Zoo-keeper:

   bin/zookeeper-server-start.sh config/zookeeper.properties
   
   Open another terminal window, SSH into your EC2 machine as done above, and start the Kafka server:

  Starting Kafka-server:

   # Duplicate the session & enter in a new console
   export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
   cd kafka_2.12-3.3.1
   bin/kafka-server-start.sh config/server.properties
```
   > **Note**: Update `server.properties` to run on public IP by editing `ADVERTISED_LISTENERS` to the public IP of the EC2 instance.
```   
   #### Creating the Kafka topic:
   
   # Duplicate the session & enter in a new console
   cd kafka_2.12-3.3.1
   bin/kafka-topics.sh --create --topic demo_testing2 --bootstrap-server {Put the Public IP of your EC2 Instance:9092} --replication-factor 1 --partitions 1
   
   #### Starting the Kafka Producer:

   bin/kafka-console-producer.sh --topic demo_testing2 --bootstrap-server {Put the Public IP of your EC2 Instance:9092}
   
   #### Starting the Kafka Consumer:

   # Duplicate the session & enter in a new console
   cd kafka_2.12-3.3.1
   bin/kafka-console-consumer.sh --topic demo_testing2 --bootstrap-server {Put the Public IP of your EC2 Instance:9092}
   ```
   
   ### Usage
   1. **Data Extraction**: 
   Extract data from Telegram using the script:
      ```bash
      python Teletest.py
      ```
      This script extracts the chat data, cleans, and transforms it to be saved into a CSV file.
   
   2. **Kafka Streaming**:
      - Start the Kafka producer using:
        ```bash
        jupyter notebook producer.ipynb
        ```
      - Start the Kafka consumer using:
        ```bash
        jupyter notebook consumer.ipynb
        ```
        The consumer uploads the data into an S3 bucket.

   3. Follow the AWS Glue and Athena documentation to analyze the data, as detailed in Darshil's tutorial.
```

### Technologies Used
- **Telegram API**: For extracting chat data from the "US F1 VISA experiences" group.
- **Python**: For data extraction, cleaning, and transformation.
- **Kafka**: A distributed streaming platform used for streaming processed data.
- **Amazon S3**: Used for data storage.
- **AWS Glue**: For data cataloging.
- **Amazon Athena**: SQL-based data analysis tool.

### Contribution & Feedback
We value your feedback and contributions. If you'd like to contribute to this project, please make a pull request. For feedback, issues, or suggestions, please open an issue in the repository.

### Acknowledgments
A special thanks to Darshil for his video tutorial on data engineering, which served as a foundation for this project.

### License
This project is licensed under the [MIT License](LICENSE).

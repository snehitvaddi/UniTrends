# 🌐 UniTrends: Analyzing US F1 VISA Chat Trends with Data Engineering! 🎓
This project revolves around analyzing chats from the "US F1 VISA experiences" group on Telegram to derive insights on universities' demand and acceptance rates. The primary motivation is to aid content creation for a YouTube channel focused on the same topic. The project not only achieved its primary goal of generating actionable insights but also served as a hands-on exploration of data engineering.

### Installation & Setup
#### Prerequisites
- Python
- Kafka
- AWS Account (for S3, Glue, and Athena)

#### Setup
1. Clone the repository:
   ```bash
   git clone [repository-link]
   ```
2. Navigate to the project directory:
   ```bash
   cd [project-directory]
   ```
3. Follow individual setup guides for:
   - Setting up Kafka
   - Configuring AWS services (S3, Glue, Athena)
   - Setting up the Telegram API for data extraction

### Usage
1. **Data Extraction**: Extract data from Telegram using the script:
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

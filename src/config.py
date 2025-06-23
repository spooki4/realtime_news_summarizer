import os
from dotenv import load_dotenv

# .env 파일에서 환경변수를 로드합니다.
load_dotenv()

# Gemini API 설정
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Kafka 설정
KAFKA_BROKER_URL = os.getenv('KAFKA_BROKER_URL', 'localhost:9092')
KAFKA_TOPIC_NAME = os.getenv('KAFKA_TOPIC_NAME', 'news-topic')
KAFKA_GROUP_ID = os.getenv('KAFKA_GROUP_ID', 'news-summary-group')

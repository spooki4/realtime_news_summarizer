import json
from kafka import KafkaConsumer
from src.config import KAFKA_BROKER_URL, KAFKA_TOPIC_NAME, KAFKA_GROUP_ID
from src.gemini_service import summarize_text


def create_consumer():
    """Kafka Consumer 인스턴스를 생성하고 반환합니다."""
    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC_NAME,
            bootstrap_servers=KAFKA_BROKER_URL,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id=KAFKA_GROUP_ID,
            consumer_timeout_ms=1000,  # 1초간 메시지 없으면 루프 종료 (테스트용)
        )
        print("✅ Kafka Consumer가 성공적으로 연결되었습니다.")
        return consumer
    except Exception as e:
        print(f"❌ Kafka Consumer 연결 실패: {e}")
        return None


if __name__ == '__main__':
    consumer = create_consumer()
    if consumer:
        print("\n🚀 Gemini 뉴스 요약 시스템이 메시지를 기다립니다...\n")
        for message in consumer:
            news = message.value
            print(f"📬 새로운 뉴스 수신 (Offset: {message.offset})")
            print(f"📌 제목: {news['title']}")
            print(f"📰 원문: {news['content'][:100]}...\n")  # 원문은 일부만 출력

            # Gemini 서비스를 호출하여 요약 실행
            summary = summarize_text(news['content'])

            print(f"🧠 Gemini 요약 결과:\n{summary}")
            print("-" * 80)

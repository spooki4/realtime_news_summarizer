import json
import time
from kafka import KafkaProducer
from src.config import KAFKA_BROKER_URL, KAFKA_TOPIC_NAME

# 샘플 뉴스 데이터
sample_news = [
    {
        "title": "한국, AI 반도체 시장 주도권 경쟁 본격화",
        "content": "정부가 차세대 AI 반도체 기술 개발에 1조 원 규모의 투자를 발표했다. 삼성전자와 SK하이닉스는 고대역폭 메모리(HBM) 생산을 확대하며 글로벌 시장 선점에 나섰다. 전문가들은 이번 투자가 국내 팹리스 생태계 강화에도 긍정적인 영향을 미칠 것으로 전망하고 있다."
    },
    {
        "title": "기후 변화로 인한 폭염, 전 세계적으로 역대 최고 기온 기록",
        "content": "세계기상기구(WMO)는 올여름 북반구 곳곳에서 관측 이래 가장 높은 기온이 기록됐다고 밝혔다. 이러한 이상 기후는 가뭄, 산불 등 심각한 자연재해로 이어지고 있으며, 각국 정부에 탄소 배출 감축을 위한 더 강력한 정책을 요구하는 목소리가 높아지고 있다."
    },
    {
        "title": "K-콘텐츠, 글로벌 OTT 플랫폼 통해 인기 확산",
        "content": "최근 공개된 한국 드라마 '서울의 밤'이 넷플릭스 글로벌 순위 1위를 차지하며 또 한 번 K-콘텐츠의 저력을 입증했다. 창의적인 스토리와 높은 완성도가 전 세계 시청자들을 사로잡은 비결로 꼽히며, 관련 산업의 수출 증대 효과도 기대되고 있다."
    }
]


def create_producer():
    """Kafka Producer 인스턴스를 생성하고 반환합니다."""
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER_URL,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("✅ Kafka Producer가 성공적으로 연결되었습니다.")
        return producer
    except Exception as e:
        print(f"❌ Kafka Producer 연결 실패: {e}")
        return None


if __name__ == '__main__':
    producer = create_producer()
    if producer:
        while True:
            for news_item in sample_news:
                print(f"📤 Kafka로 뉴스 전송 중... (제목: {news_item['title']})")
                producer.send(KAFKA_TOPIC_NAME, value=news_item)
                time.sleep(5)  # 5초마다 하나의 뉴스를 전송
            print("모든 샘플 뉴스를 전송했습니다. 15초 후 다시 시작합니다.")
            time.sleep(15)
        producer.flush()  # 남아있는 메시지 모두 전송

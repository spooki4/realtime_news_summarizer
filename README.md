# Real-Time News Summarizer with Kafka & Gemini AI

실시간으로 유입되는 뉴스 데이터를 Apache Kafka로 스트리밍하고, Google의 Gemini AI를 이용해 자동으로 요약하는 프로젝트입니다. 이 프로젝트는 최신 AI 기술과 데이터 스트리밍 파이프라인을 결합하여 실시간 정보 처리 시스템을 구축하는 방법을 보여줍니다.

---

## 🚀 주요 기능 (Features)

- **실시간 데이터 처리 (Real-Time Data Processing)**: Kafka를 통해 뉴스 데이터를 지연 없이 실시간으로 수신하고 처리합니다.
- **AI 기반 자동 요약 (AI-Powered Summarization)**: Google의 강력한 LLM인 Gemini AI를 활용하여 긴 뉴스 기사를 3줄의 핵심 요약으로 압축합니다.
- **확장 가능한 아키텍처 (Scalable Architecture)**: Producer-Consumer 패턴과 Docker 기반 환경을 통해 시스템 확장이 용이합니다.
- **쉬운 환경 구성 (Easy Setup)**: `Docker Compose`를 사용하여 단 한 번의 명령으로 Kafka 클러스터를 실행할 수 있습니다.

---

## 🛠️ 기술 스택 (Tech Stack)

| Category      | Technology                                                                                                                              |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **AI Model**  | <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=flat&logo=google&logoColor=white" alt="Gemini">                      |
| **Streaming** | <img src="https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat&logo=apachekafka&logoColor=white" alt="Kafka">                  |
| **Language**  | <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">                               |
| **Container** | <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" alt="Docker">                                 |
| **Libraries** | `kafka-python`, `google-generativeai`, `python-dotenv`                                                                                  |

---

## 📂 프로젝트 구조 (Project Structure)

```
realtime_news_summarizer/
├── docker-compose.yml       # Kafka & Zookeeper 실행을 위한 Docker 설정
├── .env.example             # .env 파일 예시
├── requirements.txt         # Python 의존성 패키지 목록
├── README.md                # 프로젝트 설명서
└── src/
    ├── config.py            # 환경변수 및 설정 값 로드
    ├── gemini_service.py    # Gemini API 호출 로직 담당
    ├── producer.py          # Kafka로 뉴스 데이터를 보내는 역할
    └── consumer.py          # Kafka에서 데이터를 받아 요약을 요청하는 역할
```

---

## 🏁 시작하기 (Getting Started)

프로젝트를 로컬 환경에서 실행하는 방법입니다.

### 1. 사전 준비 (Prerequisites)

- [Docker](https://www.docker.com/get-started) 및 [Docker Compose](https://docs.docker.com/compose/install/) 설치
- [Python 3.8+](https://www.python.org/downloads/) 설치
- [Google AI Studio](https://aistudio.google.com/app/apikey)에서 Gemini API 키 발급

### 2. 설치 및 설정 (Installation & Setup)

1.  **리포지터리 복제 (Clone the repository):**
    ```bash
    git clone https://github.com/your-username/realtime-news-summarizer.git
    cd realtime-news-summarizer
    ```

2.  **Python 의존성 설치 (Install Python dependencies):**
    ```bash
    pip install -r requirements.txt
    ```

3.  **환경 변수 설정 (Set up environment variables):**
    `.env.example` 파일을 복사하여 `.env` 파일을 생성하고, 발급받은 Gemini API 키를 입력하세요.
    ```bash
    cp .env.example .env
    ```
    ```.env
    # .env 파일 내용
    GEMINI_API_KEY="여기에_당신의_API_키를_입력하세요"
    ```

### 3. 실행 (Execution)

1.  **(터미널 1) Kafka 클러스터 시작 (Start Kafka cluster):**
    Docker를 이용해 Kafka와 Zookeeper를 백그라운드에서 실행합니다.
    ```bash
    docker-compose up -d
    ```

2.  **(터미널 2) Consumer 실행 (Run the consumer):**
    Consumer를 먼저 실행하여 Kafka 토픽에서 메시지를 기다리게 합니다.
    ```bash
    python -m src.consumer
    ```

3.  **(터미널 3) Producer 실행 (Run the producer):**
    Producer를 실행하여 샘플 뉴스 데이터를 Kafka로 전송합니다.
    ```bash
    python -m src.producer
    ```

4.  **결과 확인 (Check the results):**
    Consumer를 실행한 터미널(터미널 2)에서 실시간으로 수신된 뉴스와 Gemini가 요약한 결과를 확인할 수 있습니다.


### 4. 종료 (Shutdown)

프로젝트 실행을 모두 마친 후, 아래 명령어로 Kafka 클러스터를 정리합니다.
```bash
docker-compose down
```

---

## 💡 향후 개선 방향 (Future Improvements)

-   [ ] **데이터베이스 연동**: 요약된 결과를 PostgreSQL이나 MongoDB 같은 데이터베이스에 저장
-   [ ] **웹 대시보드**: FastAPI와 React/Vue를 사용하여 요약 결과를 실시간으로 보여주는 웹 대시보드 구축
-   [ ] **에러 핸들링 고도화**: 메시지 처리 실패 시 Dead Letter Queue(DLQ) 패턴 적용
-   [ ] **Kubernetes 배포**: 대규모 트래픽 처리를 위해 Kubernetes 환경에 배포

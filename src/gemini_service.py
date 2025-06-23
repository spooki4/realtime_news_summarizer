import google.generativeai as genai
from src.config import GEMINI_API_KEY

# API 키로 Gemini 설정
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')  # 최신이고 빠른 모델 사용
    print("✅ Gemini 모델이 성공적으로 초기화되었습니다.")
except Exception as e:
    print(f"❌ Gemini 모델 초기화 실패: {e}")
    model = None


def summarize_text(article_text: str) -> str:
    """Gemini API를 호출하여 주어진 텍스트를 요약합니다."""
    if not model:
        return "[요약 실패] Gemini 모델이 초기화되지 않았습니다."

    # Gemini에게 전달할 프롬프트
    prompt = f"""
    다음 뉴스 기사를 전문적이고 간결하게, 핵심 내용만 담아 3줄로 요약해줘.
    
    --- 기사 원문 ---
    {article_text}
    --- 요약 ---
    """

    try:
        response = model.generate_content(prompt)
        # 응답 텍스트의 앞뒤 공백 제거 후 반환
        return response.text.strip()
    except Exception as e:
        # API 호출 중 발생할 수 있는 다양한 예외 처리
        print(f"❌ Gemini API 호출 중 오류 발생: {e}")
        return f"[요약 실패] API 호출 중 오류가 발생했습니다: {e}"

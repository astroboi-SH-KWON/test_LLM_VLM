"""
codegemma:7b                  ------------    5.0 GB    21 hours ago
gemma3:27b                    ------------    17 GB     21 hours ago
gemma3:12b                    ------------    8.1 GB    21 hours ago
llama3.1:8b-instruct-q8_0     ------------    8.5 GB    23 hours ago
llama3.1:70b-instruct-q2_K    ------------    26 GB     23 hours ago
deepseek-coder-v2:latest      ------------    8.9 GB    24 hours ago
mixtral:latest                ------------    26 GB     28 hours ago
mistral-small:latest          ------------    14 GB     2 days ago
mistral-nemo:latest           ------------    7.1 GB    2 days ago
mistral:latest                ------------    4.4 GB    2 days ago
codellama:latest              ------------    3.8 GB    2 days ago
llama3:latest                 ------------    4.7 GB    2 days ago
"""

MODEL_ID = "gemma3:27b"

if MODEL_ID == "gemma3:27b":
    CUSTOM_PREFIX = """
    
    """

    HANDLE_PARSING_ERRORS = (

    )

    FULL_QUERY = """
    
    """
else:
    CUSTOM_PREFIX = """
You are a specialized Python data analysis expert.
Your ONLY goal is to solve the user's request using the dataframe `df`.

You must use the following format:

[REPORT FORMAT 예시]
Final Answer:
==================================================
            분석 결과 보고서
==================================================
1. 분석 요약: (전체적인 분석 결과를 한 줄 요약)

2. 주요 통계 수치:
   (평균값, 분산, 상관분석, 분산분석, 회귀분석, 요인분석, 주성분분석)

3. 도표 (Visual Analysis):
   - 분석 결과 그래프를 'chart.png'로 저장하고 화면에 출력하였습니다.

4. 데이터 상세 분석:
   - (데이터의 흐름과 특징을 구체적인 숫자를 인용하여 설명)

5. 비즈니스 제언:
   - (분석 결과를 바탕으로 서비스 운영에 도움이 될 만한 아이디어)
==================================================
        """

    HANDLE_PARSING_ERRORS = (
        "Check your format. Ensure 'Action: python_repl_ast' is present "
        "and 'Action Input' contains ONLY raw Python code without any backticks or markdown tags."
        "You MUST use the format: 'Thought: <reasoning>\nAction: python_repl_ast\nAction Input: <code>'. "
        "Do not explain functions. Just execute the code for the given 'df'."
    )

    FULL_QUERY = """

        """
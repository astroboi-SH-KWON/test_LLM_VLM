# test_LLM_VLM
test_LLM_VLM

## 1. Setting up the Environment for Mac m2
    conda create -n data_analysis python=3.10
    conda activate data_analysis

    pip install bitsandbytes==0.42.0 vllm==0.7.3 transformers==4.48.2

    pip install matplotlib
    pip install lxml
    pip install prophet
    pip install sklearn
    pip install statsmodels
    pip install seaborn
    pip install ydata_profiling
    pip install tensorflow

    brew install libomp
    export KMP_DUPLICATE_LIB_OK=TRUE
    pip install 'accelerate>=0.26.0'

    pip install tf-keras
    pip install peft

    # # transformers 와 peft 버전 불일치
    pip install --upgrade transformers peft accelerate
    
    # # 상용 LLM api 이용, 학습 데이터 만들기 
    ~~pip install google-generativeai~~  # # Deprecated
    pip install google-genai

    # # RAG 활용
    pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers
    pip install pypdf

    # # for 010_langchain_df_agent.ipynb
    pip install langchain-experimental pandas tabulate
    pip install seaborn statsmodels

## 2. Setting up the Environment for Ubuntu 24.04.2 LTS 2080ti(Driver Version: 550.120 CUDA Version: 12.4 )
    conda create -n test_vLLM python=3.10
    conda activate test_vLLM

    pip install bitsandbytes==0.45.3 vllm==0.7.3 transformers==4.48.2
    pip install matplotlib
    pip install lxml
    pip install pandas
    pip install 'accelerate>=0.26.0'
    pip install wordcloud
    
    pip install datasets
    pip install peft

    # # transformers 와 peft 버전 불일치
    pip install -U transformers peft accelerate bitsandbytes

    # # 상용 LLM api 이용, 학습 데이터 만들기 
    pip install google-genai

    # # RAG 활용
    pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers
    pip install pypdf

    # # for 010_langchain_df_agent.ipynb
    pip install langchain-experimental pandas tabulate
    pip install seaborn statsmodels

    # # 
    pip install streamlit pandas langchain-ollama langchain-experimental tabulate

## 3. cmd for ollama
    # # 1. ollama 설치
    curl -fsSL https://ollama.com/install.sh | sh

    # # 2. Task에 맞는 모델 다운로드 e.g code 관련 CodeLlama, DeepSeek-Coder, 사내 메일 요약 Llama-3, 데이터 분석 Mistral
    ollama pull llama3
    ollama pull codellama
    ollama pull mistral

    # # 3. 모델 실행
    ollama run {model_id}

    # # 4. 모델 중지
    # # 4-1. local prompt (대화창) 나오기
    >>>/bye
    # # 4-2. 메모리 해제
    ollama stop {model_id}

    # # 5. 실행 중인 모델 확인
    ollama ps
    
    # # 6. ollama 전체 서비스 중지
    sudo systemctl stop ollama

    # # 7. ollama 서비스 재시작
    sudo systemctl start ollama
    
    # # 8. 설치(pull) 목록  
    ollama list
    
    NAME                    ID              SIZE      MODIFIED       
    mistral-small:latest    ____________    14 GB     9 minutes ago     
    mixtral:latest          ____________    26 GB     22 minutes ago    
    mistral-nemo:latest     ____________    7.1 GB    33 minutes ago    
    mistral:latest          ____________    4.4 GB    20 hours ago      
    codellama:latest        ____________    3.8 GB    21 hours ago      
    llama3:latest           ____________    4.7 GB    21 hours ago

    # # 9. 모델 삭제
    ollama rm {model_id}

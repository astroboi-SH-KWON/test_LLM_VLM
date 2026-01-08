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
    pip install google-generativeai

    # # RAG 활용
    pip install langchain langchain-community langchain-huggingface chromadb sentence-transformers


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

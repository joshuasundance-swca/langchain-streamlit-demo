import os

MODEL_DICT = {
    "gpt-3.5-turbo": "OpenAI",
    "gpt-4": "OpenAI",
    "claude-instant-v1": "Anthropic",
    "claude-2": "Anthropic",
    "meta-llama/Llama-2-7b-chat-hf": "Anyscale Endpoints",
    "meta-llama/Llama-2-13b-chat-hf": "Anyscale Endpoints",
    "meta-llama/Llama-2-70b-chat-hf": "Anyscale Endpoints",
    "codellama/CodeLlama-34b-Instruct-hf": "Anyscale Endpoints",
    "Azure OpenAI": "Azure OpenAI",
}

SUPPORTED_MODELS = list(MODEL_DICT.keys())

DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "gpt-3.5-turbo")

DEFAULT_SYSTEM_PROMPT = os.environ.get(
    "DEFAULT_SYSTEM_PROMPT",
    "You are a helpful chatbot.",
)

MIN_TEMP = float(os.environ.get("MIN_TEMPERATURE", 0.0))
MAX_TEMP = float(os.environ.get("MAX_TEMPERATURE", 1.0))
DEFAULT_TEMP = float(os.environ.get("DEFAULT_TEMPERATURE", 0.7))

MIN_MAX_TOKENS = int(os.environ.get("MIN_MAX_TOKENS", 1))
MAX_MAX_TOKENS = int(os.environ.get("MAX_MAX_TOKENS", 100000))
DEFAULT_MAX_TOKENS = int(os.environ.get("DEFAULT_MAX_TOKENS", 1000))

DEFAULT_LANGSMITH_PROJECT = os.environ.get("LANGCHAIN_PROJECT")

AZURE_VARS = [
    "AZURE_OPENAI_BASE_URL",
    "AZURE_OPENAI_API_VERSION",
    "AZURE_OPENAI_DEPLOYMENT_NAME",
    "AZURE_OPENAI_API_KEY",
    "AZURE_OPENAI_MODEL_VERSION",
]

AZURE_DICT = {v: os.environ.get(v, "") for v in AZURE_VARS}

PROVIDER_KEY_DICT = {
    "OpenAI": os.environ.get("OPENAI_API_KEY", ""),
    "Anthropic": os.environ.get("ANTHROPIC_API_KEY", ""),
    "Anyscale Endpoints": os.environ.get("ANYSCALE_API_KEY", ""),
    "LANGSMITH": os.environ.get("LANGCHAIN_API_KEY", ""),
}

OPENAI_API_KEY = PROVIDER_KEY_DICT["OpenAI"]


MIN_CHUNK_SIZE = 1
MAX_CHUNK_SIZE = 10000
DEFAULT_CHUNK_SIZE = 1000

MIN_CHUNK_OVERLAP = 0
MAX_CHUNK_OVERLAP = 10000
DEFAULT_CHUNK_OVERLAP = 0

DEFAULT_RETRIEVER_K = 4

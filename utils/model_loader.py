import os
from dotenv import load_dotenv
from typing import Any, Literal, Optional
from pydantic import Field, BaseModel
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI


class ConfigLoader:

    def __init__(self):
        print(f"Loading configuration from config.yaml")
        self.config = self.load_config()

    def __gititem__(self, key):
        return self.config.get[key]


class ModelLoader:
    model_provider: Literal["openai", "groq"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context : Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load and return the LLM model based on the configuration.

        """
        print("Loading LLM model...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading Groq model..................")
            # Add Groq model loading logic here
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.configp["llm"]["groq"]["model_name"]
            llm = ChatGroq(model=model_name, api=groq_api_key)
        elif self.model_provider == "openai":
            print("Loading OpenAI model..................")
            # Add OpenAI model loading logic here
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.configp["llm"]["openai"]["model_name"]
            llm = ChatOpenAI(model_name=model_name, openai_api_key=openai_api_key, temperature=0)

        return llm
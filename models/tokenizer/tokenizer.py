import logging
from typing import List, Dict
from transformers import AutoTokenizer
from config.settings import settings

logger = logging.getLogger(__name__)

class TextTokenizer:
    def __init__(self):
        self.tokenizer = None
        self.max_length = 512

    def initialize(self, model_name: str = "distilbert-base-uncased"):
        """Initialize the tokenizer"""
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        logger.info(f"Initialized tokenizer with model: {model_name}")

    def tokenize(self, text: str) -> Dict[str, List[int]]:
        """Tokenize input text"""
        if self.tokenizer is None:
            self.initialize()
        
        return self.tokenizer(
            text,
            padding='max_length',
            max_length=self.max_length,
            truncation=True,
            return_tensors="pt"
        )

    def decode(self, token_ids: List[int]) -> str:
        """Decode token IDs back to text"""
        if self.tokenizer is None:
            self.initialize()
            
        return self.tokenizer.decode(token_ids, skip_special_tokens=True)
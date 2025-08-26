"""Model interfaces and wrappers"""
from .llm import LLMWrapper
from .judge import JudgeInterface

__all__ = ['LLMWrapper', 'JudgeInterface']

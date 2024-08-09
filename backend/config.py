# Useful for debugging purposes when you don't want to waste GPT4-Vision credits
# Setting to True will stream a mock response instead of calling the OpenAI API
# TODO: Should only be set to true when value is 'True', not any abitrary truthy value
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", None)

AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_RESOURCE_NAME = os.environ.get("AZURE_OPENAI_RESOURCE_NAME")
AZURE_OPENAI_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.environ.get("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_DALLE3_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DALLE3_DEPLOYMENT_NAME")
AZURE_OPENAI_DALLE3_API_VERSION = os.environ.get("AZURE_OPENAI_DALLE3_API_VERSION")

# Debugging-related

SHOULD_MOCK_AI_RESPONSE = bool(os.environ.get("MOCK", False))
IS_DEBUG_ENABLED = bool(os.environ.get("IS_DEBUG_ENABLED", False))
DEBUG_DIR = os.environ.get("DEBUG_DIR", "")

# Set to True when running in production (on the hosted version)
# Used as a feature flag to enable or disable certain features
IS_PROD = os.environ.get("IS_PROD", False)

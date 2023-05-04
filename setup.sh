#!/bin/bash
echo "Get a OpenAI key @ https://platform.openai.com/account/api-keys"
echo "Enter your OpenAI key: "
read openai_key
pip3 install openai
sed -i "7s/.*/openai.api_key = '$openai_key'/" main.py

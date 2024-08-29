"""
CREDIT: copied directly from Neuronpedia Docs.
link: https://docs.neuronpedia.org/steering
"""

import json
import requests

# prompt and model
PROMPT = "The most dangerous city on earth is"
MODEL_ID = "gemma-2b"

# feature about San Francisco
FEATURE = {"modelId": "gemma-2b", "layer": "6-res-jb", "index": 10200, "strength": 5}

# other settings
TEMPERATURE = 0.2
N_TOKENS = 20
FREQ_PENALTY = 1.0
SEED = 16
STRENGTH_MULTIPLIER = 4

# make the request
url = "https://www.neuronpedia.org/api/steer"
data = {
    "prompt": PROMPT,
    "modelId": MODEL_ID,
    "features": [FEATURE],
    "temperature": TEMPERATURE,
    "n_tokens": N_TOKENS,
    "freq_penalty": FREQ_PENALTY,
    "seed": SEED,
    "strength_multiplier": STRENGTH_MULTIPLIER,
}
headers = {"Content-Type": "application/json"}

# send request
response = requests.post(url, json=data, headers=headers)
json_response = response.json()
formatted_response = json.dumps(json_response, indent=4)
print(formatted_response)
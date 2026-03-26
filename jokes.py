import random

JOKES = [
  "Why don't scientists trust atoms? Because they make up everything!",
  "Why did the scarecrow win an award? He was outstanding in his field!",
  "I told my wife she was drawing her eyebrows too high. She looked surprised.",
  "Why don't eggs tell jokes? They'd crack each other up!",
  "What do you call a fake noodle? An impasta!",
  "How do you organize a space party? You planet!",
  "Why did the Kubernetes developer go broke? Because he used up all his resources!",
]

def get_random_joke():
  return random.choice(JOKES)
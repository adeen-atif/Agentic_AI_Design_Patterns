import concurrent.futures

def analyze_sentiment():
    return "Sentiment: Positive"

def extract_keywords():
    return "Keywords: AI, LLM, Healthcare"

def summarize_text():
    return "Summary complete."

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(lambda f: f(), [analyze_sentiment, extract_keywords, summarize_text]))

print(results)

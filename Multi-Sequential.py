def researcher_agent(topic):
    return f"Research on {topic} done."

def writer_agent(research):
    return f"Drafted: {research}"

def editor_agent(draft):
    return f"Finalized: {draft}"

research = researcher_agent("AI in Pharma")
draft = writer_agent(research)
final = editor_agent(draft)

print(final)

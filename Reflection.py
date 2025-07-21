from openai import OpenAI

client = OpenAI()

def generate_output(prompt):
    return client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content

def reflect_on_output(output):
    reflection_prompt = f"Review this output and suggest improvements:\n\n{output}"
    return generate_output(reflection_prompt)

response = generate_output("Explain quantum computing to a 12-year-old.")
refined = reflect_on_output(response)

print("Original Response:\n", response)
print("\nRefined Version:\n", refined)

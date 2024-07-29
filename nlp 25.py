import openai

openai.api_key = 'YOUR_API_KEY'

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Once upon a time, in a land far away,",
  max_tokens=50
)

print(response.choices[0].text.strip())

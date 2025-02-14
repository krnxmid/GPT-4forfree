from openai import OpenAI
from rich.markdown import Markdown
from rich.console import Console
console = Console()
# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings. 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key="YOUR_API_KEY"
)
prompt = input("Enter your prompt: ")
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-4o",
    temperature=1,
    max_tokens=4096,
    top_p=1
)
console.print(Markdown(response.choices[0].message.content))

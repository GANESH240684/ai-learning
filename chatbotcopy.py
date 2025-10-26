import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# Function to get latest cricket matches from ESPN CricInfo
def get_latest_cricket_updates():
    url = "https://site.api.espn.com/apis/site/v2/sports/cricket/scoreboard"
    try:
        response = requests.get(url)
        data = response.json()

        matches = []
        for event in data.get("events", []):
            name = event.get("name", "Unknown Match")
            status = event.get("status", {}).get("type", {}).get("description", "Unknown Status")
            matches.append(f"{name} — {status}")

        if not matches:
            return "No live or recent cricket matches found."
        return "\n".join(matches)

    except Exception as e:
        return f"Error fetching cricket data: {e}"

# Main interactive loop
while True:
    question_prompt = input("How may I help you today? \n")

    if "cricket" in question_prompt.lower():
        # Get live cricket data
        cricket_updates = get_latest_cricket_updates()

        # Pass updates to GPT for summarization
        completion = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "user",
                    "content": f"Here are the latest cricket updates:\n{cricket_updates}\n\nSummarize this in one or two lines."
                }
            ]
        )

        print("\n" + completion.choices[0].message.content + "\n")

    else:
        # Normal GPT conversation
        completion = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "user", "content": question_prompt}
            ]
        )
        print("\n" + completion.choices[0].message.content + "\n")
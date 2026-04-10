from google import genai
import json
import os
import time

client = genai.Client(api_key=os.getenv("AIzaSyBJLy7dvSVWHpyqQVUh-zvaWlqi-zOZYQo"))

SYSTEM_PROMPT = """
You are a UAV navigation assistant.

Convert user commands into NED (North, East, Down) waypoints.

Rules:
- Output ONLY valid JSON
- No explanation, no markdown
- Format:

{
  "waypoints": [
    {"north": float, "east": float, "alt": float}
  ]
}

Guidelines:
- Use meters
- forward = north
- right = east
- Default altitude = 10
- Return ONLY JSON
"""

def get_waypoints(command):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=SYSTEM_PROMPT + "\nUser: " + command
        )

        text = response.text.strip()
        text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)
          except Exception as e:


        if "north" in command:
            return {"waypoints": [{"north": 5, "east": 0, "alt": 10}]}
        elif "square" in command:
            return {
                "waypoints": [
                    {"north": 10, "east": 0, "alt": 10},
                    {"north": 10, "east": 10, "alt": 10},
                    {"north": 0, "east": 10, "alt": 10},
                    {"north": 0, "east": 0, "alt": 10}
                ]
            }
        else:
            return {"waypoints": [{"north": 0, "east": 0, "alt": 10}]}

if __name__ == "__main__":
    while True:
        cmd = input("Enter command: ")

        if not cmd.strip():
            continue

        result = get_waypoints(cmd)

        print("\nParsed Output:")
        print(json.dumps(result, indent=2))

        time.sleep(3)

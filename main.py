import os

import anthropic
from termcolor import colored


class Agentize:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def get_message(self):
        try:
            user_input = input()
            return user_input, bool(user_input)
        except EOFError as e:
            return "", str(e)

    def run(self):
        conversation = []
        print("Chat with Claude (use 'ctrl/cmd + d' to quit)")

        while True:
            print(colored("You: ", "blue"), end="")

            user_input, ok = self.get_message()
            if not ok:
                break

            user_message = {
                "role": "user",
                "content": [{"type": "text", "text": user_input}],
            }

            conversation.append(user_message)

            message = self.run_inference(conversation)
            conversation.append({"role": "assistant", "content": message.content})

            for content in message.content:
                if content.type == "text":
                    print(colored("Claude:", "yellow"), f"{content.text}")

    def run_inference(self, conversation):
        return self.client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            messages=conversation,
        )


def main():
    agentize = Agentize()
    agentize.run()


if __name__ == "__main__":
    main()

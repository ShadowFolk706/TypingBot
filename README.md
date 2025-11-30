# TypingBot
A program that will type for you

This project is meant to deceive Google Doc extensions that allow ceratin users to see when text has been copied and pasted into the open dokument. This program has features to both type out text that you have copied, or you can ask a prompt and have AI's answer typed out for you as if you wrote it. This AI model is run entirely on-device, so no WiFi is needed, no company gets your data, and with the way it is currently set up, your prompts are not saved to any log.
Prerequisites
- Python
- Ollama
  - You also need an Ollama model downloaded, this is easy to do. This code currently uses the model llama3.2, but that can be changed by replacing the "llama3.2" model with whatever model you downloaded
- PyAutoGui

Both using AI and not using AI work now. There are pauses randomly for both ends of words and sentences to further mimik a human typer. These can be toggled from input to input as well as a text informing the user that the bot is done typing.

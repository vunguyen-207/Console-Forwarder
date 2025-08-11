# Telegram Remote CMD Bot

[📄 Tiếng Việt](README.md)

## Overview
A simple Python script that sets up a Telegram bot capable of executing shell commands remotely via the `/cmd` command. The primary purpose of this tool is to bypass and counteract malicious activities from screen-sharers during client computer inspections. You can use this bot to run commands on your PC securely and discreetly.

By running commands through Telegram, you avoid granting full remote control, reducing the risk of unauthorized changes or data exposure. This is particularly useful in scenarios like tech support, debugging, or automated tasks where screen visibility isn't necessary.

**Note:** Use this tool responsibly and ensure you have permission to access and execute commands on the target machine. This is made for concept-proving and wasn't intended for malicious purposes.

## Features
- Execute any shell command remotely via Telegram.
- Simple setup with minimal dependencies.
- Runs in the background to avoid detection during screen-sharing.
- Limits interaction to command-line output, preventing visual manipulation.

## Requirements
- Python 3.6+
- Telegram Bot Token (create one via [BotFather](https://t.me/botfather))
- Installed libraries: `python-telegram-bot` (install via `pip install python-telegram-bot`)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/vunguyen-207/Console-Forwarder/
   cd Console-Forwarder
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Edit the script (`bot.py`) to replace `BOT_TOKEN` and `CHAT_ID` with your own:
   - `YourToken`: Your Telegram bot token.
   - `YourChatID`: The chat ID where the bot will respond (e.g., your personal chat or a group).

4. Run the script:
   ```
   python bot.py
   ```

To run it in the background (for bypass purposes):
- On Windows: Use `pythonw bot.py` to run without a console window.
- On Linux/Mac: Use `nohup python bot.py &` or convert to a service.

For persistence and hidden execution:
- Compile to executable using PyInstaller: `pyinstaller --onefile --noconsole bot.py`
- Add to startup or task scheduler to ensure it runs silently, or do that using the public methods.

## Usage
1. Start the bot by running the script.
2. In Telegram, send `/cmd <your_command>` to the bot.
   - Ex: `/cmd dir` (on Windows) or `/cmd ls` (on Linux).
3. The bot will execute the command and reply with the output.

During a screen-sharing session, the bot runs invisibly, allowing you to perform actions without the sharer seeing or interfering directly.

## Security Considerations
- **Recode Required:** This is a rapidly developed proof-of-concept product. You will need to recode it to ensure complete anonymity in its operation.
- **Access Control:** Restrict the chat ID to trusted users only.
- **Command Risks:** Executing arbitrary commands can be dangerous; implement additional authentication if needed.
- **Bypass Ethics:** This tool helps avoid unnecessary screen access but ensure compliance with laws and policies.

## License
MIT License - See [LICENSE](LICENSE) for details.

## Contributing
Feel free to fork and submit pull requests for improvements, such as adding authentication or more bypass techniques.

## Disclaimer
This tool is for educational and legitimate use only. I am not responsible for any misuse.

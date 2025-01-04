# Discord Link Moderation Bot

## Description

This **Discord Link Moderation Bot** is designed to help server administrators manage and moderate messages containing links in their Discord channels. It automatically detects and deletes messages containing links (except those in a whitelist) and sends notifications to a specified staff channel for moderation. The bot also allows staff members to approve or deny messages by reacting with checkmarks.

### Features:
- Detects and deletes messages with links (except links from whitelisted users and channels).
- Sends a notification to a staff channel when a message with a link is detected.
- Staff can approve or reject the message by reacting with ✅ or ❌.
- Fully customizable whitelist for users and channels.

## Installation

### Prerequisites
Before running the bot, make sure you have the following installed:
- Python 3.x
- `discord.py` library

You can install the required library by running:

```bash
pip install discord.py
```

### Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/sonixnguyen/link-moderation-discord-bot.git
cd link-moderation-discord-bot
```

2. Replace the placeholder `STAFF_CHANNEL_ID` with your actual staff channel ID in the code.

3. Set up the whitelist of users and channels (optional):
   - Add user IDs to the `WHITELISTED_USER_IDS` list.
   - Add channel IDs to the `WHITELISTED_CHANNEL_IDS` list.

4. Replace the placeholder `YOUR_BOT_TOKEN` in the last line of the script with your actual Discord bot token.

5. Run the bot:

```bash
python bot.py
```

## Configuration

### Moderation Settings

- **STAFF_CHANNEL_ID**: The ID of the channel where moderation requests will be sent.
- **WHITELISTED_USER_IDS**: A list of user IDs that are allowed to send links without moderation.
- **WHITELISTED_CHANNEL_IDS**: A list of channel IDs where links will not be moderated.
- **LINK_REGEX**: A regular expression used to identify URLs in messages.

## How to Use

1. The bot listens to messages in channels. If a message contains a URL, it checks if the URL is from **discord.com** (in which case it will be ignored).
2. If a URL is detected from another source, the bot deletes the message and notifies the staff in the specified staff channel.
3. Staff can approve or deny the message by reacting with a ✅ or ❌ emoji in the staff channel.
4. When a staff member approves a message, the bot will resend the original message in the original channel with an approval embed.

## Contribution

If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, feel free to open an issue on GitHub or reach out via [Telegram](https://t.me/sonixnguyen) or [Discord]().

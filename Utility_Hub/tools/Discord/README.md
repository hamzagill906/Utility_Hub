# Discord Messaging Tool

This tool is part of the **Utility Hub** project and provides functionality for sending messages to Discord channels using Discord's API.

## Features

- Send messages to Discord channels.
- Easy integration with other tools in the Utility Hub.
- Configurable via environment variables.

## Prerequisites

- A Discord bot token.
- The bot must be added to the desired server with appropriate permissions.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/Utility_Hub.git
    cd Utility_Hub/tools/Discord
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Create a `.env` file in the `Discord` directory with the following content:

```env
DISCORD_BOT_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_channel_id
```

Replace `your_discord_bot_token` and `your_channel_id` with your actual bot token and channel ID.

## Usage

Run the script to send a message:
```bash
python send_message.py "Your message here"
```

## Example

```bash
python send_message.py "Hello, Discord!"
```

## Contributing

Contributions are welcome! Please follow the project's [contribution guidelines](../../CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](../../LICENSE).
# LinkedIn Job Scraper with Discord Bot Integration

This project scrapes developer job postings from LinkedIn and sends them to a Discord channel using a bot.

## Features

- Scrapes recent developer jobs from LinkedIn.
- Integrates with Discord via a bot.
- Sends job listings directly to your Discord server.

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Flan-dev1/linkedin-scraper.git
   cd linkedin-scraper
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

   Required packages:

   - `discord.py`
   - `python-dotenv`
   - `requests`
   - `beautifulsoup4`

3. **Configure environment variables:**
   - Create a `.env` file with your Discord bot token:
     ```
     TOKEN='your_discord_bot_token'
     ```

## Usage

1. **Run the Discord bot:**

   ```sh
   python discordbot.py
   ```

2. **Use the bot in Discord:**
   - Type `$test` in your Discord server to receive the latest job listings.

## Files

- [`linkedin.py`](linkedin.py): Scrapes jobs from LinkedIn.
- [`discordbot.py`](discordbot.py): Discord bot integration.

## License

MIT License. See [`LICENSE`](LICENSE) for details.

## Disclaimer

This project is for educational purposes. Scraping LinkedIn may violate their

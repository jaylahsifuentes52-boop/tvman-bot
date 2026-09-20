OWNER-ONLY DISCORD BOT

1. Open bot.py.
2. Find:
   OWNER_ID = 123456789012345678
3. Replace that number with YOUR Discord user ID.
4. Do NOT put your bot token in bot.py.
5. On Render, create an environment variable:
   Key: DISCORD_TOKEN
   Value: your Discord bot token
6. Build command:
   pip install -r requirements.txt
7. Start command:
   python bot.py

The included /panel command can only be used by the Discord account whose ID is in OWNER_ID.

IMPORTANT:
- Keep DISCORD_TOKEN private.
- This example does not include your token.
- To make your other slash commands owner-only, add @owner_only() above each command.

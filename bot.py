from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Sample country data
countries_data = {
    "USA": {
        "capital": "Washington, D.C.",
        "code": "+1",
        "area": "9,833,520 km²",
        "population": "331 million",
        "language": "English"
    },
    "India": {
        "capital": "New Delhi",
        "code": "+91",
        "area": "3,287,263 km²",
        "population": "1.4 billion",
        "language": "Hindi"
    },
    "Japan": {
        "capital": "Tokyo",
        "code": "+81",
        "area": "377,975 km²",
        "population": "126 million",
        "language": "Japanese"
    },
    "Uk":{
        {
        "capital": "London",
        "code": "+10",
        "area": "435,975 km²",
        "population": "145 million",
        "language": "British"
    },
    }
}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to Country Info Bot! Type /country <country_name> to get info.")

# Country info command
async def country_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Get the country name from the user's message
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a country name like this: /country <country_name>")
        return

    country_name = " ".join(context.args).title()

    # Check if the country exists in the data
    if country_name in countries_data:
        data = countries_data[country_name]
        response = f"**{country_name}**\n" \
                   f"Capital: {data['capital']}\n" \
                   f"Country Code: {data['code']}\n" \
                   f"Area: {data['area']}\n" \
                   f"Population: {data['population']}\n" \
                   f"Majority Language: {data['language']}"
    else:
        response = f"Sorry, I don't have data for {country_name}."

    await update.message.reply_text(response)

# Main function to start the bot
def main():
    # Initialize the application with your bot token
    application = ApplicationBuilder().token("7685063979:AAHWfou8oYVkQ0qEDLwZcJe3T6zaSOGFaGs").build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("country", country_info))

    # Start polling updates from Telegram
    application.run_polling()

if __name__ == "__main__":
    main()

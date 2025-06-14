import tweepy
import os
import random

auth = tweepy.OAuth1UserHandler(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET"),
    os.getenv("ACCESS_TOKEN"),
    os.getenv("ACCESS_TOKEN_SECRET")
)
api = tweepy.API(auth)

tweets = [
    "⚔️ Welcome to Chimeria, where every NFT is a warrior. Will yours survive?",
    "🧪 Mutants, relics, and warbands. Only the strong mint in the Savage Lands.",
    "🔥 2000 left to mint. Claim your gladiator or fall forgotten. #NFTs #BASE #SavageLands",
]

tweet = random.choice(tweets)
api.update_status(tweet)
print("✅ Tweet sent!")

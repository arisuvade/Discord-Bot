import discord
import responses


async def send_message(msg: str, user_msg: str, is_private: bool) -> str:
    try:
        response: str = responses.responses_handler(user_msg)
        if is_private:
            await msg.author.send(response)
        else:
            await msg.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot() -> None:
    TOKEN: str = "MTAyNTk3Nzg0NDc1NDU1NDkyMA.GiNOUB\
.TtVTj8HMwqZOU5POc6tw4V3rs0DOLZ1sKVF9so"

    intents: str = discord.Intents.default()
    intents.message_content: bool = True
    client: str = discord.Client(intents=intents)

    @client.event
    async def on_ready() -> str:
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(msg: str) -> str:
        if msg.author == client.user:
            return

        usernameid: str = msg.author
        user_msg: str = msg.content
        channel: str = msg.channel
        print(f"Channel: {channel} | {usernameid}: {user_msg}")

        if user_msg.startswith("?"):
            user_msg = user_msg[1:]
            await send_message(msg, user_msg, is_private=True)
        else:
            await send_message(msg, user_msg, is_private=False)

    client.run(TOKEN)

import os
import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as Issue Assigner {0.user}'
        .format(client))

# @client.event
# async def on_message(message):
#   if message.author == client.user :
#     return

#   if message.author in db.keys():
#     pass
#   else:
#     db[message.author] = "Admin"
  
#   if message.content.startswith('$hello_send_role_message'):
#     await message.channel.send("```Please take Hacker role by react 🥳 to this message. ```")

#   if message.content.startswith('$list_users'):
#     await message.channel.send(db.keys())


# @client.event
# async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
#   role_message_id = 975979325520216144
#   emoji_to_role = {
#     discord.PartialEmoji(name='🔴'): 975813555817414661,  # ID of the role associated with unicode emoji '🔴'.
#     discord.PartialEmoji(name='🟡'): 975813555817414660,  # ID of the role associated with unicode emoji '🟡'.
#     discord.PartialEmoji(name='🙏'): 975813555817414657,  # ID of the role associated with a partial emoji's ID.
#   }
#   if payload.message_id != role_message_id:
#     return
#   guild = self.get_guild(payload.guild_id)
#   if guild is None:
#     print("Guild is none")
#     return
#   try:
#     role_id = emoji_to_role[payload.emoji]
#   except KeyError:
#     print("There is keyerror")
#     return

#   role = guild.get_role(role_id)
#   if role in None:
#     print("Role is None")
#   try:
#     await payload.member.add_roles(role)
#   except discord.HTTPException:
#     print("error is assigning roles")
#     pass

emoji_to_role = {
    discord.PartialEmoji(name='🥳'): 975813555817414657,
  }

@client.event
async def on_raw_reaction_add(payload):
  if payload.message_id == 976036898139152424 and payload.emoji.name == "🥳":
    role_id = emoji_to_role[payload.emoji]
    # role_id1 = guild_id.get_role(role_id)
    guild_id = payload.member.guild.get_role(role_id)
    await payload.member.add_roles(guild_id)

@client.event
async def on_raw_reaction_remove(payload):
  if payload.message_id == 976036898139152424 and payload.emoji.name == "🥳":
    role_id = emoji_to_role[payload.emoji]
    # role = payload.member.get_role(role_id)
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    role = guild.get_role(role_id)
    await member.remove_roles(role)
    

my_secret = os.environ['TOKEN']
client.run(my_secret)

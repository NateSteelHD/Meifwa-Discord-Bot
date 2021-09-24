import discord
import aiohttp
import logging
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

log = logging.getLogger("NSFW cog")

async def api_call(call_uri, returnObj=False):
	async with aiohttp.ClientSession() as session:
		async with session.get(f"{call_uri}") as response:
			response = await response.json()
			if returnObj == False:
				return response["url"]
			elif returnObj == True:
				return response


class nsfw(commands.Cog):
    def __init__(self, bot):
	    self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log.warn(f"{self.__class__.__name__} Cog has been loaded")

    @commands.cooldown(5, 7, commands.BucketType.user)
    @commands.command()
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="Juicy henti for you!",
                color=ctx.message.author.color,
                timestamp=ctx.message.created_at,
            )

            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}#{ctx.message.author.discriminator}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url
            )

            embed.set_image(
                url=await api_call("https://nekos.life/api/v2/img/Random_hentai_gif")
            )
            await ctx.message.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="HoldUp!!",
                description="This command can only be used in a NSFW channel.",
                color=0xFF0000,
                timestamp=ctx.message.created_at,
            )
            await ctx.message.reply(embed=embed, delete_after=20)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @commands.command(name="feet", aliases=["feetgif", "foot"])
    async def feet(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="***Feet***",
                color=ctx.message.author.color,
                timestamp=ctx.message.created_at,
            )

            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}#{ctx.message.author.discriminator}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url
            )

            embed.set_image(url=await api_call("https://nekos.life/api/v2/img/feetg"))
            await ctx.message.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="HoldUp!!",
                description="This command can only be used in a NSFW channel.",
                color=0xFF0000,
                timestamp=ctx.message.created_at,
            )
            await ctx.message.reply(embed=embed, delete_after=20)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @commands.command()
    async def cum(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="***Sticky white stuff!***",
                color=ctx.message.author.color,
                timestamp=ctx.message.created_at,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}#{ctx.message.author.discriminator}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url
            )
            embed.set_image(url=await api_call("https://nekos.life/api/v2/img/cum"))
            await ctx.message.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="HoldUp!!",
                description="This command can only be used in a NSFW channel.",
                color=0xFF0000,
                timestamp=ctx.message.created_at,
            )
            await ctx.message.reply(embed=embed, delete_after=20)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @commands.command(name="nekofuck", aliases=["nekosex", "nekogif"])
    async def nekofuck(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="Catgirls!!!!",
                color=ctx.message.author.color,
                timestamp=ctx.message.created_at,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}#{ctx.message.author.discriminator}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call("https://nekos.life/api/v2/img/nsfw_neko_gif")
            )
            await ctx.message.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="HoldUp!!",
                description="This command can only be used in a NSFW channel.",
                color=0xFF0000,
                timestamp=ctx.message.created_at,
            )
            await ctx.message.reply(embed=embed, delete_after=20)

    @commands.cooldown(5, 7, commands.BucketType.user)
    @commands.command(name="futanari")
    async def futanari(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="...",
                color=ctx.message.author.color,
                timestamp=ctx.message.created_at,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}#{ctx.message.author.discriminator}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call("https://nekos.life/api/v2/img/futanari")
            )
            await ctx.message.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="HoldUp!!",
                description="This command can only be used in a NSFW channel.",
                color=0xFF0000,
                timestamp=ctx.message.created_at,
            )
            await ctx.message.reply(embed=embed, delete_after=20)
    
    @commands.cooldown(5, 7, commands.BucketType.user)
    @commands.command(name="boobs", aliases=["boob"])
    async def boobs(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="**Tiddies**!!!!!",
                color=ctx.message.author.color,
                timestamp=ctx.message.created_at,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}#{ctx.message.author.discriminator}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name, icon_url=self.bot.user.avatar_url
            )
            embed.set_image(url=await api_call("https://nekos.life/api/v2/img/boobs"))

            await ctx.message.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="HoldUp!!",
                description="This command can only be used in a NSFW channel.",
                color=0xFF0000,
                timestamp=ctx.message.created_at,
            )
            await ctx.message.reply(embed=embed, delete_after=20)


def setup(bot):
	bot.add_cog(nsfw(bot))
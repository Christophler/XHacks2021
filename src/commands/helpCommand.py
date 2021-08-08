import discord

class HelpCommand:
    def __init__(self, names, settings):
        self.settings = settings
        self.names = names
        
    def getNames(self):
        return self.names
        
    async def run(self, message, args):
        
        # build embed
        embed = discord.Embed(title="Commands",
                               description="Thank you for using MoneyMoneyStocksBot (by Jeremy, Christopher, and Henry)")
        embed.set_image(url=("https://g.foolcdn.com/editorial/images/637254/stock-up-glowing-green-arrow-climbs-on-a-stock-screen.jpg"))
        embed.set_thumbnail(url="https://www.cnet.com/a/img/uaUy0yK-_-dwdVo_pzqVS3d48hI=/1200x630/2021/04/01/05b0b37a-2c25-4ea0-941c-c9db574e94e5/16br-stonks-motd-1920x1080-1920x1080-d7e1e18d423d.jpg")
        embed.set_author(name="MoneyMoneyStocksBot", url="https://discord.com/api/oauth2/authorize?client_id=873654361438433300&permissions=8&scope=bot", icon_url="https://www.cnet.com/a/img/uaUy0yK-_-dwdVo_pzqVS3d48hI=/1200x630/2021/04/01/05b0b37a-2c25-4ea0-941c-c9db574e94e5/16br-stonks-motd-1920x1080-1920x1080-d7e1e18d423d.jpg")
        cmd_prefix = self.settings.getAttribute('command_prefix')
        embed.add_field(name="Command Prefix", value=cmd_prefix)
        embed.add_field(name="Stock Command", value=(cmd_prefix + "stock <stock_name> - View the stock's progress in the last 7 days"))
        embed.add_field(name="Stocks Command", value=(cmd_prefix + "stocks - View the stocks you can see"))
        embed.add_field(name="Use On Your Own Discord", value=("https://tinyurl.com/moneymoneystocksbot"))
        await message.channel.send(embed=embed, content=("<@" + str(message.author.id) + ">"))

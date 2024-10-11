# Kütüphanelerin içe aktarılması

import discord
from discord.ext import commands
import random

# Ayarlamalar

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Konsoldan durum kontrolü

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptım!')

# Yardım komudu

@bot.command()
async def yardim(ctx):
    await ctx.send("""**Eagle Bot Komutları:**
                   **  !selam: ** Kullanıcıya selam verir.
                   **  !sayitahmin: ** Sayı tahmin oyunu başlatır.
                   **  !tahmin <sayı>: ** Sayı tahmin oyununda tahmin yapabilmek için kullanılır.""")

# Selamlama

@bot.command()
async def selam(ctx):
    await ctx.send(f"Selamlar {ctx.author.mention}, nasılsın?")

# Sayı tahmin oyunu

bilinecekSayi = None
oyuncu = None
tahminSayisi = 0

@bot.command()
async def sayitahmin(ctx):
    global bilinecekSayi
    global oyuncu
    oyuncu = ctx.author
    bilinecekSayi = random.randint(1, 100)
    await ctx.send("""**Sayı tahmin etme oyunu başladı. Sayıyı tahmin etmek için "!tahmin <sayı>" yazabilirsiniz.** """)
    await ctx.send("**Unutmadan söyleyeyim, sayı 1-100 arasında!**")

@bot.command()
async def tahmin(ctx, tahmin: int):
    global bilinecekSayi
    global tahminSayisi
    global oyuncu

    if bilinecekSayi is None:
        await ctx.send("Tahmin yapabilmek için oyunu başlatmalısınız.")
    elif oyuncu != ctx.author:
        await ctx.send("**Oyunu siz başlatmadınız, başkasının oyununa karışmayın.**")
    elif tahmin < bilinecekSayi:
        tahminSayisi += 1
        await ctx.send("Daha büyük bir sayı girmelisin!")
    elif tahmin > bilinecekSayi:
        tahminSayisi += 1
        await ctx.send("Daha küçük bir sayı girmelisin!")
    else:
        tahminSayisi += 1
        await ctx.send(f"**Tebrikler! Sayıyı bildiniz. Oyun bitti. Yapılan tahmin sayısı: {tahminSayisi}**")
        bilinecekSayi = None
        oyuncu = None
        tahminSayisi = 0

# Hazır cevaplar

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "merhaba oğlum" and message.author.name == "mayemi":
        await message.channel.send("Merhaba baba!")
    await bot.process_commands(message)

#Token

bot.run('YOUR TOKEN HERE')

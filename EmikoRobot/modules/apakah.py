import random
from EmikoRobot.events import register
from EmikoRobot import telethn

APAKAH_STRING = [
    "Iya",
    "Tidak",
    "Mungkin",
    "Mungkin Tidak",
    "Bisa jadi",
    "Hah",
    "Tidak Mungkin",
    "YNTKTS",
    "Maap ga dulu",
    "Coba tanya [Zea](@zeafeya)",
    "Tanya aja sama mamak kau tu pler",
]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply("Berikan saya pertanyaan 😐")
        return
    await event.reply(random.choice(APAKAH_STRING))

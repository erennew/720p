import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os, asyncio, pyrogram, psutil, platform, time
from bot import data
from bot.plugins.incoming_message_fn import incoming_compress_message_f
from pyrogram.types import Message
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess


def checkKey(dict, key):
  if key in dict.keys():
    return True
  else:
    return False

def hbs(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "B", 1: "K", 2: "M", 3: "G", 4: "T", 5: "P"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"
def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "") +
        ((str(hours) + "h, ") if hours else "") +
        ((str(minutes) + "m, ") if minutes else "") +
        ((str(seconds) + "s, ") if seconds else "") +
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]

async def on_task_complete():
    del data[0]
    if len(data) > 0:
      await add_task(data[0])

async def add_task(message: Message):
    try:
        os.system('rm -rf /app/downloads/*')
        await incoming_compress_message_f(message)
    except Exception as e:
        LOGGER.info(e)  
    await on_task_complete()
async def create_temp_file(directory, extension=".mkv"):
    """Create a guaranteed unique temp file"""
    temp_count = 0
    max_attempts = 100
    while temp_count < max_attempts:
        temp_name = f"temp_{int(time.time())}_{temp_count}{extension}"
        temp_path = os.path.join(directory, temp_name)
        if not os.path.exists(temp_path):
            return temp_path
        temp_count += 1
    raise Exception("Could not create unique temp file after 100 attempts")
async def sysinfo(e):
    cpuUsage = psutil.cpu_percent(interval=0.5)
    cpu_freq = psutil.cpu_freq()
    freq_current = f"{round(cpu_freq.current / 1000, 2)} GHz"
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    ram_stats = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    dl_size = psutil.net_io_counters().bytes_recv
    ul_size = psutil.net_io_counters().bytes_sent
    message = await e.reply_text(f"<u><b>Sʏꜱᴛᴇᴍ Sᴛᴀᴛꜱ 🧮</b></u>\n"
                                 f"<blockquote><b>🎖️ CPU Freq:</b> {freq_current}\n"
                                 f"<b>CPU Cores [ Physical:</b> {cpu_count} | <b>Total:</b> {cpu_count_logical} ]\n\n"
                                 f"<b>💾 Total Disk :</b> {psutil._common.bytes2human(disk.total)}B\n"
                                 f"<b>Used:</b> {psutil._common.bytes2human(disk.used)}B | <b>Free:</b> {psutil._common.bytes2human(disk.free)}B\n\n"
                                 f"<b>🔺 Total Upload:</b> {psutil._common.bytes2human(ul_size)}B\n"
                                 f"<b>🔻 Total Download:</b> {psutil._common.bytes2human(dl_size)}B\n\n"
                                 f"<b>🎮 Total Ram :</b> {psutil._common.bytes2human(ram_stats.total)}B\n"
                                 f"<b>Used:</b>{psutil._common.bytes2human(ram_stats.used)}B | <b>Free:</b> {psutil._common.bytes2human(ram_stats.available)}B\n\n"
                                 f"<b>🖥 CPU:</b> {cpuUsage}%\n"
                                 f"<b>🎮 RAM:</b> {int(ram_stats.percent)}%\n"
                                 f"<b>💿 DISK:</b> {int(disk.percent)}%</blockquote>")

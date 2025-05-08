import asyncio
import sys
from shazamio import Shazam


async def main():
  shazam = Shazam()
  # out = await shazam.recognize_song('dora.ogg') # slow and deprecated, don't use this!
  out = await shazam.recognize(sys.argv[1])  # rust version, use this!
  print(out)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

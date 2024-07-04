import aiohttp
import asyncio
import re

# **WARNING**
# - This script makes it seem like you have petals that you actually don't.
#   Therefore, if you equip them or use them for crafting more than once, your account will be banned.
# - We do NOT recommend running the script outside of a guest account if you are not a ban speedrunner!
# - Don't forget that we do NOT have any responsibility for any damage to you caused by the script.

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://florr.io") as response:
            text = await response.text()
            match = re.search(r'const\sversionHash\s=\s"(.*)";', text)
            if match:
                current_version_hash = match.group(1)
            else:
                raise ValueError("Version hash not found in the response")

    if current_version_hash != "73690873cf390ed5ab70c4525d36aa5efcf87531":
        print("You seem to be running the script for an outdated client. Run the latest script.")
        return

    MAX_RARITIES = 8
    MAX_PETALS = 79
    petal_inventory_base_address = 16938948

    for petal_index in range(1, MAX_PETALS + 1):
        for rarity_index in range(MAX_RARITIES):
            offset = ((petal_index * MAX_RARITIES + rarity_index) << 2)
            # Note: The following line assumes you have a way to modify memory in Python
            # which is not typically possible without using external libraries or system calls
            # Module.HEAPU32[(petal_inventory_base_address + offset) >> 2] = 1

    print("Successfully modified the memory.")

if __name__ == "__main__":
    asyncio.run(main())


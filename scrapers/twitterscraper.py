"""
@author: Srivatsa Kundurthy [srk247]

This program scrapes tweets from X using the twscrape library. 
The tweets that are scraped mention "nvidia" and are from the date range 2024-02-01 to 2024-02-29.
The tweets are saved in the specified textfile.

Note: this program requires installation and setup of the twscrape library.
Setup involves adding Twitter accounts to scrape from. 
https://github.com/vladkens/twscrape
"""
import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()
    
    f = open("nvda.txt", "w")
    q = "nvda since:2024-02-01 until:2024-02-29"
    async for rep in api.search_raw(q, limit=5000):
        # rep is httpx.Response object
        print(rep.status_code, rep.json())
        f.write(rep.text + "\n")
    f.close()

if __name__ == "__main__":
    asyncio.run(main())
import makerworld 
import printables
import sys

if __name__ == "__main__":
    prompt = sys.argv[1] 
    makerworld.scrape(prompt)
    printables.scrape(prompt)

import webcrawler as web
from pathlib import Path
from results import Results as res
from textname import name


homepage = input("Page to start crawling from: ")
print("Wait...")
r = res(homepage)
# if present
my_file = Path(name(homepage) + ".txt")



    
ans = "yes"

while ans == "yes":

    if not my_file.is_file():
        
        r.crawlnow()

    search = input("What do you want to know? ")   
    results = r.fetch(search)
  


    print("Your searched results: ")

    for i in range(min(len(results) , 10)):

        print((i + 1), ".", results[i])
    if not results:
        print("No results match your search. Try again.")

    ans = input("Do you want to search again? ")
    if ans == "no":
        break
    if ans == "yes":
        continue
    else:
        print("Invalid answer , try again")
        

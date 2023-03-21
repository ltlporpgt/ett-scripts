import tikolutool
import time

print("PageMonitor")
print("Please enter a comma separated list of pages.")
pagelist = input(">>")
pagelist = pagelist.split(',')

known_pages = {}
print("[*] Getting initial state of pages...")
for page in pagelist:
  known_pages[page] = tikolutool.get_page(page,print_log=False)
print("[*] Starting monitoring...")
while True:
  for page in pagelist:
    page_content = tikolutool.get_page(page, print_log=False)
    if page_content == known_pages[page] or page_content == '':
        pass
    else:
      print(f"[!] Page /{page} has updated!")
      print(get_edits_string(known_pages[page], page_content))
      known_pages[page] = page_content
  time.sleep(5)

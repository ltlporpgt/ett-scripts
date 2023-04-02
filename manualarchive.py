import json
import tikolutool
import texttool

# This tool was made in ~30 minutes, due to a finding that I needed to act upon quickly.
# No gurantees as to its quality, but it does work well enough to archive a few important pages.

print("<(o)> Welcome to manualarchive.")
print("Good for archiving those pages that are hidden.") # _Those_ pages. :)

archive = {}

archived = []

xas=input("Use pre-existing pagearchive.json? y/n:")
if xas == 'y':
	file=open('pagearchive.json','r')
	unloaded = file.read()
	file.close()
	archive = json.loads(unloaded)

unscanned = []

try:
	while 1:
		unscanned=[input('page>')]
		while len(unscanned) != 0:
			page = unscanned.pop(0)
			print(f"Checking page {page}...")
			if page in archived:
				print("Page already archived!")
				pass
			ans=input("Archive? y/n>")
			if ans != 'y': # Just to be safe, this is very manual. :)
				pass
			else:
				archived.append(page)
				content = tikolutool.get_page(page)
				if content == '':
					print("Page blank. Will not archive.")
#				elif '$$  _|$' in content:
#					print("Looks like we already got to it. Nothing to archive :(")
				else:
					print("Page is not blank! Archiving...")
					archive[page] = content
					print("Scanning for links...")
					links = texttool.grab_links(content)
					for link in links:
						if link in archived:
							pass
						elif link in unscanned:
							pass
						else:
							unscanned.append(link)
except KeyboardInterrupt:
	print("Alright, time to save!")
	pagearchive=json.dumps(archive)
	file = open('pagearchive.json','w')
	file.write(pagearchive)
	file.close()
	print("Saved to pagearchive.json :)")

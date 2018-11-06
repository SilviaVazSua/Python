# Table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.

table_of_contents = {
	"Chapter 1: Getting Started": "page 1",
	"Chapter 2: Numbers": "page 9",
	"Chapter 3: Letters": "page 13"
	}

print("Table of Contents".center(50), "\n")

for x, y in table_of_contents.items():
	n = len(x)
	print(x.ljust(0), y.rjust(50-n, "."))

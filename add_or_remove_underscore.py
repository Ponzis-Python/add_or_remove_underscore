#adds or removes underscores from input string, prints result
src = input("Paste string here: ")

if '_' in src:
	dst = src.replace("_", " ")
else:
	dst = src.replace(" ", "_")

print(dst)
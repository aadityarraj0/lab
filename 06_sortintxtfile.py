content = open("input.txt").read()

words = content.split()
words.sort()

outfile = open("sorted_output.txt", "w")

for i in words:
    outfile.write(i + "\n")

outfile.close()
print("Words sorted successfully! Check 'sorted_output.txt'")

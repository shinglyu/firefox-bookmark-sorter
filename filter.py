import csv

with open('sqloutput.csv', 'rb') as f:
    r = csv.reader(f, delimiter=',', quotechar='"')
    lines = list(r)

output = []
for row in lines:
    url = row[1]
    # If there are https equivalent, skip the http one
    if url.replace('http', 'https') in map(lambda x:x[1], lines):
        continue
    output.append(row)

print("File saved to filtered.csv")
with open('filtered.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in output:
        spamwriter.writerow(row)

#print output

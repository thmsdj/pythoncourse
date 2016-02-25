import os
 
# Following is the directory with log files,
# On Windows substitute it where you downloaded the files
root = "/var/log/apache2"
 
for filename in os.listdir(root):
    if not filename.startswith("access.log"):
        print "Skipping unknown file:", filename
        continue
    if filename.endswith(".gz"):
        print "Skipping compressed file:", filename
        continue
    print "Going to process:", filename
    for line in open(os.path.join(root, filename)):
        # Copypasted from the previous example
        total = total + 1
        try:
                source_timestamp, request, response, _, _, agent, _ = line.split("\"")
                method, path, protocol = request.split(" ")

                for keyword in keywords:
                    if keyword in agent:
                        d[keyword] = d.get(keyword, 0) + 1
        except ValueError:
                pass # This will do nothing
# Print the results
print "Total requests:", total
print d
print "Total lines with requested keywords:", sum(d.values())
l = d.items()
l.sort(key = lambda t:t[1], reverse=True) #Same as:
#l.sort = lambda (key, value):-value) # will not work in python 3
for key, value in l:
        print key, "===>", value, "(", value * 100 / total, "%)"
        print "%s => %d (%.02f%%)" % (key, value, value * 100.0 / total)


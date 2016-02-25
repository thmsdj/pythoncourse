practices for home

#Most visited URL?
#Most used user agent?
#Most used OS?

# l = d.items()
# l.sort(key = lambda t:t[1])

fh = open("access.log")

keywords = "Windows", "Linux", "OS X", "Ubuntu", "Android", "iPhone", "Googlebot", "bingbot"
d = {}
win = 0 #create integer variable and name it win
total = 0 #create another integer variable 
mac = 0

for line in fh:
        total = total + 1
        try:
                source_timestamp, request, response, _, _, agent, _ = line.split("\"")
                method, path, protocol = request.split(" ")

                for keyword in keywords:
                    if keyword in agent:
                        d[keyword] = d.get(keyword, 0) + 1
#                      try:
#                          d[keyword] = d[keyword] + 1
#                      except KeyError:
#                          d[keyword] = 1
#                      break # Stop searching for other keywords
#               if "Windows" in agent:
#                       win = win + 1
#               if "Mac" in agent:
#                       mac = mac + 1
#               print "User visited URL: http://enos.itcollege.ee" + path
#               print "agent", agent
#               print "--"
        except ValueError:
                pass # This will do nothing
#               print "Failed to parse", line

print "Total requests:", total
print d
print "Total lines with requested keywords:", sum(d.values())
l = d.items()
l.sort(key = lambda t:t[1], reverse=True) #Same as:
#l.sort = lambda (key, value):-value) # will not work in python 3
for key, value in l:
        print key, "===>", value, "(", value * 100 / total, "%)"
        print "%s => %d (%.02f%%)" % (key, value, value * 100.0 / total)
#print "Total requests:", total
#print "Requests from Windows:", win
#print "Requests from Mac computers:", mac

#print "Mac percentage:", format(mac * 100.0 / total , '.2f') + "%"
#print "Windows percentage:", format(win * 100.0 / total , '.2f') + "%"


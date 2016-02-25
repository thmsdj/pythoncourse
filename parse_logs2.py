import os
import gzip
import urllib
import argparse

# Following is the directory with log files,
# On Windows substitute it where you downloaded the files

keywords = "Windows", "Linux", "OS X", "Ubuntu", "Android", "iPhone", "Googlebot", "bingbot"
d = {}

urls = {}
users = {}
total = 0

parser = argparse.ArgumentParser(description='Apache2 log parser')
parser.add_argument('--path', help='Path to Apache2', default="/var/log/apache2")
parser.add_argument('--top-urls', help="Find top URLs", action='store_true')
parser.add_argument('--geoip', help="Resolve IPs to country codes", action='store_true')
parser.add_argument('--verbose', help="Increase verbosity", action='store_true')
args = parser.parse_args()

print "We are expecting logs from:", args.path						

for filename in os.listdir(args.path):

    if not filename.startswith("access.log"):
        continue
    if args.verbose:
        print "Parsing ...", filename
    if filename.endswith(".gz"):
        fh = gzip.open(os.path.join(args.path, filename))
   
    else:
        fh = open(os.path.join(args.path, filename))
    print "Going to process:", filename
    for line in fh:
        # Copypasted from the previous example
        total = total + 1
        try:
                source_timestamp, request, response, _, _, agent, _ = line.split("\"")
                method, path, protocol = request.split(" ")
                #dont forget to import urllib
                path = urllib.unquote(path)
                if path.startswith("/~"):
                    username, remainder = path[2:].split("/", 1)
                    try:
                        users[username] = users[username] + 1
                    except:
                        users[username] = 1

                url = "http://enos.itcollege.ee" + path
                try:
                    urls[url] = urls[url] +1
                except:
                    urls[url] = 1             
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
#for key, value in l:
#        print key, "===>", value, "(", value * 100 / total, "%)"
#        print "%s => %d (%.02f%%)" % (key, value, value * 100.0 / total)


print("Top 5 visited users:")
results = users.items()
results.sort(key = lambda item:item[1], reverse=True)
for user, hits in results[:5]:
    print user, "===>", hits, "(", hits * 100 / total, "%)"

results = urls.items()
results.sort(key = lambda item:item[1], reverse=True)
for keyword, hits in results[0:10]:
    print keyword, "===>", hits, "(", hits * 100 / total, "%)" 
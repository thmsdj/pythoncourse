import argparse

parser = argparse.ArgumentParser(description='Apache2 log parser')
parser.add_argument('--path', help='Path to Apache2', default="/var/log/apache2")
parser.add_argument('--top-urls', help="Find top URLs")
parser.add_argument('--geoip', help="Resolve IPs to country codes", action='store_true')

args = parser.parse_args()
print "We are expecting logs from:", args.path						

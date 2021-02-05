from jnpr.junos import Device
from lxml import etree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-device', help='Input host name', type=str)
parser.add_argument('-user', help='Input user name', type=str)
parser.add_argument('-password', help='Input password', type=str)
parser.add_argument('-interface', help='Input interface name', type=str)
parser.add_argument('-output_format', help='output format', type=str)


args,unknown = parser.parse_known_args()
device = args.device or device
user = args.user or user
password = args.password or password
output_format = args.output_format or output_format

dev = Device(host=device, user= user,password=password,gather_facts=False)
dev.open()


cnf = dev.rpc.get_config(options={'format':output_format})
print(etree.tostring(cnf))
dev.close()
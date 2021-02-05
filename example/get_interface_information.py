from jnpr.junos import Device
from lxml import etree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-device', help='Input host name', type=str)
parser.add_argument('-user', help='Input user name', type=str)
parser.add_argument('-password', help='Input password', type=str)
parser.add_argument('-interface', help='Input interface name', type=str)



args,unknown = parser.parse_known_args()
device = args.device or device
user = args.user or user
password = args.password or password
interface = args.interface or interface

dev = Device(host=device, user= user,password=password,gather_facts=False)
dev.open()


op = drv.rpc.get_interface_information({'format':'xml'}, interface_name=interface, terse=True)
print(etree.tostring(op))
dev.close()
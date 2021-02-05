from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-device', help='Input host name', type=str)
parser.add_argument('-user', help='Input user name', type=str)
parser.add_argument('-password', help='Input password', type=str)


args,unknown = parser.parse_known_args()
device = args.device or device
user = args.user or user
password = args.password or password


dev = Device(host=device, user= user,password=password,gather_facts=False)
dev.open()

cu = Config(dev)
data = """<policy-options>
            <policy-statement action="delete">
                <name>TEST</name>
                <term>
                    <name>1</name>
                    <from>
                        <protocol>mpls</protocol>
                    </from>
                    <then>
                        <accept />
                    </then>
                </term>
            </policy-statement>
        </policy-options>"""

cu.load(data)
if cu.commit_check():
    cu.commit()
else:
    cu.rollback()



dev.close()
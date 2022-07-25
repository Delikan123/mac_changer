import subprocess
import optparse
import re





opt_object=optparse.OptionParser()

def user_input():
    opt_object.add_option("-i","--interface",dest="interface",help="mac_started")
    opt_object.add_option("-m","--mac",dest="mac_address",help="mac_started")
    return opt_object.parse_args()


def change_mac(user_interface,user_mac):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
    subprocess.call(["ifconfig",user_interface,"up"])

def control(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    new_control=re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_control:
        return new_control.group(0)
    else:
        return None






(user_input,args)=user_input()
change_mac(user_input.interface,user_input.mac_address)
print("mac change")

new_control1=control(str(user_input.interface))
if new_control1==user_input.mac_address:
    print("Success")
else:
    print("Error")









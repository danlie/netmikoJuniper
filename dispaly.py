from tenacity import retry


from netmiko import ConnectHandler
import dispaly
junipersw88_2 = {
	'device_type': 'juniper',
	'host':   '192.168.88.2',
	'username': 'root',
	'password': 'juniper123',
	'port' : 22,
}
net_connect = ConnectHandler(**junipersw88_2)
def displayset(junoscommand):
    output = net_connect.send_command('{}'.format(junoscommand))
    print(output)
# This is test

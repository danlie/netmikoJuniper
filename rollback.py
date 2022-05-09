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
rollback_res = ["rollback rescue"]
net_connect.send_config_set(rollback_res, exit_config_mode=False)
net_connect.commit()
exit_config_mode = ['exit']
net_connect.send_config_set(exit_config_mode, exit_config_mode=False)
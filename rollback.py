rollback_res = ["rollback rescue"]
net_connect.send_config_set(rollback_res, exit_config_mode=False)
net_connect.commit()
exit_config_mode = ['exit']
net_connect.send_config_set(exit_config_mode, exit_config_mode=False)
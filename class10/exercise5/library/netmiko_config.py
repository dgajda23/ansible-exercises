from ansible.module_utils.basic import AnsibleModule

netmiko_found = False
try:
    from netmiko import ConnectHandler

    netmiko_found = True
except ImportError:
    pass

def main():
    module_args = dict(
        host=dict(type="str", required=True),
        device_type=dict(type="str", required=True),
        username=dict(type="str", required=False),
        password=dict(type="str", required=False, no_log=True),
        config_list=dict(type="list", required=True),
    )

    module = AnsibleModule(argument_spec=module_args)
    result = dict(changed=False, msg="")

    host = module.params["host"]
    device_type = module.params["device_type"]
    username = module.params["username"]
    password = module.params["password"]
    config_list = module.params["config_list"]

    if not config_list:
        module.exit_json(**result)

    net_connect = ConnectHandler(
        host=host, device_type=device_type, username=username, password=password
    )
    result["changed"] = True
    output = net_connect.send_config_set(config_list)
    result["output"] = output
    module.exit_json(**result)

if __name__ == "__main__":
    main()

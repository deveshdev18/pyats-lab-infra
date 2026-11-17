# pyats-lab-infra

Shared Cisco IOS-XE test automation functions (the "infrastructure" or toolbox),
written in the style of Cisco Genie SDK APIs.

Every function works against a **simulated IOS-XE router** held in memory, so test
scripts run without a real lab.

| Module | Functions |
|---|---|
| `pyats_lab.device` | `connect_device`, `disconnect_device`, `is_device_connected`, `get_software_version`, `get_hostname`, `configure_hostname`, `save_running_config`, `is_running_config_saved` |
| `pyats_lab.vlan` | `configure_vlan`, `vlan_exists`, `get_vlan_name`, `list_vlans`, `unconfigure_vlan` |
| `pyats_lab.interface` | `shut_interface`, `unshut_interface`, `get_interface_status`, `configure_interface_description`, `get_interface_description`, `get_interface_input_errors` |
| `pyats_lab.routing` | `get_ospf_neighbor_state`, `list_ospf_neighbors` |
| `pyats_lab.connectivity` | `execute_ping` |
| `pyats_lab.health` | `get_cpu_utilization`, `get_free_memory_percent` |

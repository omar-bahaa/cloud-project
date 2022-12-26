'''
creating ISCSI
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/online-storage-management#target-setup-create-iscsi-target
and everything after that 
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/osm-create-iscsi-initiator
API
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-iscsi#iscsi-api
'''



#Discover targets at a given IP address:
iscsi_discover_ip = lambda ip: f"iscsiadm --mode discoverydb --type sendtargets --portal {ip} --discover\n"
#Login, must use a node record id found by the discovery:
iscsi_login = lambda ip, portnum, discovered_ip: "iscsiadm --mode node --targetname {discovered_ip}:test --portal {ip}:{portnum} --login\n"
#Logout
iscsi_logout = lambda ip, portnum, discovered_ip: f"iscsiadm --mode node --targetname {discovered_ip}:test --portal {ip}:{portnum} --logout\n"
#list node records
iscsi_list_records = lambda : f"iscsiadm --mode node\n"
# Display all data for a given node record
iscsi_display_node = lambda ip, portnum, discovered_ip : f"iscsiadm --mode node --targetname {discovered_ip}:test --portal {ip}:{portnum}\n"

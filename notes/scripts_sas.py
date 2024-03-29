# aliases
make_alias = lambda phy, alias: f"alias create {alias} {phy}\n"
del_alias = lambda alias: f"alias delete single {alias}\n"
delall_alias = "alias delete all noconfirm\n"

# zonegroups
create_zonegr = lambda name: f"zonegroup create {name}\r"
del_zonegr = lambda zonegr: f"zonegroup delete single {zonegr}\r"
delall_zonegr = "zonegroup delete all noconfirm\r"
add_zonegr = lambda zonegr, expander, phy: f"zonegroup add {zonegr} {expander}:{phy}\r"
rm_zonegr = lambda zonegr, expander, phy: f"zonegroup remove {zonegr} {expander}:{phy}\r"

# zonesets
create_zones = lambda name: f"zoneset create {name}\r"
del_zones = lambda zones: f"zoneset delete single {zones}\r"
delall_zones = "zoneset delete all noconfirm\r"
add_zones = lambda zones, zonegr1, zonegr2: f"zoneset add {zones} {zonegr1} {zonegr2}\r"
rm_zones = lambda zones, zonegr1, zonegr2: f"zoneset remove {zones} {zonegr1} {zonegr2}\r"
act_zones = lambda zones, passw: f"zoneset activate {zones}\n{passw}\r\r"
deact_zones = lambda passw: f"zoneset deactivate\n{passw}\r\r"
passwd = lambda zones, opass, npass: f"{opass}\r\r{npass}\r\r{npass}\r\r"


"""
Expanders:
- SAS_ConnectionBlade_06 (connected to all bladeservers, SX980_07, and SX980_15)
- SAS_ConnectionBlade_05 (connected to all bladeservers, SX980_07, and SX980_15)
- SX980_07 (connected to SAS_ConnectionBlade_06 and 10 HDD disks)
- SX980_15 (connected to SAS_ConnectionBlade_06 and 10 HDD disks)

Each expander has phy number (SAS_ConnectionBlade_06,05 00:63, SX980_07's 00:21, and SX980_15 00:21) which corresponds to connection port number,
which is connected to another device as a ServerBlade, HDD disk, or even an expander.

Adding to a zonegroup requires an expander and the phy connected to that expander to be added.
Expanders are almost all aliased (SAS_ConnectionBlade_06 is an alias). Real names are called SAS Address.
"""

"""
To activate a zoneset we need to deactivate any activated zoneset. Only 1 may be activated.
After entering a passwd for activation or deactivation, double enter is needed.
"""

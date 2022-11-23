# aliases
make_alias = lambda phy, alias: f"alias create {alias} {phy}\n"
del_alias = lambda alias: f"alias delete single {alias}\n"
delall_alias = "alias delete all noconfirm\n"

# zonegroups
create_zonegr = lambda name: f"zonegroup create {name}\n"
del_zonegr = lambda zonegr: f"zonegroup delete single {zonegr}\n"
delall_zonegr = "zonegroup delete all noconfirm\n"
add_zonegr = lambda zonegr, expander, phy: f"zonegroup add {zonegr} {expander}:{phy}\n"
rm_zonegr = lambda zonegr, expander, phy: f"zonegroup remove {zonegr} {expander}:{phy}\n"

# zonesets
create_zones = lambda name: f"zoneset create {name}\n"
del_zones = lambda zones: f"zoneset delete single {zones}\n"
delall_zones = "zoneset delete all noconfirm\n"
add_zones = lambda zones, zonegr1, zonegr2: f"zoneset add {zones} {zonegr1} {zonegr2}\n"
rm_zones = lambda zones, zonegr1, zonegr2: f"zoneset remove {zones} {zonegr1} {zonegr2}\n"


"""
Expanders:
- SAS_ConnectionBlade_06 (connected to all bladeservers, SX980_07, and SX980_15)
- SX980_07 (connected to SAS_ConnectionBlade_06 and 10 HDD disks)
- SX980_15 (connected to SAS_ConnectionBlade_06 and 10 HDD disks)

Each expander has phy number (SAS_ConnectionBlade_06 00:63, SX980_07's 00:21, and SX980_15 00:21) which corresponds to connection port number,
which is connected to another device as a ServerBlade, HDD disk, or even an expander.

Adding to a zonegroup requires an expander and the phy connected to that expander to be added.
Expanders are almost all aliased (SAS_ConnectionBlade_06 is an alias). Real names are called SAS Adress.
"""

"""
To activate a zoneset we need to deactivate any activated zoneset. Only 1 may be activated
After entering a passwd for activation or deactivation, double enter is needed.
"""
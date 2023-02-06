# def get_device_name(phy, table_str):
#     data=table_str.split("Attached SATA Port Selector")[1]
#     print(data)
#     table = [line.split() for line in data.strip().split("\n")[2:]]
#     for line in table:
#         if line[0].endswith(f"{phy:02d}"):
#             return line[5]
#     return None

def get_device_name(given_expndr_phy,table_str):
    data=table_str.split("Attached SATA Port Selector")[1]
    lines = data.split("\n")
    device_names = {}
    for line in lines[7:]:
        fields = line.split()

        if len(fields) > 0:
            expndr=fields[0]
            phy = fields[1]
            expndr_phy=expndr+"_"+phy
            device = fields[6]
            if device != "----------------":
                device_names[expndr_phy] = device
            else:
                device_names[expndr_phy] = "None"
    print(device_names)
    if given_expndr_phy in device_names.keys():
        return device_names[given_expndr_phy]
    else:
        return "error: expander and physical port does not exist, please specify them in the form: ExpandeName_PhysNumber"



# table_str = """
#                Phy                                     Attached
# ===================================== ==========================================
# Alias /                               Alias /               Device  Capabilities
# ------------------------------------- ------------------------------------------
# SAS_ConnectionB* 00  T   -   6.0  *    ServerBlade_01   005  End       111000000
# SAS_ConnectionB* 01  T   -   6.0  *    ServerBlade_01   004  End       111000000
# SAS_ConnectionB* 02  T   -   6.0  *    ServerBlade_09   005  End       111000000
# SAS_ConnectionB* 03  T   -   6.0  *    ServerBlade_09   004  End       111000000
# SAS_ConnectionB* 04  T   -   6.0  *    ServerBlade_02   005  End       111000000
# SAS_ConnectionB* 05  T   -   6.0  *    ServerBlade_02   004  End       111000000
# SAS_ConnectionB* 06  T   -   6.0  *    ServerBlade_10   005  End       111000000
# SAS_ConnectionB* 07  T   -   6.0  *    ServerBlade_10   004  End       111000000
# SAS_ConnectionB* 08  T   -   6.0  *    ServerBlade_03   005  End       111000000
# SAS_ConnectionB* 09  T   -   6.0  *    ServerBlade_03   004  End       111000000
# SAS_ConnectionB* 10  T   -    -   *    ---------------- ---  None      000000000
# """
new_str="""Notes:
  - RA - Routing Attributes :  * phy is an Invalid T to T link.
  - VP   - Virtual PHY
  - LS/S - Link Speed/Status:  1.5|3.0|6.0 Gb/s
                              - phy enabled but link uninitialized
                              * phy disabled
  - ZG   - Zone Grp
    Zoning Active:  Zone Group Number
    Zoning Inactive:  * phy may be assigned to a zone group
                      - phy may not be assigned to a zone group
  - Capabilities
     1xxxxxxxx - Attached SMP Initiator
     x1xxxxxxx - Attached STP Initiator
     xx1xxxxxx - Attached SSP Initiator
     xxx1xxxxx - Attached SATA Host
     xxxx1xxxx - Attached SMP Target
     xxxxx1xxx - Attached STP Target
     xxxxxx1xx - Attached SSP Target
     xxxxxxx1x - Attached SATA Target
     xxxxxxxx1 - Attached SATA Port Selector

                Phy                                     Attached
===================================== ==========================================
Alias /                               Alias /               Device  Capabilities
SAS Address      Phy RA VP LS/S  ZG   SAS Address      Phy  Type      IIIITTTTS
------------------------------------- ------------------------------------------
SAS_ConnectionB* 00  T   -   6.0  *    ServerBlade_01   005  End       111000000
SAS_ConnectionB* 01  T   -   6.0  *    ServerBlade_01   004  End       111000000
SAS_ConnectionB* 02  T   -   6.0  *    ServerBlade_09   005  End       111000000
SAS_ConnectionB* 03  T   -   6.0  *    ServerBlade_09   004  End       111000000
SAS_ConnectionB* 04  T   -   6.0  *    ServerBlade_02   005  End       111000000
SAS_ConnectionB* 05  T   -   6.0  *    ServerBlade_02   004  End       111000000
SAS_ConnectionB* 06  T   -   6.0  *    ServerBlade_10   005  End       111000000
SAS_ConnectionB* 07  T   -   6.0  *    ServerBlade_10   004  End       111000000
SAS_ConnectionB* 08  T   -   6.0  *    ServerBlade_03   005  End       111000000
SAS_ConnectionB* 09  T   -   6.0  *    ServerBlade_03   004  End       111000000
SAS_ConnectionB* 10  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 11  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 12  T   -   6.0  *    ServerBlade_04   005  End       111000000
SAS_ConnectionB* 13  T   -   6.0  *    ServerBlade_04   004  End       111000000
SAS_ConnectionB* 14  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 15  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 16  T   -   6.0  *    ServerBlade_05   005  End       111000000
SAS_ConnectionB* 17  T   -   6.0  *    ServerBlade_05   004  End       111000000
SAS_ConnectionB* 18  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 19  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 20  T   -   6.0  *    ServerBlade_06   005  End       111000000
SAS_ConnectionB* 21  T   -   6.0  *    ServerBlade_06   004  End       111000000
SAS_ConnectionB* 22  T   -   6.0  *    ServerBlade_14   005  End       111000000
SAS_ConnectionB* 23  T   -   6.0  *    ServerBlade_14   004  End       111000000
SAS_ConnectionB* 24  T   -   6.0  -    SX980_07         016  ZExpander 000010000
SAS_ConnectionB* 25  T   -   6.0  -    SX980_07         017  ZExpander 000010000
SAS_ConnectionB* 26  T   -   6.0  -    SX980_15         018  ZExpander 000010000
SAS_ConnectionB* 27  T   -   6.0  -    SX980_15         019  ZExpander 000010000
SAS_ConnectionB* 28  T   -   6.0  -    SX980_07         018  ZExpander 000010000
SAS_ConnectionB* 29  T   -   6.0  -    SX980_07         019  ZExpander 000010000
SAS_ConnectionB* 30  T   -   6.0  -    SX980_15         016  ZExpander 000010000
SAS_ConnectionB* 31  T   -   6.0  -    SX980_15         017  ZExpander 000010000
SAS_ConnectionB* 32  T   -   6.0  *    ServerBlade_17   005  End       111000000
SAS_ConnectionB* 33  T   -   6.0  *    ServerBlade_17   004  End       111000000
SAS_ConnectionB* 34  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 35  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 36  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 37  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 38  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 39  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 40  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 41  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 42  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 43  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 44  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 45  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 46  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 47  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 48  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 49  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 50  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 51  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 52  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 53  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 54  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 55  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 56  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 57  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 58  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 59  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 60  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 61  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 62  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 63  T   -    -   *    ---------------- ---  None      000000000
SAS_ConnectionB* 64  D   *   6.0  -    50030050000a1e7d 000  End       101000100
SAS_ConnectionB* 65  D   *    -   -    ---------------- ---  None      000000000
SX980_07         00  T   -   6.0  *    HDD_SAS_709      000  End       000000100
SX980_07         01  T   -   6.0  *    HDD_SAS_708      000  End       000000100
SX980_07         02  T   -   6.0  *    HDD_SAS_707      000  End       000000100
SX980_07         03  T   -   6.0  *    HDD_SAS_706      000  End       000000100
SX980_07         04  T   -   6.0  *    HDD_SAS_705      000  End       000000100
SX980_07         05  T   -   6.0  *    HDD_SAS_704      000  End       000000100
SX980_07         06  T   -   6.0  *    HDD_SAS_703      000  End       000000100
SX980_07         07  T   -   6.0  *    HDD_SAS_702      000  End       000000100
SX980_07         08  T   -   6.0  *    HDD_SAS_701      000  End       000000100
SX980_07         09  T   -   6.0  *    HDD_SAS_700      000  End       000000100
SX980_07         10  T   -    *   *    ---------------- ---  None      000000000
SX980_07         11  T   -    *   *    ---------------- ---  None      000000000
SX980_07         12  T   -    -   *    ---------------- ---  None      000000000
SX980_07         13  T   -    -   *    ---------------- ---  None      000000000
SX980_07         14  T   -    -   *    ---------------- ---  None      000000000
SX980_07         15  T   -    -   *    ---------------- ---  None      000000000
SX980_07         16  T   -   6.0  -    SAS_ConnectionB* 024  Switch    000010000
SX980_07         17  T   -   6.0  -    SAS_ConnectionB* 025  Switch    000010000
SX980_07         18  T   -   6.0  -    SAS_ConnectionB* 028  Switch    000010000
SX980_07         19  T   -   6.0  -    SAS_ConnectionB* 029  Switch    000010000
SX980_07         20  D   *   6.0  -    500300500009f0bd 000  End       101000100
SX980_07         21  D   *    -   -    ---------------- ---  None      000000000
SX980_15         00  T   -   6.0  *    HDD_SAS_1509     000  End       000000100
SX980_15         01  T   -   6.0  *    HDD_SAS_1508     000  End       000000100
SX980_15         02  T   -   6.0  *    HDD_SAS_1507     000  End       000000100
SX980_15         03  T   -   6.0  *    HDD_SAS_1506     000  End       000000100
SX980_15         04  T   -   6.0  *    HDD_SAS_1505     000  End       000000100
SX980_15         05  T   -   6.0  *    HDD_SAS_1504     000  End       000000100
SX980_15         06  T   -   6.0  *    HDD_SAS_1503     000  End       000000100
SX980_15         07  T   -   6.0  *    HDD_SAS_1502     000  End       000000100
SX980_15         08  T   -   6.0  *    HDD_SAS_1501     000  End       000000100
SX980_15         09  T   -   6.0  *    HDD_SAS_1500     000  End       000000100
SX980_15         10  T   -    *   *    ---------------- ---  None      000000000
SX980_15         11  T   -    *   *    ---------------- ---  None      000000000
SX980_15         12  T   -    -   *    ---------------- ---  None      000000000
SX980_15         13  T   -    -   *    ---------------- ---  None      000000000
SX980_15         14  T   -    -   *    ---------------- ---  None      000000000
SX980_15         15  T   -    -   *    ---------------- ---  None      000000000
SX980_15         16  T   -   6.0  -    SAS_ConnectionB* 030  Switch    000010000
SX980_15         17  T   -   6.0  -    SAS_ConnectionB* 031  Switch    000010000
SX980_15         18  T   -   6.0  -    SAS_ConnectionB* 026  Switch    000010000
SX980_15         19  T   -   6.0  -    SAS_ConnectionB* 027  Switch    000010000
SX980_15         20  D   *   6.0  -    500300500009ecfd 000  End       101000100
SX980_15         21  D   *    -   -    ---------------- ---  None      000000000
"""
print(get_device_name("SAS_ConnectionB*_00", new_str)) # ServerBlade_01
print(get_device_name("SX980_15_17", new_str)) # ServerBlade_01
print(get_device_name("SAS_ConnectionB*_10", new_str)) # None

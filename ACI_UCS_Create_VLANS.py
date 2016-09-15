#!/usr/bin/env python
#
#Script to create a VLAN Pool in ACI, create VLANS in UCS, and add those VLANs to VNIC templates within UCS.
#
#Create VLANs in UCS
#import UCS packages
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan
from ucsmsdk.ucshandle import UcsHandle
import sys
import credentials

#command line argument should be in the form of vlannumber-vlannumber (2001-2024)
vl_input = sys.argv[1]

def expand_list(vl_list):
	vl_spl = vl_list.split("-")
	beg_num = int(vl_spl[0])
	end_num = int(vl_spl[1]) + 1
	vl_range = range(beg_num, end_num)
	vl_newlist = []
	for vl_id in vl_range:
		vl_cnvrt = str(vl_id)
		vl_newlist.append(vl_cnvrt)
	print vl_newlist
	return vl_newlist


#create UCS VLANs
def create_UCS_VLAN(vl_range):
	handle = UcsHandle(credentials.UCS_login['ipaddr'], credentials.UCS_login['username'], credentials.UCS_login['password'])
	handle.login()
	for vlan_id in vl_range:
	    mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="ACI-" + vlan_id, id=vlan_id, mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", compression_type="included")
	    handle.add_mo(mo)
	handle.commit()
vl_range = expand_list(vl_input)

create_UCS_VLAN(vl_range)



# ACI_UCS_VLAN_Pools
Python script to add VLAN Pools to ACI, VLANs to UCS, and VLANs to UCS VNIC Templates.

This script references a credentials file that has a dictionary of credentials for UCS and ACI. It is called credentials.py and should be in the following format.

ACI_login = {
	'ipaddr' : '10.1.1.1',
    'username' : 'admin',
    'password' : 'acipassword'
}

UCS_login = {
	'ipaddr' : '10.1.1.1',
    'username' : 'admin',
    'password' : 'ucspassword'
}


If you don't wish to use the credentials file, you can edit the values to reflect your environment, or change them to variables that you input either through raw_input or sys.argv.

This script was tested against the following versions:
-ACI 2.0(1m)
-UCSM 3.1(1e)

from pysnmp.hlapi import *

def print_snmp(g):
    for result in g:
        errorIndication, errorStatus, errorIndex, varBinds = result
        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(varBind)
                print(' = '.join([x.prettyPrint() for x in varBind]))

g = getCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

print_snmp(g)

n = nextCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
    lexicographicMode=False)

print_snmp(n)
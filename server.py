#coding:utf-8
from pymodbus.server.sync import StartTcpServer
from pymodbus.server.sync import StartUdpServer
from pymodbus.server.sync import StartSerialServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer
import logging
import argparse
import sys
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-server_ip', action='store', dest='server_ip', type=str, help='Input the ip address of modbus server')
    parser.add_argument('-server_port', action='store', dest='server_port', type=int, help='Input the port of modbus server')
    arg = parser.parse_args()
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    store = ModbusSlaveContext(
        di = ModbusSequentialDataBlock(0, [17]*100),
        co = ModbusSequentialDataBlock(0, [17]*100),
        hr = ModbusSequentialDataBlock(0, [17]*100),
        ir = ModbusSequentialDataBlock(0, [17]*100))
    context = ModbusServerContext(slaves=store, single=True)
    identity = ModbusDeviceIdentification()
    identity.VendorName  = 'Pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
    identity.ProductName = 'Pymodbus Server'
    identity.ModelName   = 'Pymodbus Server'
    identity.MajorMinorRevision = '1.0'
    StartTcpServer(context, identity=identity, address=(arg.server_ip, arg.server_port))

if __name__=='__main__':
    if (len(sys.argv)<=2):
        print 'Input -h for help'
    else:
        main()
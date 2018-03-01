#coding:utf-8
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
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
    client = ModbusClient(arg.server_ip, port=arg.server_port)
    client.connect()
    rr = client.read_coils(1, 1, unit=0x02)
    rq = client.write_coil(1, True)
    rr = client.read_coils(1,1)
    assert(rq.function_code < 0x80)    
    assert(rr.bits[0] == True)          
    rq = client.write_coils(1, [True]*8)
    rr = client.read_coils(1,8)
    assert(rq.function_code < 0x80)     
    assert(rr.bits == [True]*8)         

    rq = client.write_register(1, 10)
    rr = client.read_holding_registers(1,1)
    assert(rq.function_code < 0x80)     
    assert(rr.registers[0] == 10)       
    client.close()

if __name__=='__main__':
    if (len(sys.argv)<=2):
        print 'Input -h for help'
    else:
        main()


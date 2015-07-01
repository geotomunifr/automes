'''
Created on May 29, 2015

@author: antoine
'''
import smbus
import time


if __name__ == '__main__':
    bus = smbus.SMBus(7)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
    
    DEVICE_ADDRESS = 0x68      #7 bit address (will be left shifted to add the read write bit)
    DEVICE_REG_HOUR = 0x02
    DEVICE_REG_ALM1 = 0x07
    DEVICE_REG_CTRL = 0x0E
    DEVICE_REG_STATUS = 0x0F
    
    #Write a single register
    #bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_HOUR, 4)
    
    #ledout_values = [0x00, 0x80, 0x80, 0x80]
    #bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_ALM1, ledout_values)
    
    #bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_CTRL, 0x1D)
    
    value=bus.read_i2c_block_data(0x68,0 , 0x13)
    print(value)
    adr=0;
    for val in value:
        #print("%02X" % (val))
        print("%02X: %02X" % (adr,val))
        adr=adr+1
        
    #while True:
        #bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_STATUS, 0x88) 
        #time.sleep(2)
        #print("wake")

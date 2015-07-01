'''
Created on May 29, 2015

@author: antoine
'''
import smbus
import time


if __name__ == '__main__':
    bus = smbus.SMBus(2)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
    
    DEVICE_ADDRESS = 0x68      #7 bit address (will be left shifted to add the read write bit)
    DEVICE_REG_HOUR = 0x02
    DEVICE_REG_ALM1 = 0x07
    DEVICE_REG_CTRL = 0x0E
    DEVICE_REG_STATUS = 0x0F

    value=bus.read_i2c_block_data(DEVICE_ADDRESS,0x11 , 0x2)
    temp=(value[0]<<2)|(value[1]>>6);
    print(temp/4.0)
    #TODO Hanlde negative temperature

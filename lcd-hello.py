import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)

sleep(5)

mylcd.lcd_clear()

mylcd.lcd_display_string("How do you do?", 1)
mylcd.lcd_display_string("My poor darling?", 2)

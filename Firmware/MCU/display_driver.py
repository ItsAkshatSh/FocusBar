import busio
import displayio
import pwmio
from fourwire import FourWire
from adafruit_ili9341 import ILI9341

from config import TFT_DC, TFT_CS, TFT_SCK, TFT_MOSI, TFT_MISO ,TFT_BL

class DisplayDriver:
    def __init__(self):
        displayio.release_displays()
        
        self.spi = busio.SPI(TFT_SCK, TFT_MOSI, TFT_MISO)
        self.spi = busio.SPI(clock = TFT_SCK, MOSI = TFT_MOSI)
        
        
        display_bus = FourWire(self.spi, command=TFT_DC, chip_select=TFT_CS, reset=None, baudrate=24000000)
        
        self.display = ILI9341(display_bus, width=240, height=320, rotation=0)
        
        self.root = displayio.Group()
        self.display.root_group = self.root
        
        self._bl = pwmio.PWMOut(TFT_BL, frequency=1000, duty_cycle=0)
        self.set_brightness(80)
        
    def set_brightness(self, percent):
        pct = max(0, min(100, percent))
        self._bl.duty_cycle = int(pct / 100 * 65535)
    
    def refresh(self):
        self.display.refresh()
import spidev, time
import RPi.GPIO as GPIO

led = 18
led2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1350000

def analog_read(channel):
    r = spi.xfer2([1,(8+channel) << 4,0])
    adc_out = ((r[1]&3)<<8)+r[2]
    return adc_out

while True:
    GPIO.output(led2,GPIO.HIGH)
    reading = analog_read(1)
    voltage = reading * 2.2/1024
    print("Reading=%d\tVoltage=%f"%(reading,voltage))
    time.sleep(1)
    if reading<500:
        GPIO.output(led,GPIO.HIGH)
        print("LED ON")
    else:
        GPIO.output(led,GPIO.LOW)
        print("LED OFF")

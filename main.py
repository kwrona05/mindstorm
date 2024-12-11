from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from time import sleep

sensor = InfraredSensor()
motors = MoveTank(OUTPUT_B, OUTPUT_C)

THRESHOLD_DISTANCE = 30

try: 
    while True:
        distance = sensor.proximity

        if distance < THRESHOLD_DISTANCE:
            motors.off()
            print('Wykryto obiekt')
        else:
            motors.on(50, 50)
            print('Brak przeszkód')

        sleep(0.1)
except KeyboardInterrupt:
    motors.off()
    print('Program zatrzymany')
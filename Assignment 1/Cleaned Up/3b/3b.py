#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import *
from ev3dev2.led import *
from ev3dev2.sound import *
import threading

#   Vocal Organ
sound = Sound()

def personalityCore(motors, sensors, mode, activation):
    """
    The personality core is a function which takes a configuration of motors, ie appendages,
    sensors, an activation function, and a string denoting which personality is going to be
    loaded that is announced to the observer.

    The motors are governed (troptotaxis) by the stimulus which is modulated by an activation
    function, denoting inhibition or excitation. All of this happens in parallel
    across two execution threads, to further adhere to the biomimetic nature of
    Braitenberg's vehicles, while simultaneously eliminating explicit conditional switching
    statements by utilizing a cybernetics inspired feedback cycle that would make Norbert
    Wiener blush.

    In short, the personality core takes a "collection of organs," "how its wired," and,
    "how it fires" configuration and emerges something that looks a lot like behaviour.
    """
    threads = []
    sound.speak('Loading personality template ' + str(mode), volume=100, play_type=0)
    def motiveUnit(index):
        while True:
            motors[index].on(activation(sensors[index].ambient_light_intensity))
    t1 = threading.Thread(target=motiveUnit, args=(0,))
    t2 = threading.Thread(target=motiveUnit, args=(1,))
    threads.append(t1)
    threads.append(t2)
    sound.speak('Initializing thinking units', volume=100, play_type=0)
    t1.start()
    t2.start()
    sound.speak('Initialization complete', volume=100, play_type=0)

def main():
    # Anatomy
    #   Movement Organs
    motors = [LargeMotor(OUTPUT_A), LargeMotor(OUTPUT_B)]
    #   Sense Organs
    sensors = [ColorSensor(INPUT_1), ColorSensor(INPUT_2)]



    """
    Coward 2a
    """
    # personalityCore(motors, sensors, "Coward bot 2a", lambda x: x)                        #Working

    """
    Aggressive 2b
    Other Notes:
        - The [::-1] is equivalent of crossing the wires of the robot and the group is aware of that option.
    """
    # personalityCore(motors, sensors[::-1], "Aggressive bot 2b", lambda x:  x)             #Working


    """
    Coward 3a
    Other Notes:
        - Our group elected to cut the max speed of the movement organs in half, as we were having a hard time
        actually catching the vehicle so we could shine a light in its face to inhibit it.

        - Braitenberg claims this vehicle will come to rest infront of a light source, but there is a flaw in his logic,
        as the vehicle would require either of its sensors to be fully stimulated, resulting in full movement inhibition.
        The problem arsises due to the vehicle possing binocular vision and that light sources can end up being located
        in the midpoint between either sensor. Essentially, Braitenberg's vehicle 3a would need to possess eyestalks,
        have the ability to go fully cross eyed, or a light source would have to have a greater diameter than the pupilary
        distance of Braitenberg's 3a vehicle.

        Admittedly, this is rather pedantic but highlights a problem with discretizing a stimulus object only by its proximity
        or intensity, as in doing so, you disregard how that stimuli propogates through space and time, along with how much of
        it is potentially saturating an area.

    """
    # personalityCore(motors, sensors, "Love bot 3a", lambda x: 0.5 * (100 - x))            #Working


    """
    Explorer 3b
    Other Notes:
        - See "Other Notes" from 3a, regarding movement speed.
        - See "Other Notes" from 2b, regarding the software equivalent of crossing wires.
    """
    personalityCore(motors, sensors[::-1], "Explorer bot 3b", lambda x: 0.5 * (100 - x))    #Working
    return 0

if __name__ == "__main__":
    main()

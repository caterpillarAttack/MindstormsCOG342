function persTemp(arg1: sensors.ColorSensor, arg2: sensors.ColorSensor, mode: string, polarity: number, debug: boolean) {
    brick.showString("Status: " + mode, 1);
    // Debugging code
    if (debug) {
        control.runInParallel(function () {
            while (true) {
                arg1.light(LightIntensityMode.Ambient);
                arg2.light(LightIntensityMode.Ambient);
                brick.showPorts();
            }
        })
    }
    //Movement threads
    control.runInParallel(function () {
        while (true) {
            motors.largeA.run(arg1.light(LightIntensityMode.Ambient) * polarity, 0);
        }
    })
    control.runInParallel(function () {
        while (true) {
            motors.largeB.run(arg2.light(LightIntensityMode.Ambient) * polarity, 0);
        }
    })
    return 0;
}

// Personality matrix selection.
function main(vers = 0) {
    switch (vers) {
        case 1:
            //Vehicle 2a
            music.playSoundEffect(sounds.animalsDogWhine)
            persTemp(sensors.color1, sensors.color2, "Fearbot", 1, false);
            break

        case 2:
            //Vehicle 3a
            music.playSoundEffect(sounds.animalsDogWhine)
            persTemp(sensors.color1, sensors.color2, "Fearbot Revr", -1, false);
            break

        case 3:
            // Vehicle 2b
            music.playSoundEffect(sounds.animalsDogBark1)
            persTemp(sensors.color2, sensors.color1, "Lovebot", 1, false);
            break

        case 4:
            // Vehicle 3b
            music.playSoundEffect(sounds.animalsDogBark1)
            persTemp(sensors.color2, sensors.color1, "Lovebot Revr", -1, false);
            break

        default:
            brick.showString('Status: No Arg', 1);
            break
    }

    return 0
}
main(1);

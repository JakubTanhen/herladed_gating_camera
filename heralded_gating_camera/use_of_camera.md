# How to find camera software and how to use it?

So if one want to use the software one should go to the computer on the left side of the lab. There go to labVIEW 2018 64 bit and open project zyla v1.2 version 2

Then to turn it on:
1. Turn on program
2. Click appply
3. If the Handle is above 100 and below 150 it is okay you can click run, otherwise have to restart computer
4. Click run
5. Start sensor cooling, and you can start preview


Saving:

1. Saving Photons - binary data that saves a matrix with fit values from photon finder, collectively everyframe
2. Save frames - save .dat files normal ones are just frames from the camera, tt are matrix of photon finder for each frame
3. Save photon frames - this saves binary file where you have dat tt files in one file - didn't work for me


# Preparing setup to use
1. Turn on APD
2. Turn on camera with cooling
3. When you use laser start from ND12 on the image intensifier and then you can go down
4. Turn on power generator for image intesifier and connect orange box
5. Set voltage around 4V, you should start see something at 3.5V, don't go above 5V
6. Turn on Stanford delay generator
7. Set triggering from APD and use advanced function of holdoff to get minimum distance between pulses as 3.3us (otherwise gating module will freak out and will be opening not correctly)
8. Set the delay and width of the pulse

In our case se used 4.4V and 10 ns delay with 40ns width.


# Quick how to use SDG 
In this section one can find how I used Stanford Delay Generator that for basic usage will be enough. I recommend to go through manual
in Manuals_Datasheets_Setups directory, where one can find how to for example program this device and do automatization.

1. So in case of heralded gating, external triggering is turned on, this one can set by using arrows in trig mode area and electric signal from APD is connected to EXT TRIG
2. Then several values needs to be setted: trigger treshold should be set high enough so the reflected signal will not randomly trigger our device and advanced triggering should be turn on. Next One can set holdoff time, this will be the time for witch stanford will ignore new triggers after triggering, this way one can set minimal delay between each trigger
3. Then one should choose output from stanford (not the first one with T0, will not be able to set proper delay for impulse) in our case it is AB channel. Here one can set the max value (point B) to desired voltage (our case 5V), and can set on the same point the delay were one should set that it will be A + .... <-here will be width set by user. It is important to have this A at the beginning because this way user is setting the width of the pulse, otherwise you will be setting individually delay for both points and it can make some issues. In point A one can set level 0V as ground and the delay will be the delay added before sending signal, even if you put 0 here, non avoidable 85ns delay will be added to this signal.


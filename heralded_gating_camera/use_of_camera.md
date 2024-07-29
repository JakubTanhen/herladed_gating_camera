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


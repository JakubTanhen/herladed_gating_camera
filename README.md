# herladed_gating_camera
This repository contains all the script, data and plots made for Bachelors thesis of Jakub Lewandowski. Software in LABView to use an Intensified Camera was made by Jerzy Szuniewicz, I described here how I used this software and saved my comments. 


# About repository in general

All the code and notes are made to analize data from ICMOS camera and APDs for coincidence logic and herladed gating.
The structure of this repository is made in way:

1. codes
Inside one can find all the python scripts I wrote. For all codes descriptions look for description in section Heralded Gating or Coincidence logic.
There is no labVIEW code to use camera and coincidence logic but there will be descriptions and paths to find them on computers in laboratory for both of them in their repositories.

2. Manuals, datasheets and setups schemes
Inside one can find all the datasheets and manuals for used electronical components. Additionally one can find here png files of setup used for this project.

Presonally I really recomend going throught manual of Stanford Delay Generator. It is very powerfull device that you can work via python code. It will be good advancment to look for delays by working with it automatically.

3. Heralded gating camera
Here one can find file with my comments how to use the camera, where find labVIEW codes for using the camera and my path how I was looking for delay and more important - What mistakes I made and problems I encountered and how it was solved.

Scheme of the setup that all those comments are about looks like this:

![Pierwszy obrazek](Manuals, Datasheets, Setups\scheme_heralded.png)

More of that there is directory "PLOTS" with the crucial plots made with Histograms_of_counts and Plotting_accumulated_events. There was a lot of measurements done with different versions of setup, but here to make all the repository cleaner is added only latest figures.

4. Coincidence logic
Here one can find file with my comments how to use coincidence logic setup, where one can find labVIEW codes and how to interperte it.

Scheme of the setup that in this directory is about looks like this:

![Pierwszy obrazek](Manuals, Datasheets, Setups\Coincidence-Scheme.png)

As I didn't figure out how to read files saved by this program I saved screenshots of the program for crucial configuration and for different setups. 

5. ND filters characterization
Characterization of different ND filters was done in the laboratory at 3rd floor. 
For this experiment Mira laser in CW mode was used at 810nm. Half of this power was put on the power meter that showed 0.5uW, and then 0.25 of inicial power was sent into the ND filter and intensity was captured on the camera. Then to get values of attenuation the value of intensity after the filter was devided by value of intensity without any filter. As for no filter measurement the exposure time have to be small and for higher ND bigger we had to do measurement as stairs. 
Example:
We want to get attenuation of ND3:
 
a. Calculate coefficient for going from ND1 to ND0 (no attenuation) for exposure 0.001
b. Calculate coefficient for ND1 and going from exposure 0.01 to 0.001
c. Calculate coefficient for going from ND3 to ND1 for exposure 0.01
d. Multiply all the coefficients together
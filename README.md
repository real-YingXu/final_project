# final_project

# project showcase


# project instruction

For this project, we mainly use four components:
1. QTPY 2040 for main controlling (controlling speaker, receiving users' press/release feedback from Neotrellis, sending data to Pico4ML for LCD display)
![80ab10b70a9447a0f1a1582951cff5e](https://user-images.githubusercontent.com/114200453/205554661-9bcd5967-a685-4f00-b26a-81e221a2b419.jpg)
2. Neotrellis Keypad for user interaction
![7488a3e7cad00aaf71475441a50a5d3](https://user-images.githubusercontent.com/114200453/205554711-53b2792c-b613-4fd8-928a-2f4bef98ae39.jpg)
3. Pico4ML (communicating with QTPY 2040 with UART, receiving user feedback and displaying current stage on LCD)
![e67e6e920a570e3ee0892871c5ad916](https://user-images.githubusercontent.com/114200453/205554769-cc1fe12c-257b-42be-95f1-6ad6bd800a8f.jpg)
4. Speaker for .wav/.mps music playing
![87bade31b6854a461e84a0713d36958](https://user-images.githubusercontent.com/114200453/209963773-e5f2d20b-5e1b-4e8b-8ba1-9d69e359d704.png)

System diagram:
![be46a745f1526035cd1deeb1c4a80b3](https://user-images.githubusercontent.com/114200453/209963142-13411307-4ea3-4ca5-8f71-a1c160d71a4a.png)

## Circuit Diagram/Building
We firstly assembled all components, which includes Pico4ML, QTPY 2040, Stemma Speaker driver, 4 ohm 3W speaker, low-pass filter composed by 330 ohm resistor and 10pF capacitor, 3.3uF capacitor for short circuit protection, and variable resistor for volume controlling, on the breadboard and tested the functionality:
![da9e2b928ca7ea0f4064bbe81ae3c1d](https://user-images.githubusercontent.com/114200453/210047345-1286b7ac-e561-413a-bc32-c845b1d60a0d.jpg)

The soldered circuit is shown below:
![a5d0832aebc9445200d81fd2fb5c9c4](https://user-images.githubusercontent.com/114200453/210046908-de51b672-6483-445e-8416-b3445e89330f.jpg)


## Software

This program is mainly written with C and circuitpython, where C is controlling the UART communication between the PICO4ML and qtpy rp2040, and the circuit python realized the functionality of the launchpad (receiving users' pressing data and controlling speaker) which is loaded on the qtpy rp2040. The detailed explaination of code will be shown in the next section.

## Soldering and case assambling 

We assambed all component in [adafruit Neotrellis case](https://www.adafruit.com/product/4372), and we use four Neotrellis board [soldered together](https://learn.adafruit.com/adafruit-neotrellis/tiling). All components shown in circuit building section are placed at the back of adafruit Neotrellis case.
![0a6b3f3f711cae549443b092d9360e1](https://user-images.githubusercontent.com/114200453/209964686-498c02bd-e179-4ea4-bb4c-3595ccf0aff3.jpg)


## Low-pass filter assambling detail



# project development
At first as we designed in proposal, we would like to design real time music game that will covert the analog sound signal to pitches and showing LED light on different pitches through FFT(Fast Fourier Transform). However, after talking with Professor Dalton, he recommanded us to use Adafruit Neotrellis to accomplish the goal,and we found a lot of interesting application on the Neotrellis,and we finally decided to make a real instrucment, a "launchpad", instead of a music game hardware based machine. 
For the first stage of design ,we use a 4x4 Neotrellis board to make a Whack a Mole game on it

## Stage 1 Whack a Mole
Stage1 demo is shown below: 

https://youtu.be/9epRLCVayiY

The hole was randomly generated:
![0e44561f16b1917239642e189afe396](https://user-images.githubusercontent.com/113209201/205417980-ccd6b806-9c1c-4ca9-b883-0b86a4d445ff.jpg)

If you hit it in time, it will show no light, or you may hit wrong which shows red light, and the rat will escape after 0.5 second. 
![1fb9372dd3fc49cf10cbd6e4c82d438](https://user-images.githubusercontent.com/113209201/205418051-4dfb38aa-c2ff-424c-bb64-eb0b75730781.jpg)

hit right gain +2, hit wrong gain -1, hit none gain 0 credits. 

![1591f55f30e0efb9959507cbaad0104](https://user-images.githubusercontent.com/113209201/205418071-c22ed010-0436-4fa4-b551-a5c84b25396e.png)

after you got below 0 score, game over!
![b1dd96557909350e81a502d35c14e64](https://user-images.githubusercontent.com/113209201/205418063-43d84f5d-1f88-475b-adac-9487aaf1e8e9.jpg)
## LCD on Pico4ML display:

we will show the credits on LCD screen which will read the data from RP2040 through PIO in/out. The "hello-world" code for LCD enable is shown [here](https://github.com/MaxMa6150/finalproject.demo/blob/main/hello_LCD.c). 

![gswto-8gi1d](https://user-images.githubusercontent.com/113209201/205536461-e9dffa7d-6352-4bbb-873e-25df8729c929.gif)

Later, we will use the LCD display to record the score of Whack a Mole and display the patterns in the 4 steps drumer. The connection between Pico4ML with LCD and QT PY 2040 is needed.

### code

The code for the code for whack-a-mole mode is in first half of [code.py](https://github.com/MaxMa6150/finalproject.demo/blob/main/code.py).

### design

![636b7ca723a340c71f5bbcdf99d054b](https://user-images.githubusercontent.com/114200453/205553588-4998bc56-a30c-4892-9ede-2b20ec399142.jpg)


### troubleshooting

1. We use the  [neotrellis_simpletest.py](https://github.com/adafruit/Adafruit_CircuitPython_NeoTrellis/blob/main/examples/neotrellis_simpletest.py) 
Since the cable is not available, we solder the cable with copper pins. 
![1551d4fc2dba9cf7454fcc54bca023e](https://user-images.githubusercontent.com/113209201/205519974-c958b217-2fb5-4a26-ac36-9b393b230299.jpg)

2. Inspired by anothering group in demo day, we figured out that Pico4ML with LCD display could be connected with QT PY 2040 with UART with Tx/RX port. The basic logic is: when QT PY 2040 receive the users action, it can transport data to Pico4ML by TX writing port. By receiving data from RX port, Pico4ML could display some information on LCD screen with the library/code explained above. The design and system diagram is shown below:
![a33de4dd40d9f26efe16ebe6f541f0e](https://user-images.githubusercontent.com/114200453/205554246-17c9fd91-0dd5-495f-bbae-505ebc2ae730.jpg)
![4952cf835d45d4de3d077f0bec4ef9a](https://user-images.githubusercontent.com/113209201/205527555-4c39911b-fb37-4d23-89e1-d4f304852c9b.jpg)
We can use uart with/without pio. The code we edited is shown [here](https://github.com/MaxMa6150/finalproject.demo/tree/main/References%20(Uart%20connection)). We finally used PIO module in UART communication in our outlast design. In final design, QT PY 2040 will send data to Pico4ML when users select a specific mode, launchpad mode or sequencer mode, and the related information will be displayed on Pico4ML LCD. UART communication is also impleted in sequencer mode. The detailed explaination will be shown in Stage 3.


## Stage 2 4-step drumer
Stage 2 demo is shown below:

https://youtu.be/yeAbvyMj_us

The 4 steps sequencer:

we use 4/4 time signature. 

![10fc630b4f2c8406bac2706b8bfcd4b](https://user-images.githubusercontent.com/113209201/205418094-1c88b3c4-5eb0-494a-baac-6569413cd4b1.jpg)

The drums are assigned with different color, and each button on y axis represents a quarter of a period. You can produce different combination of drums by pressing down those drum button and create drum beats.

![bd59270a8f012a40c5f49dafbe0900b](https://user-images.githubusercontent.com/113209201/205418163-4cc14d23-2ab0-4c8f-b9df-3c60070a3c02.jpg)

### code

The code for the code for 4-step drumer mode is in second half of [code.py](https://github.com/MaxMa6150/finalproject.demo/blob/main/code.py).




### trouble shooting:

1. the original code we used have the audioio module which didn't implement on qtpy2040, so we use audiopwmio instead and it has a lower resolution of audio out.

## Stage 3 8x8 8-Step drumer
After we get used to Neotrellis 4x4, we decided to solider four board to make it a 8x8 board, and we will realize a 8 step drumer on that with sample plaing. 

###Touble shooting
In the original code, to make the drums to play at the same time, we use a mixer to play music in different channels. However, the sound samples in mixer are strictly required which means we may not use the sound files which is in different format, so we can only use the 16bit 2 channel 21600 sample rate WAV files instead of a MP3 files which we used in launchpad mode. 


## Stage 4 8x8 Launchpad with color functions
```
    A = False
    B = False

    IN = input("Sequencer: 1 ; Launchpad : 2  ;  1 or 2 ?:")
    if int(IN) == 1:
        uart.write(bytes([0x53]))
        for y in range(8):
            for x in range(8):
                trellis.set_callback(x,y,blink)
        A = True
    elif int(IN) == 2:
        uart.write(bytes([0x4c]))
        for y in range(8):
            for x in range(8):
                trellis.set_callback(x,y,blink2)
        B = True
```
To make the user to choose which mode they would like to play, we use a simple python input to realize that function. In this way, the user could choose the mode they want to play by interacting with console.

Then we made a number of light function which will produce different light effect when the button is pressed:
```
def cross(x,y,color):
    trellis.color(x,y,color)
    trellis.color(x,y,OFF)
    if x == 0 :
        if y == 0:
            trellis.color(x,y+1,color)
            trellis.color(x+1,y,color)
            trellis.color(x,y+1,OFF)
            trellis.color(x+1,y,OFF)
        elif y == 7:
            trellis.color(x,y-1,color)
            trellis.color(x+1,y,color)
            trellis.color(x,y-1,OFF)
            trellis.color(x+1,y,OFF)
        elif y in range(1,7):
            trellis.color(x,y+1,color)
            trellis.color(x,y-1,color)
            trellis.color(x+1,y,color)
            trellis.color(x,y+1,OFF)
            trellis.color(x,y-1,OFF)
            trellis.color(x+1,y,OFF)
    elif x == 7:
        if y == 0:
            trellis.color(x,y+1,color)
            trellis.color(x-1,y,color)
            trellis.color(x,y+1,OFF)
            trellis.color(x-1,y,OFF)
        elif y == 7:
            trellis.color(x,y-1,color)
            trellis.color(x-1,y,color)
            trellis.color(x,y-1,OFF)
            trellis.color(x-1,y,OFF)
        elif y in range(1,7):
            trellis.color(x,y+1,color)
            trellis.color(x,y-1,color)
            trellis.color(x-1,y,color)
            trellis.color(x,y+1,OFF)
            trellis.color(x,y-1,OFF)
            trellis.color(x-1,y,OFF)

    elif y == 0 and x in range(1,7):
        trellis.color(x,y+1,color)
        trellis.color(x+1,y,color)
        trellis.color(x-1,y,color)
        trellis.color(x,y+1,OFF)
        trellis.color(x+1,y,OFF)
        trellis.color(x-1,y,OFF)
    elif y == 7 and x in range(1,7):
        trellis.color(x,y-1,color)
        trellis.color(x+1,y,color)
        trellis.color(x-1,y,color)
        trellis.color(x,y-1,OFF)
        trellis.color(x+1,y,OFF)
        trellis.color(x-1,y,OFF)

    else:
        trellis.color(x,y+1,color)
        trellis.color(x,y-1,color)
        trellis.color(x+1,y,color)
        trellis.color(x-1,y,color)
        trellis.color(x,y+1,OFF)
        trellis.color(x,y-1,OFF)
        trellis.color(x+1,y,OFF)
        trellis.color(x-1,y,OFF)
```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_7.gif?raw=true)

```
def rainbow(x,y,color):
    for a in range(8):
        trellis.color(a,a,colorwheel(4*a*a))
        trellis.color(a,7-a,colorwheel(4*a*a))
    for a in range(8):
        trellis.color(a,a,OFF)
        trellis.color(a,7-a,OFF)

```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_4.gif?raw=true)


```

def block(x,y,color):
    if x in range(4) and y in range(4):
        for x in range(4):
            for y in range(4):
                trellis.color(x,y,colorwheel(4*x*y))
    if x in range(4,8) and y in range(4):
        for x in range(4,8):
            for y in range(4):
                trellis.color(x,y,colorwheel(4*x*y))
    if x in range(4) and y in range(4,8):
        for x in range(4):
            for y in range(4,8):
                trellis.color(x,y,colorwheel(4*x*y))
    if x in range(4,8) and y in range(4,8):
        for x in range(4,8):
            for y in range(4,8):
                trellis.color(x,y,colorwheel(4*x*y))

    for y in range(8):
        for x in range(8):
            trellis.color(x,y,OFF)
```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_3.gif?raw=true)
```
def waterx(x,y,color):
    for x in range(8):
        trellis.color(x,0,color)
        trellis.color(x,1,color)
        trellis.color(x,2,color)
        trellis.color(x,3,color)
        trellis.color(x,4,color)
        trellis.color(x,5,color)
        trellis.color(x,6,color)
        trellis.color(x,7,color)

    for x in range(7,-1,-1):
        trellis.color(x,0,OFF)
        trellis.color(x,1,OFF)
        trellis.color(x,2,OFF)
        trellis.color(x,3,OFF)
        trellis.color(x,4,OFF)
        trellis.color(x,5,OFF)
        trellis.color(x,6,OFF)
        trellis.color(x,7,OFF)

def watery(x,y,color):
    for y in range(8):
        trellis.color(0,y,color)
        trellis.color(1,y,color)
        trellis.color(2,y,color)
        trellis.color(3,y,color)
        trellis.color(4,y,color)
        trellis.color(5,y,color)
        trellis.color(6,y,color)
        trellis.color(7,y,color)

    for y in range(7,-1,-1):
        trellis.color(0,y,OFF)
        trellis.color(1,y,OFF)
        trellis.color(2,y,OFF)
        trellis.color(3,y,OFF)
        trellis.color(4,y,OFF)
        trellis.color(5,y,OFF)
        trellis.color(6,y,OFF)
        trellis.color(7,y,OFF)
```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_1.gif?raw=true)
```
def bigcross(x,y,color):
    for a in range(8):
        trellis.color(x,a,color)


    for b in range(8):
        trellis.color(b,y,color)

    for a in range(8):
        trellis.color(x,a,OFF)


    for b in range(8):
        trellis.color(b,y,OFF)
```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_6.gif?raw=true)

```

def spin(x,y,color):
    a = 1
    b = 1
    while a <= 5:
        for i in range(a):
            if y < 0 or y > 7:
                break
            x = x+b
            if x >= 0 and x <= 7:
                trellis.color(x,y,color)
                trellis.color(x-b,y,OFF)

            else:
                x = x-b
                break
        for j in range(a):
            if x < 0 or x > 7:
                break
            y = y+b
            if y <= 7 and y >= 0:
                trellis.color(x,y,color)
                trellis.color(x,y-b,OFF)
            else:
                y = y-b
                break
        a += 1
        b *= -1
    trellis.color(x,y,OFF)
```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_5.gif?raw=true)
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_5_2.gif?raw=true)
```


def love(x,y,color):
    a=0
    b=0
    trellis.color(0+a,2+b,color)
    trellis.color(0+a,3+b,color)
    trellis.color(1+a,0+b,color)
    trellis.color(2+a,0+b,color)
    trellis.color(3+a,1+b,color)
    trellis.color(4+a,0+b,color)
    trellis.color(5+a,0+b,color)
    trellis.color(6+a,1+b,color)
    trellis.color(6+a,2+b,color)
    trellis.color(6+a,3+b,color)
    trellis.color(1+a,4+b,color)
    trellis.color(2+a,5+b,color)
    trellis.color(3+a,6+b,color)
    trellis.color(4+a,5+b,color)
    trellis.color(5+a,4+b,color)
    trellis.color(0+a,1+b,color)
    time.sleep(0.5)
    trellis.color(0+a,2+b,OFF)
    trellis.color(0+a,3+b,OFF)
    trellis.color(1+a,0+b,OFF)
    trellis.color(2+a,0+b,OFF)
    trellis.color(3+a,1+b,OFF)
    trellis.color(4+a,0+b,OFF)
    trellis.color(5+a,0+b,OFF)
    trellis.color(6+a,1+b,OFF)
    trellis.color(6+a,2+b,OFF)
    trellis.color(6+a,3+b,OFF)
    trellis.color(1+a,4+b,OFF)
    trellis.color(2+a,5+b,OFF)
    trellis.color(3+a,6+b,OFF)
    trellis.color(4+a,5+b,OFF)
    trellis.color(5+a,4+b,OFF)
    trellis.color(0+a,1+b,OFF)
```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_2.gif?raw=true)
```
def loveloop(x,y):
    i=0
    while True:
        if i < 255:
            trellis.color(0,2,colorwheel(i))
            trellis.color(0,3,colorwheel(i))
            trellis.color(1,0,colorwheel(i))
            trellis.color(2,0,colorwheel(i))
            trellis.color(3,1,colorwheel(i))
            trellis.color(4,0,colorwheel(i))
            trellis.color(5,0,colorwheel(i))
            trellis.color(6,1,colorwheel(i))
            trellis.color(6,2,colorwheel(i))
            trellis.color(6,3,colorwheel(i))
            trellis.color(1,4,colorwheel(i))
            trellis.color(2,5,colorwheel(i))
            trellis.color(3,6,colorwheel(i))
            trellis.color(4,5,colorwheel(i))
            trellis.color(5,4,colorwheel(i))
            trellis.color(0,1,colorwheel(i))
            i += 1
        elif i == 255:
            while (i>0):
                trellis.color(0,2,colorwheel(i))
                trellis.color(0,3,colorwheel(i))
                trellis.color(1,0,colorwheel(i))
                trellis.color(2,0,colorwheel(i))
                trellis.color(3,1,colorwheel(i))
                trellis.color(4,0,colorwheel(i))
                trellis.color(5,0,colorwheel(i))
                trellis.color(6,1,colorwheel(i))
                trellis.color(6,2,colorwheel(i))
                trellis.color(6,3,colorwheel(i))
                trellis.color(1,4,colorwheel(i))
                trellis.color(2,5,colorwheel(i))
                trellis.color(3,6,colorwheel(i))
                trellis.color(4,5,colorwheel(i))
                trellis.color(5,4,colorwheel(i))
                trellis.color(0,1,colorwheel(i))
                i -= 1

```
end
![](https://github.com/MaxMa6150/final_project/blob/main/light/end.gif?raw=true)
```

def cloud(x,y,color):
    for y in range(8):
        for x in range(8):
            trellis.color(x,y,colorwheel(4*x*y))
    for y in range(8):
        for x in range(8):
            trellis.color(x,y,OFF)
```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_8.gif?raw=true)
```

def cloud_edit(x,y,color):
i = 32
if i < 64:
if x == 4 and y == 4:
    for b in range(y,y+4,1):
        for a in range(x,x+4,1):
            rinbowgrab = color
            #trellis.color(a,b-1,OFF)
            rinbowgrab = (rinbowgrab[0],rinbowgrab[1]+4*i,rinbowgrab[2]+8*i)
            trellis.color(a,b,rinbowgrab)
            i = i+1
    for b in range(y,y+4,1):
        for a in range(x,x+4,1):
            trellis.color(a,b,OFF)
if x == 3 and y == 3:
    for b in range(y,y-4,-1):
        for a in range(x,x-4,-1):
            rinbowgrab = color
            rinbowgrab = (rinbowgrab[0],rinbowgrab[1]+4*i,rinbowgrab[2]+8*i)
            trellis.color(a,b,rinbowgrab)
            i = i+1
    for b in range(y,y-4,-1):
        for a in range(x,x-4,-1):
            trellis.color(a,b,OFF)
if x == 3 and y == 4:
    for b in range(y,y+4,1):
        for a in range(x,x-4,-1):
            rinbowgrab = color
            rinbowgrab = (rinbowgrab[0],rinbowgrab[1]+4*i,rinbowgrab[2]+8*i)
            trellis.color(a,b,rinbowgrab)
    for b in range(y,y+4,1):
        for a in range(x,x-4,-1):
            trellis.color(a,b,OFF)
if x == 4 and y == 3:
    for b in range(y,y-4,-1):
        for a in range(x,x+4,1):
            rinbowgrab = color
            rinbowgrab = (rinbowgrab[0],rinbowgrab[1]+4*i,rinbowgrab[2]+8*i)
            trellis.color(a,b,rinbowgrab)
            i = i+1
    for b in range(y,y-4,-1):
        for a in range(x,x+4,1):
            trellis.color(a,b,OFF)
else:
    love(x,y,color)
```
![](https://github.com/MaxMa6150/final_project/blob/main/light/light_9.gif?raw=true)

### Trouble shooting
During the light progarm testing, we found an issue that since the light function is playing with the music playing, the speed of music playing the the light show playing will be affected when they play together, and the user can not interact with the buttons when the light is playing. Our guess is that the I2C bus is taking too much data from the borad, and it has reach its limit transmitssion speed, so in order to speed up the I2C transmission speed, we change the I2C frequency from 0.1Mhz to 0.4Mhz, and it significantly increased the speed of light functions. 

### Final stage 
We soldering the wire to one borad, and assamble them to the case. 

###Trouble shooting:
Since we can only use the audiopwmio to drive the speaker, and we are using a audio amp for 8ohm 1w speaker, the speaker is easily overdrived,and the background noise is large. SO we need a low pass filter and voltage divider to solve the problem. 
For the voltage divider, we used a variable resistor to do the job, and for the low pass filter we use a 10 pf capacitor and  a 1k ohm resistor which will wave out the sound above 5k hz,and we also use a 3.3uf capacitor to reduce the short circuit noise produce when the switcher is on and off. 

# Reflections Pros/cons
RP2040 pros:
circuit python, large storage, RT and TX supported for board commmunciation

cons:
uncomplished python libary which didnot include audioio to play audio, low default I2C frequency

PICO4ML:

Pros: LCD display

Cons: Small storage for data so we can not improve the quality of the music output by loading larger music files. 

Neotrellis:
Pros: Easy to use and program, silicon button embedded with Neopixel LEDs

Cons: Since the Neopixel leds on the board can only be assesed one at a time with circuitpython, the delay of the LED light show is significant, and even more obvious when the audio is playing with the light functions. 

4ohm 3w Speaker
Pros: sensitive and high quality sound supported,and easy to drive with the AMPs

Cons: Since we can only use the audiopwmio to drive the speaker, and we are using a audio amp for 8ohm 1w speaker, the speaker is easily overdrived,and the background noise is large. SO we need a low pass filter and voltage divider to solve the problem. 


#Future improvements:
We will use a SD card to store the music files, so that we can store a much larger sample file groups to directly used by the board. Also, we will update the library of the ciruitpython for the Neotrellis to make the Neopixel LED control easier and faster in a more pratical way. Next, we will update the audio output drive to use audioio instead of audiopwmio to produce a better sound output quality. Finally, we will add more functionalty to the sequencer such as a speed up and down moduel for each beat using time stamp and a recording cycle which will loop the notes you played with. 

# Feature accomplisments
One of the most interesting feature we have accomplished is the 8 step sequencer playing with the audio sample. Since for a real launchpad, the sample should go along withthe drum beat to produce a basic beat fot the music production,and we produce a 8 beat drum sample which could be real time modified and redistributed to syncronized samples that will give instant feedback to the music composer. It is really exiting to realize the function of producing a drum beat. 
The second part which is really exciting is to make a LCD display based on URAT data transmission. By using PIO, the delay of the two board data transmisson is minized. Also, by using URAT to transport data, it will solve the problem that the I2C bus is loading too musch data at the same time, so it is very practical in the future study. 

# PIO explaination
# 
















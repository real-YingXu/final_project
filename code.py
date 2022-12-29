# SPDX-FileCopyrightText: 2022 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import digitalio
from adafruit_neotrellis.neotrellis import NeoTrellis
from adafruit_neotrellis.multitrellis import MultiTrellis
from rainbowio import colorwheel
import random
import audiocore
import audiopwmio
import audiobusio
import audiomp3
import audiomixer


uart = busio.UART(board.TX, board.RX, baudrate=115200)

uart.write(bytes([0x73]))



# create the i2c object for the trellis
i2c_bus = busio.I2C(board.SCL1, board.SDA1,frequency=400000)  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
trelli = [
    [NeoTrellis(i2c_bus, False, addr=0x2E), NeoTrellis(i2c_bus, False, addr=0x2F)],
    [NeoTrellis(i2c_bus, False, addr=0x32), NeoTrellis(i2c_bus, False, addr=0x30)]
    ]
# create the trellis
trellis = MultiTrellis(trelli)

# Set the brightness value (0 to 1.0)
trellis.brightness = 0.5



# some color definitions
OFF = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 192,203)
PEACH = (255,218,185)
CRIMSON = (220,20,60)
LIGHTGOLD = (250,250,210)
GOLD = (250,215,0)

COLORS = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE,WHITE,PINK,PEACH,CRIMSON,LIGHTGOLD,GOLD]
DRUM_COLOR = (CYAN,
              GREEN,
              YELLOW,
              RED)

TICKER_COLOR = WHITE

Credit = []
life = []
#create path to the folders

DRUM_FOLDER = "/sample1/"
SAMPLE_FOLDER1 = "/sample2.1/"
SAMPLE_FOLDER = "/sample2/"
ALONE1 = [SAMPLE_FOLDER1+"alone-001.wav",

          ]

ALONE = [SAMPLE_FOLDER+"alone-001.mp3",
          SAMPLE_FOLDER+"alone-002.mp3",
          SAMPLE_FOLDER+"alone-003.mp3",
          SAMPLE_FOLDER+"alone-004.mp3",
          SAMPLE_FOLDER+"alone-005.mp3",
          SAMPLE_FOLDER+"alone-006.mp3",
          SAMPLE_FOLDER+"alone-007.mp3",
          SAMPLE_FOLDER+"alone-008.mp3",
          SAMPLE_FOLDER+"alone-009.mp3",
          SAMPLE_FOLDER+"alone-010.mp3",
          SAMPLE_FOLDER+"alone-011.mp3",
          SAMPLE_FOLDER+"alone-012.mp3",
          SAMPLE_FOLDER+"alone-013.mp3",
          SAMPLE_FOLDER+"alone-014.mp3",
          SAMPLE_FOLDER+"alone-015.mp3",
          SAMPLE_FOLDER+"alone-016.mp3",]


DRUM = [DRUM_FOLDER+"01.wav",
        DRUM_FOLDER+"02.wav",
        DRUM_FOLDER+"03.wav",
        DRUM_FOLDER+"04.wav",]


tempo = 150  # Starting BPM

# You can use the accelerometer to speed/slow down tempo by tilting!
ENABLE_TILT_TEMPO = True
MIN_TEMPO = 100
MAX_TEMPO = 300


# this will be called when button events are received

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

'''
def spin(x,y,color):
    i=0
    trellis.color(x,y-1,color)
    for i in range(7):
        if a == 0 or a == 7 or b == 0 or b == 7:
            break
        a = x + i
        b = y + i
        if a == x+1:
        trellis.color(a,b,color)
'''


def rainbow(x,y,color):
    for a in range(8):
        trellis.color(a,a,colorwheel(4*a*a))
        trellis.color(a,7-a,colorwheel(4*a*a))
    for a in range(8):
        trellis.color(a,a,OFF)
        trellis.color(a,7-a,OFF)







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

def bigcross(x,y,color):
    for a in range(8):
        trellis.color(x,a,color)


    for b in range(8):
        trellis.color(b,y,color)

    for a in range(8):
        trellis.color(x,a,OFF)


    for b in range(8):
        trellis.color(b,y,OFF)



def spin_new(x,y,color):
    if x<2 or y<2 or x>5 or y>5:

        for a in range(8):
            trellis.color(x,a,color)
            trellis.color(7-x,7-a,color)

        for b in range(8):
            trellis.color(b,y,color)
            trellis.color(7-b,7-y,color)

        for a in range(8):
            trellis.color(x,a,OFF)
            trellis.color(7-x,7-a,OFF)

        for b in range(8):
            trellis.color(b,y,OFF)
            trellis.color(7-b,7-y,OFF)
    else:
        watery(x,y,color)



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



def cloud(x,y,color):
    for y in range(8):
        for x in range(8):
            trellis.color(x,y,colorwheel(4*x*y))
    for y in range(8):
        for x in range(8):
            trellis.color(x,y,OFF)


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



# Parse the first file to figure out what format its in
with open(DRUM[0], "rb") as f:
    wav = audiocore.WaveFile(f)
    print("%d channels, %d bits per sample, %d Hz sample rate " %
          (wav.channel_count, wav.bits_per_sample, wav.sample_rate))

    # Audio playback object - we'll go with either mono or stereo depending on
    # what we see in the first file
    if wav.channel_count == 1:
        audio = audiopwmio.PWMAudioOut(board.A0)
    elif wav.channel_count == 2:
        audio = audiopwmio.PWMAudioOut(board.A0)
    else:
        raise RuntimeError("Must be mono or stereo waves!")
    mixer = audiomixer.Mixer(voice_count=5,
                          sample_rate=wav.sample_rate,
                          channel_count=wav.channel_count,
                          bits_per_sample=wav.bits_per_sample,
                          samples_signed=True)
    audio.play(mixer)



def blink(xo,yo,edge):
    # turn the LED on when a rising edge is detected
    #if event.edge == NeoTrellis.EDGE_RISING:
        #trellis.color[event.number] = BLUE
    # turn the LED off when a falling edge is detected
    #elif event.edge == NeoTrellis.EDGE_FALLING:
        #trellis.color[event.number] = OFF
    #data = open(VOICES[xo+yo], "rb")
    #color=random.choice(COLORS)

    #wav = audiocore.WaveFile(data)
    #mp3 = audiomp3.MP3Decoder(data)

    if yo in range(4):
        if edge == NeoTrellis.EDGE_RISING:
            #a.play(wav)
            #bigcorss(xo,yo,color)

            beatset[yo][xo] = not beatset[yo][xo] # enable the voice
            if beatset[yo][xo]:
                color = DRUM_COLOR[yo]
            else:
                color = 0
            trellis.color(xo,yo,color)

    if xo == 0 and yo == 4:
        if edge == NeoTrellis.EDGE_RISING:
            data = open(ALONE1[0], "rb")
            wav = audiocore.WaveFile(data)
            mixer.voice[4].play(wav)
            trellis.color(xo,yo,CYAN)
            #audio.play(mp3)
            #waterx(x,y,color)





pattern=[waterx,
        cloud,
        block,
        spin_new,
        rainbow,
        love,
        bigcross]


def blink2(xo,yo,edge):
    color=random.choice(COLORS)

    if edge == NeoTrellis.EDGE_RISING:
        data = open(ALONE[4*(xo//2)+(yo//2)], "rb")
        mp3 = audiomp3.MP3Decoder(data)
        audio.play(mp3)



        if xo == 7 and yo == 7:
            uart.write(bytes([0x45]))
            loveloop(xo,yo)
        elif xo in range(0,2) and yo in range(0,2):
            for x in range(8):
                cross(x,yo, colorwheel(16*yo+16*x))
        elif xo in range (6,8) and yo in range(0,2):
            for x in range(7,-1,-1):
                cross(x, yo, colorwheel(8*x+8*yo))
        elif xo in range(3,5) and yo in range(3,5):
            cloud_edit(xo,yo,color)

        elif xo in range(2,6) and yo in range(2,6):
            spin(xo,yo,colorwheel(4*xo+4*yo))

        elif yo in range(1,7,1) and xo in range(1,7,1) :
           bigcross(xo,yo,CRIMSON)

        else:
            a = random.randrange(0,7,1)
            pattern[a](xo,yo,color)









def blink3(xo,yo,edge):
    # turn the LED on when a rising edge is detected
    #if event.edge == NeoTrellis.EDGE_RISING:
        #trellis.pixels[event.number] = BLUE
    # turn the LED off when a falling edge is detected
    #elif event.edge == NeoTrellis.EDGE_FALLING:
        #trellis.pixels[event.number] = OFF

    if edge == NeoTrellis.EDGE_RISING:
        trellis.color(x,v,OFF)


BIT1 = [0x31,0x32,0x33,0x34]

samples = []
# Read the 4 wave files, convert to stereo samples, and store
# (show load status on neopixels and play audio once loaded too!)
for v in range(4):
    uart.write(bytes([BIT1[v]]))
    trellis.color(0,v,DRUM_COLOR[v])
    wave_file = open(DRUM[v], "rb")
    # OK we managed to open the wave OK
    for x in range(1,4):
        trellis.color(x,v,DRUM_COLOR[v])
    sample = audiocore.WaveFile(wave_file)
    # debug play back on load!
    mixer.play(sample, voice=0)
    for x in range(4, 8):
        trellis.color(x, v,DRUM_COLOR[v])
    while mixer.playing:
        pass
    #trellis.color(7,v,DRUM_COLOR[v])

    time.sleep(0.3)
    samples.append(sample)


color=random.choice([RED, YELLOW, GREEN, CYAN, BLUE, PURPLE])
for y in range(8):
    for x in range(8):
    # activate rising edge events on all keys
        trellis.activate_key(x, y, NeoTrellis.EDGE_RISING)
        # activate falling edge events on all keys
        trellis.activate_key(x, y, NeoTrellis.EDGE_FALLING)
        # set all keys to trigger the blink callback
        #trellis.set_callback(x,y,blink)


        # cycle the LEDs on startup

        trellis.color(x,y,color)
        time.sleep(0.02)

uart.write(bytes([0x35]))
for y in range(8):
    for x in range(8):
        trellis.color(x, y, OFF)
        time.sleep(0.02)

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

start = time.time()

speaker_enable = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
speaker_enable.switch_to_output(value=True)


#a = audiopwmio.PWMAudioOut(board.A0)
#a = audiobusio.I2SOut(board.SDA, board.SCL, board.A0)



#trellis.color(5,5,CYAN)

# Our global state
current_step = 7 # we actually start on the last step since we increment first
# the state of the sequencer
beatset = [[False] * 8, [False] * 8, [False] * 8, [False] * 8]
# currently pressed buttons
Drum = ["a","b","c","d"]
BIT = [0x41,0x42,0x43,0x44]
Num = [0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37]
while A:

    stamp = time.monotonic()

    # redraw the last step to remove the ticker bar (e.g. 'normal' view)
    for y in range(4):
        color = 0
        if beatset[y][current_step]:
            color = DRUM_COLOR[y]
        trellis.color(current_step,y,color)

    # next beat!
    current_step = (current_step + 1) % 8

    # draw the vertical ticker bar, with selected voices highlighted
    for y in range(4):
        if beatset[y][current_step]:
            uart.write(bytes([BIT[y]]))
            uart.write(bytes([Num[current_step]]))
            r, g, b = DRUM_COLOR[y]
            color = (r//2, g//2, b//2)  # this voice is enabled
            mixer.play(samples[y], voice=y)
            mixer.play(samples[y], voice=y)
        else:
            color = TICKER_COLOR    # no voice on
            #uart.write(bytes([0x45]))
        trellis.color(current_step,y, color)
    if current_step == 7:
        time.sleep(0.1)
        uart.write(bytes([0x45]))



    # handle button presses while we're waiting for the next tempo beat
    # also check the accelerometer if we're using it, to adjust tempo
    while time.monotonic() - stamp < 60/tempo:
        # Check for pressed buttons
        trellis.color(0,4,GOLD)
        #trellis.color(1,5,CRIMSON)

        #trellis.color(1,6,CRIMSON)

        trellis.sync()

        time.sleep(0.02)

while B:
    trellis.sync()
    time.sleep(0.02)
j = -1
while C:
    j += 2
    if j > 32:
        break
    t = time.monotonic()
    N = j % 8 #y
    M = j // 4 #x
    data = open(ALONE[4*(M//2)+(N//2)], "rb")
    trellis.color(M,N,CYAN)
    mp3 = audiomp3.MP3Decoder(data)
    audio.play(mp3)

    print(M,N,j)

    while time.monotonic - t < 6:
        pass
        #trellis.sync()

        # the trellis can only be read every 17 millisecons or so
    trellis.color(M,N,OFF)


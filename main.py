import time
import board
import digitalio
import audiomp3
import audiopwmio

# Configure GPIO pins for button, relay, and LED
button_pin = board.GP2
relay_pin = board.GP3
led_pin = board.LED

button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

relay = digitalio.DigitalInOut(relay_pin)
relay.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT

# Configure PWM audio output
audio_pin = board.GP16
audio = audiopwmio.PWMAudioOut(audio_pin)

# MP3 file to play
mp3_file = "slow.mp3"

# Function to generate beeps and toggle LED
def beep():
    relay.value = True   # Close relay
    led.value = True     # Turn on LED
    time.sleep(0.1)      # Beep duration
    relay.value = False  # Open relay
    led.value = False    # Turn off LED

# Function to play MP3 and generate beeps simultaneously
def play_mp3_and_beep():
    # Open MP3 file
    decoder = audiomp3.MP3Decoder(open(mp3_file, "rb"))
    # Start audio playback
    audio.play(decoder)
    # Generate 6 beeps simultaneously
    for _ in range(6):
        beep()
        time.sleep(0.90)    # Delay 1 second between beeps

# Main loop
while True:
    if not button.value:  # Button pressed
        play_mp3_and_beep()  # Start audio playback and beeps
        time.sleep(0.2)    # Debounce delay

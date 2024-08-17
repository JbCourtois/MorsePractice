from init_mixer import beep, pause, background


alphaToMorse = {
    ' ': "/", ',': '//', ';': '//', '.': '///', '?': '///', '!': '///',
    'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".",
    'f': "..-.", 'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-",
    'l': ".-..", 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-",
    'r': ".-.", 's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--",
    'x': "-..-", 'y': "-.--", 'z': "--..",
}


def init_transmission():
    channel_b = background.play(loops=-1)
    channel_b.set_volume(0.5)
    pause(30)


def morsecode(message):
    """
    converts text to morse code.
    prints result and calls morseaudio.
    """
    # if you enter nothing, exits method
    if not message:
        return

    # remembers characters that do not have standard morse code equivalent
    unabletoconvert = ""
    morse = ""
    for char in message.lower():
        if char in alphaToMorse:
            morse += alphaToMorse[char] + ' '
        else:
            unabletoconvert += char
    if len(unabletoconvert) != 0:
        print("These characters are unable to be converted:\n" + ' '.join(unabletoconvert))
    morse = morse[:-1]
    print(morse)
    morseaudio(morse)


def morseaudio(morse):
    """
    plays audio conversion of morse string using inbuilt windows module.
    :param morse: morse code string.
    """
    for char in morse:
        if char == ".":
            beep(1)
        elif char == "-":
            beep(4)
        elif char == "/":
            pause(9)
        else:
            # char is blank space
            pause(6)
    pause(9)

import pyautogui
import ollama
import time
import threading
import random

model = "llama3.2"
spinning = True


# Type Function
def Type(String, wordThink, sentenceThink, paragraphThink, dismissal):
    txtToPrint = String.split(' ')
    times = [0.032, 0.035, 0.0375, 0.04]

    # Countdown
    print('You have 5 seconds to place your cursor', end='\r')
    time.sleep(1)
    print('You have 4 seconds to place your cursor', end='\r')
    time.sleep(1)
    print('You have 3 seconds to place your cursor', end='\r')
    time.sleep(1)
    print('You have 2 seconds to place your cursor', end='\r')
    time.sleep(1)
    print('You have 1 second to place your cursor', end='\r')
    time.sleep(1)

    # Printing Stuff
    i = 0
    while i < len(txtToPrint):
        intrvl = random.choice(times)
        wordSplit = list(txtToPrint[i])

        # Paragraph Wait
        if '\n' in txtToPrint[i]:
            parts = txtToPrint[i].split('\n')
            for j, part in enumerate(parts):
                if part:
                    pyautogui.typewrite(part, intrvl)
                if j < len(parts)-1:
                    pyautogui.press('enter')
                    if paragraphThink:
                        time.sleep(random.randint(20,45))
            pyautogui.typewrite(' ', 0.02)

        # Printing Normally
        else:
            pyautogui.typewrite(txtToPrint[i], intrvl)
            pyautogui.typewrite(' ', 0.02)

        # Sentence Wait
        if txtToPrint[i].endswith('.'):
            if sentenceThink:
                if random.randint(1,4) == 3:
                    time.sleep(random.randint(15,30))

        # Word Wait
        if wordThink:
            if random.randint(1, 30) == 13:
                time.sleep(random.randint(10,15))
        i += 1

    # Dissmissal Message
    if dismissal:
        pyautogui.typewrite('\n')
        pyautogui.typewrite('Done!')


# Spinner Function
def Spinner(stopEvent):
    spinState=['⠹', '⠼', '⠶','⠧','⠏', '⠛']
    i=0
    while not stopEvent.is_set():
        print(f'{spinState[i]}', end='\r')
        time.sleep(.1)
        i = (i+1)%len(spinState)
    print(' ', end='\r')

stopSpinner = threading.Event()


# Main Running Loop
while True:
    stopSpinner.clear()
    aiOrNo = input('Would you like to use AI to answer your question [Y/N]: ')
    if aiOrNo != 'Y' and aiOrNo != 'N':
        break

    # Word Think
    wordThinkYN = input('Would you like word think on? (waiting randomly between words) [Y/N]: ')
    if wordThinkYN == 'Y':
        wordThinkBool = True
    elif wordThinkYN == 'N':
        wordThinkBool = False
    else:
        break

    # Sentence Think
    sentenceThinkYN = input('Would you like sentence think on? (waiting randomly between sentences) [Y/N]: ')
    if sentenceThinkYN  == 'Y':
        sentenceThinkBool = True
    elif sentenceThinkYN  == 'N':
        sentenceThinkBool = False
    else:
        break

    # Paragraph Think
    paragraphThinkYN = input('Would you like paragraph think on? (waiting between paragraphs) [Y/N]: ')
    if paragraphThinkYN  == 'Y':
        paragraphThinkBool = True
    elif paragraphThinkYN  == 'N':
        paragraphThinkBool = False
    else:
        break

    # Dismissal Message
    dismissalYN = input('Would you like a „Done!“ when your text is done being typed? [Y/N]: ')
    if dismissalYN == 'Y':
        dissmissalBool = True
    elif dismissalYN == 'N':
        dissmissalBool = False
    else:
        break

    # DO STUFF
    #   No AI
    if aiOrNo == 'N':
        textToType = input('What text would you like typed? ')
        Type(textToType, wordThinkBool, sentenceThinkBool, paragraphThinkBool, dissmissalBool) 

    #   AI
    elif aiOrNo == 'Y':
        prompt = input('What question would you like AI to answer?: ')
        spinnerThread = threading.Thread(target=Spinner, args=(stopSpinner,))
        spinnerThread.start()
        aiAnswer = ollama.generate(model, prompt+'. Do not include any special characters such as em dashes or emojis. Do not include a salutationary nor dismissal line nor a "Here is" statement at the beginning either.').response
        stopSpinner.set()
        spinnerThread.join()
        Type(aiAnswer, wordThinkBool, sentenceThinkBool, paragraphThinkBool, dissmissalBool)
    
    print("\nDone!", end='\n\n')

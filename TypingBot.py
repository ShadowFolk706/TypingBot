import pyautogui
import ollama
import time
import random

model = "llama2"

def Type(String):
    txtToPrint = String.split(" ")
    times = [0.032, 0.035, 0.0375, 0.04]

    print("You have 5 seconds to place your cursor")
    time.sleep(1)
    print("You have 4 seconds to place your cursor")
    time.sleep(1)
    print("You have but 3 seconds to place your cursor")
    time.sleep(1)
    print("You have 2 seconds to place your cursor")
    time.sleep(1)
    print("You have 1 seconds to place your cursor")
    time.sleep(1)

    pyautogui.typewrite("·", interval=.045)
    i = 0

    def quotationMark():
        pyautogui.keyDown('Shift')
        pyautogui.press("'")
        pyautogui.keyUp('Shift')

    while i < len(txtToPrint):
        intrvl = random.choice(times)
        # intrvl = 0
        if txtToPrint[i]=='“':
            quotationMark()
        elif txtToPrint[i]=='”':
            quotationMark()
        else:
            pyautogui.typewrite(txtToPrint[i], intrvl)
        pyautogui.typewrite(" ", 0.00)
        i += 1


while True:
    aiOrNo = input("Would you like to use AI to answer this question [Y/N]: ")
    if aiOrNo == "N":
        textToType = input("What text would you like typed? ")
        Type(textToType)

    elif aiOrNo == "Y":
        prompt = input("What question would you like AI to answer?: ")
        aiAnswer = ollama.generate(model, prompt+' Do not include any special characters such as em dashes or emojis').response
        Type(aiAnswer)
    else:
        break


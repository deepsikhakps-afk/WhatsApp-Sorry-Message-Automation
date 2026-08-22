import pyautogui,time
number=input("Mobile number: ")
count=int(input("Number of messages: "))
pyautogui.hotkey("ctrl","l")
pyautogui.write("https://web.whatsapp.com/send?phone="+number)
pyautogui.press("enter"); time.sleep(8)
message="I'm sorry ❤️ Please forgive me!"
for i in range(count): pyautogui.write(message); pyautogui.press("enter")
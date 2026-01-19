from openai_client import OpenAI
import pyautogui
import time
import pyperclip


#  OPENAI CLIENT 
client = OpenAI(
    api_key="enter api key"
)


#  check last message 
def is_last_message_from_sender(chat_log, sender_name="Sachin Ranila"):
    try:
        last_line = chat_log.strip().split("\n")[-1]
        if sender_name in last_line:
            return True
        return False
    except:
        return False


# chrome / whatsapp click
pyautogui.click(1639, 1412)
time.sleep(1)

while True:
    time.sleep(5)

    # select chat
    pyautogui.moveTo(972, 202)
    pyautogui.dragTo(2213, 1278, duration=2, button='left')

    # copy
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    # remove selection
    pyautogui.click(1994, 281)

    chat_history = pyperclip.paste()
    print(chat_history)

    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Yogesh. "
                        "You speak Hindi + English. "
                        "You are from India and talk like a normal WhatsApp user. "
                        "Reply short and natural."
                    )
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # message box click
        pyautogui.click(1808, 1328)
        time.sleep(0.5)

        # paste & send
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')

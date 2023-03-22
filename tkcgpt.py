# ===================================================
# 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
# ===================================================

# =================
# package importing
# =================
import tkinter
import openai

# ==========================
# root window configurations
# ==========================
# root window
root = tkinter.Tk(screenName=None, baseName=None, className="Tk", useTk=True, sync=False, use=None)

# root window configurations
root.title("CZ1993 ChatGPT")
root.geometry("1280x640")

# ========================
# OpenAI API key inputting
# ========================
# OpenAI API key label
label_key = tkinter.Label(root, text="Key", font=("Calibri", 11))
label_key.pack(pady=5)

# OpenAI API key entry
entry_key = tkinter.Entry(root, width=60, font=("Calibri", 11))
entry_key.pack(pady=5)

# key entered function
label_key_entered = tkinter.Label(root, fg="blue", text="Key Entered", font=("Calibri", 11))

def key_entered():
    openai.api_key = entry_key.get()
    label_key_entered.pack(pady=5)

# OpenAI API key enter button
button_key = tkinter.Button(root, text="Enter Key", font=("Calibri", 11), command=lambda: key_entered())
button_key.pack(pady=5)

# =========================================
# inquiry inputting and response outputting
# =========================================
# screen to show the dialogue
# ...

# inquiry entry
entry_inquiry = tkinter.Entry(root, width=60, font=("Calibri", 11))
entry_inquiry.pack(side=tkinter.BOTTOM, pady=5)

def inquiry_entered():
    messages = []
    while True:
        inquiry = input("User: ")
        messages.append({"role": "user", "content": inquiry})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        response = completion.choices[0].message.content
        print("ChatGPT: ", response)
        messages.append({"role": "assistant", "content": response})

# inquiry enter button
button_inquiry = tkinter.Button(root, text="Enter Inquiry", font=("Calibri", 11), command=lambda: inquiry_entered())
button_inquiry.pack(side=tkinter.BOTTOM, pady=5)

root.mainloop()

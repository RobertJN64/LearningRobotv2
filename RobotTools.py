def printlog(text):
    print("<", str(text), ">")
    with open("userscripts/printlog.txt", "a") as f:
        f.write(str(text) + "\n")
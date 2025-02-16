import webbrowser, sys, pyperclip
#/Данный код нужен для того, чтоб получать ответ с консоли
#if len(sys.argv) > 1:
#address = ' '.join(sys.argv[1:])
#else:
#\
address = pyperclip.paste()
webbrowser.open('google.com/maps/place/' + address)
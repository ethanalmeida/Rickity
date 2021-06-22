import webbrowser

def rickity():
    site = 'youtube.com/watch?v=dQw4w9WgXcQ'
    visit = "http://{}".format(site)
    webbrowser.open(visit)


if __name__ == "__main__":
    rickity()

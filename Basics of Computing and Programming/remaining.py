def remainingwords(s: str):
    return "" if len(s.split(None, 1)) == 1 else s.split(None, 1)[1]
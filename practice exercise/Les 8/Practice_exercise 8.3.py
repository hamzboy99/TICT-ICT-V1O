def code(invoerstring):
    for item in invoerstring:
        rangnummer = ord(item)
        rangnummerNieuw = rangnummer + 3
        nieuweLetter = chr(rangnummerNieuw)
        print(nieuweLetter, end='')

zin = input("Code:")
code(zin)

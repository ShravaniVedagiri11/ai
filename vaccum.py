ra=input("enter status of a ")
rb=input("enter status of b ")
pos=input("enter pos of robot")
if pos=="a":
    if ra=="dirty":
        print("action=suck")
        ra="clean"
    else:
        print("action=-move to b")
        pos="b"
if pos=="b":
    if rb=="dirty":
        print("action=suck")
        rb="clean"
    else:
        print("action=-move to a")
        pos="a"

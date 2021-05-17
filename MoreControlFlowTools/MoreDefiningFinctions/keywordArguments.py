def dog(color, weight=10, height=0.5, type='alaska'):
    print(type, ' dog have ', color, ' weight ',
          weight, ' and height ', height)


dog('black')
dog('yellow', weight=5)
dog('orange', type='barge', height=1)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

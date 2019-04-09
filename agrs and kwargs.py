def myfunc(*likes,**snacks):

    if 'sweet' or 'juice' in snacks:

        print(f"I like {' and '.join(likes)} and my favourite sweet is {snacks['sweet']}")
        print(f"my favourite juice is {snacks['juice']}")
    else:
        pass
myfunc('cakes','friuts',sweet="jamun",juice='mango')
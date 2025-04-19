#peps PYTHON ENVIROMENT PROPOSAL STAMENT

def meow(n:int) -> str:
    """
    MEOW N TIMES , DOCSTRING
    
    :Param n: Number of times to meow
    :Type n: int
    :raise TypeError: If is not an int
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows:str = meow(number)
print(meows, end="")

help(meow)
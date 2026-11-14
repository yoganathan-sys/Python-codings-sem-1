def myfun(a,b):
    return a+b
print(*map(myfun,[10,20,'good'],(2,5.5,'morn')),sep='\n')

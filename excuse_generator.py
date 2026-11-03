import random 

who = ['the dog','my granma','his turtle','my bird']
what = ['eat','pissed','crushed','broked']
when = ['before the class','right in time','when I finished','during my lunch','while I was praying']

def generateExcuse():
    randomWho = random.choice(who)
    randomWhat = random.choice(what)
    randomWhen = random.choice(when)

    excuse = f'{randomWho} {randomWhat} {randomWhen}'
    return excuse

print(generateExcuse())


def parrot(voltage, state='a stiff', action='voom', type='norwegian Blue'):
    print("--This parrot woudn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("--Lovely plumage, the", type)
    print("--It's", state, "!")

parrot(voltage=1000)
parrot(voltage=1000000, action="VOOOOOOM")
parrot('a million', 'benifit of life', 'jump')
parrot('a thousand', state='pushing the daisies')

# here are some invalid functions
#parrot()                                               -- empty call
#parrot(voltage='5.0', 'dead')                          -- no keyword sepcified after keyword argument
#parrot(110, voltage='69')                              -- duplicate arguments
#parrot( actor='jhon')                                  -- no keyword argument
def esp(numE):
    numes = numE 
    return (' '*numes)

def right_justify(s):
    ao = s
    numlet = (len(ao))
    subtra = 70-numlet
    espnec = esp(subtra)
    print (str(espnec)+str(ao))
    return 

right_justify('monty')

my_dictionary = {}
all_tracks = [] 
class Track:
    def __init__(self):
        self.name = 0  
        self.eta = 0 
        self.phi = 0
        # self.z0 = 0
        # self.d0 = 0
        # self.pT = 0
for i in range(1,100):
    track = Track()
    track.eta = i
    track.phi = i*i 
    track.name = 'track {}'.format(i) 
    my_dictionary[track.name] = [track.eta, track.phi]  


matches = [] 
failures = [] 

match = False 
def match(a,b):
    if my_dictionary['track {}'.format(a)] == my_dictionary['track {}'.format(b)]: 
        #print('match')
        match = True
        matches.append(1)
    else: 
        #print('this isnt the same thing')
        match = False 
        failures.append(1)
    #if match == True: 
        #print('it was true')
    return match 

total_matches = 0 
total_failed = 0 
for i in range(1,10): 
    for j in range(1,100): 
        if match(i,j):
        #print('it was  a match')
            total_matches = total_matches + 1 
        else: 
        #print('nah m8')
            total_failed = total_failed + 1 
print('failed',total_failed,'matched',total_matches)    

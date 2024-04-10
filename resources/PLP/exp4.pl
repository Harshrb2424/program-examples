run :-
    write('Do you have HEADACHE?'),
    read(HA),
    write('Do you have TEMPERATURE?'),
    read(TP),
    write('Do you have a SORE THROAT?'),
    read(ST),
    write('Are you feeling TIRED?'),
    read(TR),
    disease(HA, TP, ST, TR).


disease(y,y,y,y):-write('You are suffering from VIRAL FEVER').
disease(y,y,y,n):-write('You are suffering from COMMON FEVER').
disease(y,y,n,y):-write('You are suffering from VIRAL FEVER').
disease(y,y,n,n):-write('You maybe OVERHOOKED').
disease(y,n,y,y):-write('You are suffering from COLD').
disease(y,n,y,n):-write('You might develop THROAT INFECTION').
disease(y,n,n,y):-write('You might have SEDENTARY for a long spell').
disease(y,n,n,n):-write('You are suffering from HEADACHE').
disease(n,y,y,y):-write('You are suffering from FEVER').
disease(n,y,y,n):-write('You are experiencing initial stages of COMMON COLD').
disease(n,y,n,y):-write('You are suffering from DEHYDRATION').
disease(n,y,n,n):-write('You are suffering from DENGU FEVER').
disease(n,n,y,y):-write('You are suffering from CHICKENGUNYA').
disease(n,n,y,n):-write('You are suffering from SORE THROAT').
disease(n,n,n,y):-write('You can relax, U are ENERVATED').
disease(n,n,n,n):-write('You are ALRIGHT').
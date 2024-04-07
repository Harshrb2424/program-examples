in_room(bananas).
in_room(chair).
in_room(monkey).

clever(monkey).
can_move(monkey,chair,bananas).
can_climb(monkey,chair).
can_reach(X,Z):-clever(X),is_close(X,Z).
is_close(X,Z):- can_climb(X,Y),under(Y,Z).
under(Y,Z):-in_room(X),in_room(Y), in_room(Z), can_move(X,Y,Z).








% Delete the element at position P (1-based index) from the list
delete(1, [_|T], T).
delete(P, [X|Y], [X|R]) :-
    P1 is P - 1,
    delete(P1, Y, R).

% Insert an element X at position N (1-based index) in the list
insert(X, 1, L, [X|L]).
insert(X, N, [H|T], [H|R]) :-
    N > 1,
    N1 is N - 1,
    insert(X, N1, T, R).
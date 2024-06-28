empties([], 0).

empties([[]|L], R) :-
    empties(L, K),
    R is K + 1.

empties([[_|_]|L], K) :-  % This clause matches non-empty sublists
    empties(L, K).

empties([X|L], K) :-
    X \= [],
    empties(L, K).

empties(L, N) :-
    findall(_, (member(X, L), X = []), L1),  % Changed X to _
    length(L1, N).
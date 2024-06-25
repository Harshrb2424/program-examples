
empties([], 0).

empties([[]|L], R) :-
    empties(L, K),
    R is K + 1.

empties([X|L], K) :-
    X \= [],
    empties(L, K).

empties(L, N) :-
    findall(X, (member(X, L), X = []), L1),
    length(L1, N).
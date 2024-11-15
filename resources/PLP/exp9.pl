% Check if an element is in the binary tree
in(X, t(_, X, _)).
in(X, t(L, _, _)) :- in(X, L).
in(X, t(_, _, R)) :- in(X, R).

% Add an element to the binary tree
add(nil, X, t(nil, X, nil)).
add(t(L, Y, R), X, t(L1, Y, R)) :-
    gt(Y, X),
    add(L, X, L1).
add(t(L, Y, R), X, t(L, Y, R1)) :-
    gt(X, Y),
    add(R, X, R1).

% Add an element to the binary tree using addroot
addroot(nil, X, t(nil, X, nil)).
addroot(t(L, Y, R), X, t(L1, X, t(L2, Y, R))) :-
    gt(Y, X),
    addroot(L, X, t(L1, X, L2)).
addroot(t(L, Y, R), X, t(t(L, Y, R1), X, R2)) :-
    gt(X, Y),
    addroot(R, X, t(R1, X, R2)).

% Display the binary tree
show(Tree) :-
    show2(Tree, 0).
show2(nil, _).
show2(t(Left, X, Right), Indent) :-
    Ind2 is Indent + 2,
    show2(Right, Ind2),
    tab(Indent), write(X), nl,
    show2(Left, Ind2).

% Comparison predicate for ordering elements (replace with appropriate comparison for your data type)
gt(X, Y) :- X > Y.

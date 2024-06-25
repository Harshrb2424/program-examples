member_nested(X, [X|_]).
member_nested(X, [Head|Tail]) :-
    (   is_list(Head),
        member_nested(X, Head)
    ;   member_nested(X, Tail)
    ).

memCount(_, [], 0).

% Recursive case: AList is the head of the list
memCount(AList, [AList|Tail], Count) :-
    memCount(AList, Tail, TailCount),
    Count is TailCount + 1.

memCount(AList, [Head|Tail], Count) :-
    AList \= Head,
    is_list(Head),
    member_nested(AList, Head),
    memCount(AList, Tail, TailCount),
    Count is TailCount + 1.

memCount(AList, [Head|Tail], Count) :-
    AList \= Head,
    (   \+ is_list(Head)
    ;   \+ member_nested(AList, Head)
    ),
    memCount(AList, Tail, Count).

:- initialization(main).
main :-
    memCount(a, [b, a], N1),
    write('N1 = '), write(N1), nl,
    memCount(a, [b, [a, a, [a], c], a], N2),
    write('N2 = '), write(N2), nl,
    memCount([a], [b, [a, a, [a], c], a], N3),
    write('N3 = '), write(N3), nl,
    halt.

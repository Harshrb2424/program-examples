not(Goal) :-
    \+ call(Goal).

prefix([], _).
prefix([H|T1], [H|T2]) :-
    prefix(T1, T2).

memCount(_, [], 0).

memCount(AList, BList, Count) :-
    prefix(AList, BList),  % AList is a prefix of BList
    append(AList, Rest, BList),  % Remove the prefix AList from BList to get Rest
    memCount(AList, Rest, CountRest),
    Count is CountRest + 1.

memCount(AList, [_|Tail], Count) :-
    not(prefix(AList, [_|Tail])),  % Ensure AList is not a prefix of the current list
    memCount(AList, Tail, Count).
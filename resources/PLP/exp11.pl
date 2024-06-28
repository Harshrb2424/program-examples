% Predicate to check if an element is a member of a list, including nested lists
member_nested(X, [X|_]) :-
    atomic(X).  % Ensure X is an atomic value

member_nested(X, [Head|_]) :-
    is_list(Head),  % Check if Head is a list
    member_nested(X, Head).

member_nested(X, [_|Tail]) :-
    member_nested(X, Tail).

% Predicate to count occurrences of AList within BList
memCount(_, [], 0).

memCount(AList, [Head|Tail], Count) :-
    is_list(Head),
    memCount(AList, Head, Count1),  % Recursively count in Head
    memCount(AList, Tail, Count2),  % Recursively count in Tail
    Count is Count1 + Count2.

memCount(AList, [Head|Tail], Count) :-
    AList = Head,  % AList matches Head
    memCount(AList, Tail, TailCount),
    Count is TailCount + 1.

memCount(AList, [_|Tail], Count) :-
    memCount(AList, Tail, Count).  % Continue counting in Tail

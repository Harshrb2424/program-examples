# List of Programs

## 1. Write simple facts for the following:

- A. Ram likes mango.
- B. Seema is a girl.
- C. Bill likes Cindy.
- D. Rose is red.
- E. John owns gold.

### Source Code: `ex1.pl` [view file](./exp1.pl)

```pl
likes(ram,mang0).
girl(seema).
red(rose).
likes(bill,candy).
owns(john,gold).
```

### Output:

```bash
ᬀ% c:/users/harsh/onedrive/documents/prolog/ex1 compiled 0.00 sec, -3 clauses
?- likes(ram, What).
What = mango.

?- likes(Who, candy).
Who = bill.

?- red(What).
What = rose.

?- owns(Who, What).
Who = john,
What = gold.
```

## 2. Write predicates:

- One converts centigrade temperatures to Fahrenheit.
- The other checks if a temperature is below freezing.

### Source Code: `ex2.pl` [view file](./exp2.pl)

```pl
c_to_f(C,F):-
   F is C*9/5+32.
frezzing(F):-
   F=<32.
```

### Output:

```bash
Ȁ% c:/users/harsh/onedrive/documents/prolog/exp2 compiled 0.00 sec, -1 clauses
?- c_to_f(100,X).
X = 212.

?- frezzing(15).
true.

?- c_to_f(32,X).
X = 89.6.
```

## 3. Write a program to solve the Monkey Banana problem.
magine a room containing a monkey, chair and some bananas. That have been hanged from the center of ceiling. If the monkey is clever enough he can reach the bananas by placing the chair directly below the bananas and climb on the chair.
### Source Code: `ex3.pl` [view file](./exp3.pl)

```pl
in_room(bananas).
in_room(chair).
in_room(monkey).

clever(monkey).
can_move(monkey,chair,bananas).
can_climb(monkey,chair).
can_reach(X,Z):-clever(X),is_close(X,Z).
is_close(X,Z):- can_climb(X,Y),under(Y,Z).
under(Y,Z):-in_room(X),in_room(Y), in_room(Z), can_move(X,Y,Z).
```

### Output:

```bash
% c:/users/harsh/onedrive/documents/prolog/exp3 compiled 0.00 sec, -3 clauses
?- can_reach(Who, What).
Who = monkey,
What = bananas .

?- can_reach(monkey, bananas).
true.

?- can_reach(monkey, apple).
false.

?- clever(Who).
Who = monkey.

?- can_climb(X,Y).
X = monkey,
Y = chair.
```

## 4. Write a program in Turbo Prolog for medical diagnosis and show the advantages and disadvantages of green and red cuts.
### ALGORITHM
1. Start
2. First the knowledge is encoded in knowledge base
3. A set of new questions are raised to the users
4. Matching the answers convert personality is returned
5. No match occur error message displayed
6. Stop.

### Source Code: `ex4.pl`[view file](./exp4.pl)

```pl
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

```

### Output:

```bash
% c:/users/harsh/onedrive/documents/prolog/exp4 compiled 0.00 sec, 0 clauses
?- run.
Do you have HEADACHE?y.
Do you have TEMPERATURE?|: n.
Do you have a SORE THROAT?|: y.
Are you feeling TIRED?|: y.
You are suffering from COLD
true .
```

## 5. Write a program to solve the 4-Queen problem.
### Description
In the 4 Queens problem the object is to place 4 queens on a chessboard in such a way that no queens can capture a piece. This means that no two queens may be placed on the same row, column, or diagonal.
### Source Code: `ex5.pl`[view file](./exp5.pl)
```pl
queens(N, Queens) :-
    length(Queens, N),
    board(Queens, Board, 0, N, _, _),
    queens(Board, 0, Queens).

board([], [], N, N, _, _).

board([_|Queens], [Col-Vars|Board], Col0, N, [_|VR], VC):-
    Col is Col0+1,
    functor(Vars, f, N),
    constraints(N, Vars, VR, VC),
    board(Queens, Board, Col, N, VR, [_|VC]).

constraints(0, _, _, _):- !.

constraints(N, Row, [R|Rs], [C|Cs]):-
    arg(N, Row, R-C),
    M is N-1,
    constraints(M, Row, Rs, Cs).

queens([], _, []).

queens([C|Cs], Row0, [Col|Solution]) :-
    Row is Row0+1,
    select(Col-Vars, [C|Cs], Board),
    arg(Row, Vars, Row-Row),
    queens(Board, Row, Solution).
```
### Output
```bash
ጀ% c:/users/harsh/onedrive/documents/prolog/exp5 compiled 0.00 sec, -2 clauses
?- queens(4,Queens).
Queens = [2, 4, 1, 3] .

?- queens(5,Queens).
Queens = [1, 3, 5, 2, 4] .

?- queens(7,Queens).
Queens = [1, 3, 5, 7, 2, 4, 6] .
```

## 6. Write a program to solve traveling salesman problems.
### Source Code: `exp6.pl`[view file](./exp6.pl)
```pl
road("tampa", "houston", 200).
road("gordon", "tampa", 300).
road("houston", "gordon", 100).
road("houston", "kansas_city", 120).
road("gordon", "kansas_city", 130).

route(Town1, Town2, Distance) :-
    road(Town1, Town2, Distance).

route(Town1, Town2, Distance) :-
    road(Town1, X, Dist1),
    route(X, Town2, Dist2),
    Distance is Dist1 + Dist2, !.
```
### Output
```bash
?- route("tampa", "houston", Distance).
Distance = 200.

?- route("gordon", "kansas_city", Distance).
Distance = 130 ;
Distance = 420.

?- route("tampa", "kansas_city", Distance).
Distance = 320 ;
Distance = 530.

?- route("houston", "kansas_city", Distance).
Distance = 120 ;
Distance = 230 ;
false.

?- route("houston", "gordon", Distance).
Distance = 100.

```
## 7. Write a program to solve water jug problems using Prolog.
### Source Code: `exp7.pl`[view file](./exp7.pl)
```pl
member(X, [X|_]).
member(X, [Y|Z]):-member(X,Z).

move(X,Y,_):-X=:=2,Y=:=0,write('done'),!.

move(X,Y,Z):-X<4,\+member((4,Y),Z),
    write("fill 4 gallon jug"),nl,move(4,Y,[(4,Y)|Z]).

move(X,Y,Z):-Y<3, \+member((X,3),Z),
    write("fill 3 gallon jug"),nl,move(X,3,[(X,3)|z]).

move(X,Y,Z):-X>0,\+member((0,Y),Z),
    write("pour 4 galloon jug"),nl, move(0,Y,[(0,Y)|Z]).

move(X,Y,Z):-Y>0,\+member((X,0),Z),
    write("pour 3 galloon jug"),nl, move(X,0,[(X,0)|Z]).

move(X,Y,Z):-P is X+Y, P>=4, Y>0,K is 4-X,M is Y-K,\+member((4,M),Z),
    write("pour from 3 gallon jug to 4 gallon jug"),nl, move(4, M, [(4,M)|Z]).

move(X,Y,Z):-P is X+Y, P>=3, X>0,K is 3-Y,M is X-K,\+member((M,3),Z),
    write("pour from 4 gallon jug to 3 gallon jug"),nl, move(M,3,[(M,3)|Z]).

move(X,Y,Z):-K is X+Y, K<4, Y>0, \+member((K,0),Z),
    write("pour from 3 gallon jug to 4 gallon jug"), nl, move(K,0,[(K,0)|Z]). move(X,Y,Z):-K is X+Y, K<3,X>0,\+member((0,K),Z),
    write("pour from 4 gallon jug to 3 gallon jug"),nl, move(0,K, [(0,K)|Z]).

```
### Output
```bash
% c:/users/harsh/onedrive/documents/prolog/exp7 compiled 0.00 sec, -2 clauses
?- move(0,0,[]).
fill 4 gallon jug
fill 3 gallon jug
pour 4 gallon jug
pour 3 gallon jug
pour from 3 gallon jug to 4 gallon jug
fill 3 gallon jug
pour from 3 gallon jug to 4 gallon jug
pour 4 gallon jug
pour 3 gallon jug
pour from 3 gallon jug to 4 gallon jug
done
true 

?- move(0,2,[]).
fill 4 gallon jug
fill 3 gallon jug
pour 4 gallon jug
pour 3 gallon jug
fill 4 gallon jug
pour from 4 gallon jug to 3 gallon jug
pour 3 gallon jug
pour from 4 gallon jug to 3 gallon jug
fill 4 gallon jug
pour from 4 gallon jug to 3 gallon jug
pour 3 gallon jug
done
true .
```
## 8. Write simple Prolog functions such as the following:
   - Remove the Nth item from the list.
   - Insert as the Nth item.
### Source Code: `exp8.pl`[view file](./exp8.pl)
```pl
delte(1,[_|T],T).
delte(P,[X|Y],[X|R]):-
    P1 is P-1,
    delte(P1,Y,R).

insert(X, 1, L, [X|L]).
insert(X, N, [H|T], [H|R]) :-
    N > 1,
    N1 is N - 1,
    insert(X, N1, T, R).
```
### Output
```bash
% c:/users/harsh/onedrive/documents/prolog/exp8 compiled 0.00 sec, -7 clauses
?- delte(4,[1,2,3,4,5,6],R).
R = [1, 2, 3, 5, 6] .

?- delte(2,[a,b,c,d,e],R).
R = [a, c, d, e] .

?- delte(5,[1,2,3,4,5,6],R).
R = [1, 2, 3, 4, 6] .

?- delete(2, [a, b, c, d],R).
R = [a, c, d] .

?- insert(x, 3, [a, b, c, d], Result).
Result = [a, b, x, c, d] .

?- insert(h, 5, [a, b, x, c, d], R).
R = [a, b, x, c, h, d] .
```
9. Assume the Prolog predicate `gt(A, B)` is true when A is greater than B. Use this predicate to define the predicate `addLeaf(Tree, X, NewTree)` which is true if NewTree is the Tree produced by adding the item X in a leaf node. Tree and NewTree are binary search trees. The empty tree is represented by the atom nil.
### Source Code: `exp9.pl`[view file](./exp9.pl)
```pl
% Check if an element is in a binary tree
in(X, t(_, X, _)).
in(X, t(L, _, _)) :- 
    in(X, L). 
in(X, t(_, _, R)) :- 
    in(X, R).

% Check if an element is in a binary search tree
in(X, t(_, X, _)).
in(X, t(Left, Root, Right)) :-
    gt(Root, X), 
    in(X, Left). 
in(X, t(Left, Root, Right)) :-
    gt(X, Root), 
    in(X, Right).

% Add an element to a binary search tree
add(Tree, X, NewTree) :-
    addroot(Tree, X, NewTree). 
add(t(L, Y, R), X, t(L1, Y, R)) :-
    gt(Y, X),
    add(L, X, L1). 
add(t(L, Y, R), X, t(L, Y, R1)) :-
    gt(X, Y), 
    add(R, X, R1). 

% Add an element to an empty tree
addroot(nil, X, t(nil, X, nil)). 
addroot(t(L, Y, R), X, t(L1, X, t(L2, Y, R))) :-
    gt(Y, X), 
    addroot(L, X, t(L1, X, L2)). 
addroot(t(L, Y, R), X, t(t(L, Y, R1), X, R2)) :-
    gt(X, Y), 
    addroot(R, X, t(R1, X, R2)).

% Display a binary tree
show(Tree) :-
    show2(Tree, 0).
show2(nil, _).
show2(t(Left, X, Right), Indent) :-
    Ind2 is Indent + 2, 
    show2(Right, Ind2), 
    tab(Indent), write(X), nl, 
    show2(Left, Ind2).

```
### Output
```bash
?- in(3, t(t(nil, 1, nil), 2, t(nil, 3, nil))).
true .

?- add(t(t(nil, 1, nil), 2, t(nil, 3, nil)), 4, NewTree).
NewTree = t(t(nil, 1, nil), 2, t(nil, 3, t(nil, 4, nil))).

?- show(t(t(nil, 1, nil), 2, t(nil, 3, nil))).
  3
2
  1
true.

?- add(nil, 5, D1),
|    add(D1, 3, D2).
D1 = t(nil, 5, nil),
D2 = t(t(nil, 3, nil), 5, nil) .

?- add(D2, 8, D3),
add(D3, 6, D4),
|    show(D3).|    
8
  6
D2 = nil,
D3 = t(nil, 8, nil),
D4 = t(t(nil, 6, nil), 8, nil) .
```
## 10. Write a Prolog predicate, `countLists(Alist, Ne, Nl)`, using accumulators, that is true when Nl is the number of items that are listed at the top level of Alist and Ne is the number of empty lists. Suggestion: First try to count the lists, or empty lists, then modify by adding the other counter.
### Source Code: `exp10.pl`[view file](./exp10.pl)
```pl
% Base case: an empty list has 0 empty sublists
empties([], 0).

% Recursive case: if the head of the list is an empty list, increment the count
empties([[]|L], R) :-
    empties(L, K),
    R is K + 1.

% Recursive case: if the head is not an empty list, just proceed with the tail
empties([X|L], K) :-
    X \= [],
    empties(L, K).

% Alternative implementation using findall and length to count empty sublists
empties(L, N) :-
    findall(X, (member(X, L), X = []), L1),
    length(L1, N).

```
### Output
```bash
ʹ% c:/users/harsh/onedrive/documents/prolog/exp10 compiled 0.00 sec, -8 clauses
empties([], 0).
true .

?- empties([[], [], [1,2], [], [3], []], Count).
Count = 4 .

?- empties([[], X, [], Y, Z, [[]]], Count).
X = Y, Y = Z, Z = [],
Count = 5 .

?- empties([[], [a], [], [b, c], [], [], [d], [], [e, f]], Count).
Count = 5 .

?- empties([[a, b], [], [c], [], [d, e], [], [], [f], [g], [], [], [h], [], [i, j, k]], Count).
Count = 7 .
```
## 11. Define a predicate `memCount(AList,Blist,Count)` that is true if Alist occurs Count times within Blist. Define without using an accumulator. Use "not" as defined in utilities.pro, to make similar cases are unique, or else you may get more than one count as an answer.
    Examples:
- `memCount(a,[b,a],N)`. N = 1 ;
- `memCount(a,[b,[a,a,[a],c],a],N)`. N = 4 ;
- `memCount([a],[b,[a,a,[a],c],a],N)`. N = 1 ; No

### Source Code: `exp11.pl`[view file](./exp11.pl)
```pl
% Check if an element is a direct member of a list
member_nested(X, [X|_]).
member_nested(X, [Head|Tail]) :-
    (   is_list(Head),
        member_nested(X, Head)
    ;   member_nested(X, Tail)
    ).

% Count occurrences of AList in List
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

% Recursive case: AList is not the head and not a member of the head
memCount(AList, [Head|Tail], Count) :-
    AList \= Head,
    (   \+ is_list(Head)
    ;   \+ member_nested(AList, Head)
    ),
    memCount(AList, Tail, Count).

% Initialization and main entry point for testing
:- initialization(main).
main :-
    memCount(a, [b, a], N1),
    write('N1 = '), write(N1), nl,
    memCount(a, [b, [a, a, [a], c], a], N2),
    write('N2 = '), write(N2), nl,
    memCount([a], [b, [a, a, [a], c], a], N3),
    write('N3 = '), write(N3), nl,
    halt.

```
### Output
```bash
% c:/users/harsh/onedrive/documents/prolog/test compiled 0.02 sec, 0 clauses
?- memCount([b], [b, [a, [b], c], b, [b, b]], Count).
Count = 3 .

?- member_nested(c, [b, [a, [b], c], d]).
true .

?- memCount(b, [b, [a, [b], c], d], Count).
Count = 2 .

?- member_nested(c, [b, [a, a, [a], c], d]).
true .

?- memCount(a, [b, [a, a, [a], c], d], Count).
Count = 3 .
```

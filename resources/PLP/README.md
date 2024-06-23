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

# 5. Write a program to solve the 4-Queen problem.
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
਀?- move(0, 0, []).
fill 4 gallon jug
fill 3 gallon jug
pour 4 galloon jug
pour 3 galloon jug
fill 4 gallon jug
pour from 4 gallon jug to 3 gallon jug
pour 3 galloon jug
pour from 4 gallon jug to 3 gallon jug
fill 4 gallon jug
pour from 4 gallon jug to 3 gallon jug
pour 3 galloon jug
done
true .

?- move(0, 2, []).
fill 4 gallon jug
fill 3 gallon jug
pour 4 galloon jug
pour 3 galloon jug
fill 4 gallon jug
pour from 4 gallon jug to 3 gallon jug
pour 3 galloon jug
pour from 4 gallon jug to 3 gallon jug
fill 4 gallon jug
pour from 4 gallon jug to 3 gallon jug
pour 3 galloon jug
done
true .
```
8. Write simple Prolog functions such as the following:
   - Remove the Nth item from the list.
   - Insert as the Nth item.
9. Assume the Prolog predicate `gt(A, B)` is true when A is greater than B. Use this predicate to define the predicate `addLeaf(Tree, X, NewTree)` which is true if NewTree is the Tree produced by adding the item X in a leaf node. Tree and NewTree are binary search trees. The empty tree is represented by the atom nil.
10. Write a Prolog predicate, `countLists(Alist, Ne, Nl)`, using accumulators, that is true when Nl is the number of items that are listed at the top level of Alist and Ne is the number of empty lists. Suggestion: First try to count the lists, or empty lists, then modify by adding the other counter.
11. Define a predicate `memCount(AList,Blist,Count)` that is true if Alist occurs Count times within Blist. Define without using an accumulator. Use "not" as defined in utilities.pro, to make similar cases are unique, or else you may get more than one count as an answer.
    Examples:

- `memCount(a,[b,a],N)`. N = 1 ;
- `memCount(a,[b,[a,a,[a],c],a],N)`. N = 4 ;
- `memCount([a],[b,[a,a,[a],c],a],N)`. N = 1 ; No

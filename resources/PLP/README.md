# List of Programs

## 1. Write simple facts for the following:

- A. Ram likes mango.
- B. Seema is a girl.
- C. Bill likes Cindy.
- D. Rose is red.
- E. John owns gold.

### Source Code: `ex1.pl`

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

### Source Code: `ex2.pl`

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

### Source Code: `ex3.pl`

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

4. Write a program in Turbo Prolog for medical diagnosis and show the advantages and disadvantages of green and red cuts.
5. Write a program to solve the 4-Queen problem.
6. Write a program to solve traveling salesman problems.
7. Write a program to solve water jug problems using Prolog.
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

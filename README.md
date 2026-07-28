# Knowledge Representation Using Prolog

## Problem Statement

Represent the following knowledge in Prolog:

- Marcus was a man.
- Marcus was a Pompeian.
- All Pompeians were Romans.
- Caesar was a ruler.
- All Romans were either loyal to Caesar or hated him.
- Everyone is loyal to someone.
- People only try to assassinate rulers they are not loyal to.
- Marcus tried to assassinate Caesar.
- All men are people.

---

## Prolog Program

```prolog
% Facts
man(marcus).
pompeian(marcus).
ruler(caesar).

% Rules
roman(X) :-
    pompeian(X).

person(X) :-
    man(X).

assassinate(marcus, caesar).

not_loyal(X, Y) :-
    assassinate(X, Y),
    ruler(Y).

hates(X, Y) :-
    not_loyal(X, Y).

loyal(X, Y) :-
    roman(X),
    Y = caesar,
    \+ hates(X, Y).

check_loyalty :-
    loyal(marcus, caesar),
    write('Marcus is loyal to Caesar.'), nl.

check_loyalty :-
    write('Marcus is NOT loyal to Caesar.'), nl.

check_hatred :-
    hates(marcus, caesar),
    write('Yes, Marcus hates Caesar.'), nl.

check_hatred :-
    write('No, Marcus does not hate Caesar.'), nl.
```

---

## Query 1

```prolog
?- check_loyalty.
```

### Output

```text
Marcus is NOT loyal to Caesar.
true.
```

---

## Query 2

```prolog
?- check_hatred.
```

### Output

```text
Yes, Marcus hates Caesar.
true.
```

---

## Result

The knowledge representation was successfully implemented in Prolog. The program concluded that Marcus is **not loyal to Caesar** and **hates Caesar**.

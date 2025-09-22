solve_blocks(Start, Goal, Solution) :-
    dfs(Start, Goal, [], Solution, 0, 10).

dfs(State, Goal, Path, Path, _, _) :-
    same_state(State, Goal).

dfs(State, Goal, CurrentPath, FinalPath, CurrentDepth, MaxDepth) :-
    CurrentDepth < MaxDepth,
    make_move(State, NextState, Move),
    \+ member(NextState, [State]),
    NewDepth is CurrentDepth + 1,
    dfs(NextState, Goal, [Move|CurrentPath], FinalPath, NewDepth, MaxDepth).

same_state([], []).

same_state(State1, State2) :-
    sort(State1, S1),
    sort(State2, S2),
    S1 = S2.

make_move(State, NewState, move(Block, table)) :-
    member(on(Block, Support), State),
    Support \= table,
    is_clear(Block, State),
    replace_position(State, on(Block, Support), on(Block, table), NewState).

make_move(State, NewState, move(Block, Target)) :-
    member(on(Block, Support), State),
    member(on(Target, _), State),
    is_clear(Block, State),
    is_clear(Target, State),
    Block \= Target,
    replace_position(State, on(Block, Support), on(Block, Target), NewState).

is_clear(Block, State) :-
    \+ member(on(_, Block), State).

replace_position([], _, _, []).
replace_position([Old|Rest], Old, New, [New|Rest]).
replace_position([Other|Rest], Old, New, [Other|NewRest]) :-
    Other \= Old,
    replace_position(Rest, Old, New, NewRest).

print_solution([]).
print_solution([move(Block, table)|Rest]) :-
    format('Move ~w to table~n', [Block]),
    print_solution(Rest).
print_solution([move(Block, Target)|Rest]) :-
    Target \= table,
    format('Move ~w onto ~w~n', [Block, Target]),
    print_solution(Rest).

example1 :-
    write('Initial: B on A, A on table'), nl,
    write('Goal: A on B, B on table'), nl, nl,
    
    Initial = [on(a, table), on(b, a)],
    Goal = [on(b, table), on(a, b)],
    
    (solve_blocks(Initial, Goal, Moves) ->
        (write('SOLUTION FOUND:'), nl,
         reverse(Moves, OrderedMoves),
         print_solution(OrderedMoves))
    ;
        write('No solution found')
    ), nl.


example2 :-
    write('Initial: A, B, C all on table'), nl,
    write('Goal: A on B, B on C, C on A (impossible circle)'), nl, nl,
    
    Initial = [on(a, table), on(b, table), on(c, table)],
    Goal = [on(a, b), on(b, c), on(c, a)],
    
    (solve_blocks(Initial, Goal, Moves) ->
        (write('SOLUTION FOUND:'), nl,
         reverse(Moves, OrderedMoves),
         print_solution(OrderedMoves))
    ;
        write('NO SOLUTION POSSIBLE')
    ), nl.

run_examples :-
    example1,
    example2,
    write('Program completed.'), nl.

:- initialization(run_examples).
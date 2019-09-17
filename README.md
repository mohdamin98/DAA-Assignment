# DAA-Assignment
# Egg Dropping Puzzle

Given
n eggs, building with k floors
Wanted
Smallest number of egg dropping experiments required to find
out in all cases, which floors an egg can be safely dropped from.

# Assumptions
An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If an egg breaks when dropped, then it would break if
dropped from a higher floor.
If an egg survives a fall then it would survive a shorter fall.
A first-floor drop may break eggs, and eggs may survive a
drop from the highest floor.

# Special Case: One Egg
Number of eggs = 1, number of floors = 21
We need at most 21 experiments

# Observations
Sub-tasks
At each point in time, we have a number of eggs n available
and a number of floors k to check
Contiguous floors to check
The height of the floors does not matter. At each point in time
we need to check a certain number of contiguous floors, say
from 10 to 14.
Height does not matter
Checking 10 to 14 is the same as checking 20 to 24.


# Solution Idea
We compute eggDrop(i,j) over and over again.
Remember results in a table
Allocate a 2-D table eggFloor that remembers the results; after
computing s = eggDrop(i,j), remember s in a table.
eggDrop [ i ] [ j ] = s ;

# hasse
Boolean lattice and Hasse diagrams drawing script(s)

## Explanation
Draws a Boolean lattice of size 2^N, given input N. 
I needed a simple script to quickly visualize some big Boolean functions and their properties such as monotonicity and how their True and False points are localized.
Read the Hasse diagrams from top to bottom. 

## Examples
N = 3: 

![N=3](https://github.com/user-attachments/assets/9059851c-cdd9-41dc-9ee8-7f8fa5fccbf3)


N = 6 : 

![N=6](https://github.com/user-attachments/assets/7152145e-e7ff-4dd6-94c0-3e9913e948f8)


Hasse diagram for the sum mod 2, N = 5: 

![N=5](https://github.com/user-attachments/assets/fa1abb3c-dd20-4de0-9dd7-bac2f3a97774)

Just for fun, lattice drawing for N=10 (took about 5 seconds to generate):

![N=10](https://github.com/user-attachments/assets/bcd270d8-ab27-4816-b80f-def5d67cd23f)


## Further work
Improve speed for N>12, allow dictionary input (truth table) for Boolean functions.

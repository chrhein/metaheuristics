# Thoughts on what to do on assignment 3

## Operators
- Always return a feasible solution. If not feasible after being processed by operator, return the initial solution.


### 2-exchange:
- Choose two random calls, and swap these.
- Pickup from call one should be swapped with pickup from call two, the same works with the deliveries.

### 3-exchange:
- Same as above.

### 1-insert:
- Choose a random call, insert at random as long as the call is valid for the vehicle.
- Loop inside the operator until being placed in a compatible vehicle (this is only a valid trick for assignment 3).


# Assignment 1 - INF273
By Christian Hein (dum009@uib.no)

<br><br>


### Task 1a


| S | 5 | `0` | 5 | 4 | 3 | 2 | 1 | 5 | `0` | 5 | 6 | 7 | 8 | 5 | `0` | 5 | S |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|


This is my solution representation to task 1a. 

A large ship carries a lot of cargo from an international hub further down the continent, and delivers this at the shipping company's hub in Norway. The hub is centrally placed in the middle of the larger cities, and these cities are connected to the hub through smaller feeder ships which travel at greater speed than the large ones. 

The smaller ships are travelling to different routes. *Route A* goes from port 5 through the ports 4, 3, 2, and 1, before returning back to port 5. In each port they off-load some cargo destined for the given port, and eventually picks up some cargo going to another port. The second route, *Route B*, does the exact same, but it goes from port 5 through the ports 6, 7 and 8 before returning to the hub.

This solution saves both time and costs, because the large ship does not need to visit every port and the smaller shipping routes are being handled simultaneously. The large ship also need to be full of cargo to be financially beneficial, so off-loading a lot of cargo while not picking up any at the same port would eventually harm the economy.

My solution representation is a compact list, where each route are separated by the 0-blocks. 

<img src=../assets/assignment1a_map.png height="500"/>

### Task 1b


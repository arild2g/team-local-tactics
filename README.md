# team-network-tactics
A game for the mandatory assignment

## Group 48
### Mathias Vehus & Arild Grimstveit

## Execution order
- Run Server.py
- Run two separate instances of Client.py

## How to play
- Pick champions by writing their corresponding names from the Champions table, presented after establishing connections between the clients and the server

## Results and match history
- The results of the game will be displayed after each player has created a team of two champions and a match is simulated
- The match history (results from previous games) will be recorded in the Match table in the sqlite3 TNTDatabase
- To see the match history, make sure to have sqlite3 installed, and run the following commands:

```
sqlite3 TNTDatabase

select * from Match
```
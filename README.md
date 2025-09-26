# VolleyStat
Basic statistics for amateurs to nerd out about volleyball.


## Usage
Should work a basic python install:

```
./src/statify.py my_match.stat
```

It will print out statistics grouped by player, grouped by action and an overall summary.


## `.stat` Annotation format
Match annotations are intended to be simple to type while watching a game.
Only annotations for the team you care about are recorded.

Lines starting with `#` are ignored.

The file starts with a team list:
* One player per line.
* First character is their shorthand identifier, followed by a space
* Rest of the line is their name.

After an empty line, the match annotation begins.
* Every point is recorded on a new line, and consists of one or more actions.
* Most actions consists of 3 characters, separated by spaces.


### Player identifier
The first character is shorthand for the player, typically the first letter of their name.
It is recommended to keep this lowercase for ease of typing.


### Action identifier
The second character is shorthand for the action type:
* a: Attack
* b: Block
* d: Dig
* r: Receive
* s: Set
* v: serVe

Notes:
* All first contacts (excl serve receives and blocks) are considered a dig
* All second contacts, including rescuing a bad pass, are considered sets
* Any blocking contact counts as a block.
* All third contacts, and _intentional_ attack hits are attacks.


### Quality ranking
All actions get assigned a quality value on a scale from 0 to 2.

* Quality 0 is for actions that directly lead to loss of the point.
* Quality 1 is for actions that do not score, or are simply OK.
* Quality 2 either leads directly to a point, or is considered optimal for non-scoring action types.


#### Attack
0. Attack error - hitting the net/out, net touch, getting stuff blocked.
1. Attack hit does not directly lead to a point
2. Attack hit leads directly to point (opponent never gains control).


#### Block
0. Block error - net touch, getting tooled.
1. Block touch, play continues on either side of the net
2. Stuff block.


#### Dig
0. Dig error - player must at least reach the ball, or be obviously out of position.  An overpass that is immediately killed counts as an error.
1. Dig, play continues on either side.
2. Great dig - either saving a tough ball, or placing the ball so that the setter has all options.


#### Receive
0. Serve receive error - ball unrecoverable.  Overpass that is immediately killed is an error.
1. Service reception, play continues either side
2. Great receive - perfect placement, setter has all options. There is no ranking adjustment for passing tough serves.

#### Set
0. Set error - ball is unreachable for third contact, double touch etc.  Trying hard but failing to make a play on a shanked receive/dig is _not_ an error, assign blame on the first touch.
1. Set is playable, but hitter has to adjust.
2. Set is well placed for a good attack, or was a spectacular recovery from the first contact.

#### Service
0. Net, out, foot fault
1. Serve, is successfully received by opponent
2. Ace (opponent never gains control)

# Cocktail Recommend Line Chat Bot
A line chat bot based on a finite state machine, and can recommend cocktail.
## Finite State Machine
![image](https://github.com/oucs638/TOC-Project-2020/blob/master/fsm.png)
## Usage
### Stage 0
- The initial state is `user`.
- The next state would be `base`, `flavor` or `random`.
### Stage 1
- If enter "base", will enter `base` state:
  - The next state would be `base0`, `base1`, `base2`, `base3`, `base4`, `base5`.
- If enter "flavor", will enter `flavor` state:
  - The next state would be `flavor00`, `flavor01`, `flavor02`, `flavor03`, `flavor04`, `flavor05`, `flavor06`, `flavor07`, `flavor08`, `flavor09`, `flavor10`, `flavor11`, `flavor12`
- If enter "random", will enter `random` state:
  - This state would recommend random three cocktails.
### Stage 2

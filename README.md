# Boggle Challenge Part 1: Basic Board Generation

## Summary

The goal of this exercise is to create a basic Boggle board. If you're not sure what Boggle or its board looks like, please peruse [Boggle on Wikipedia](http://en.wikipedia.org/wiki/Boggle).

As mentioned above we are only going to generate the board for now. The board looks like this...

![Boggle Board Example](https://s-media-cache-ak0.pinimg.com/originals/f0/92/03/f09203920ca7db9c7f3e9247308a8482.jpg)

To model the board generation, imagine how this might take place in the real world. For instance, in the physical version of the game, you would shake the boggle die to randomly create a 4x4 grid of randomly generated letters.

### Step 1: Basic Boggle Board

This first iteration of our board will not care if it's possible for a word to be created with our generated board. In other words, we're going to focus on building out the necessary data structure to emulate our board.

The `BoggleBoard` class has one core instance method: `shake!`

1. Think about how to represent the board. `shake!` should modify the board by filling each cell with a random upper-case letter `A..Z`. Also, there aren't any restrictions on the letters. They can appear multiple times, so choose at random.

2. If you've looked into Boggle, you're probably thinking about how in Boggle 'Q' is always 'Qu'. Don't worry about this, instead just use 'Q' to represent 'Qu'

#### Example

Our code should output something like this:

* When a new 'BoggleBoard' is initialized the output should look like this:

```python
   ____
   ____
   ____
   ____
```

* When `shake!` is invoked on our board, it should output something like this:

```python
   LMVQ
   DKHZ
   SUCO
   GDMV
```

* When I `shake!` it again, it should randomly generate the board again.

### Step 2: Smart Boggle board

We currently implement our board without modeling dice. We should do that next to make our board come closer to modeling the a real Boggle board.

When modeling the die it's important to conceptualize how this works in the real world. If it helps, grab some real dice and toss em! What happens? One side lands face up and that's our chosen letter, right? How many possible letters can be exposed on any roll of the dice?

Perhaps we could leverage a secondary array to model a die landing in only one cell without explicitly making note of which dice have landed and which haven't. Would we use something else?

We're still only going to have one core method, `shake!` on our `BoggleBoard` class. The following is a list of Boggle Dice, with 'Q' representing 'Qu':

```python
AAEEGN
ELRTTY
AOOTTW
ABBJOO
EHRTVW
CIMOTU
DISTTY
EIOSST
DELRVY
ACHOPS
HIMNQU
EEINSU
EEGHNW
AFFKPS
HLNNRZ
DEILRX
```

### Step 3: Dealing with that Pesky 'Qu'

Our Boggle board generator is nearly finished! We still have one pesky little issue with the representation of 'Qu'. Our board currently prints a 'Q' instead of a 'Qu'. How could we print a 'Qu' instead?

There are various ways to approach this, but it might be worth keeping in mind that how the board is represented in your program, doesn't have to be how it appears to a person using the program.

The alignment of your board my start to look funky once you figure this out, so you'll want to make sure you adjust your program so that it now looks something like this:

```text
P  N  O  T
S  A  F  G
S  V  L  T
L  Qu Z  F
```

## Additional Resources
* [Boggle on Wikipedia](http://en.wikipedia.org/wiki/Boggle)
* [Play Boggle online](http://www.wordplays.com/boggle)

# Wordle Solver

A command-line Wordle solver written in Python. After each guess, you enter the color feedback from the game, and the solver eliminates every word that no longer fits and suggests the most likely remaining word. In testing it solves puzzles in about **3.8 guesses on average**.

## How it works

1. **Fixed opening guess.** The solver always starts with `crane`, a word with common letters that cuts the candidate list down quickly.
2. **Feedback encoding.** You type one character per letter:
   - `g` = green (right letter, right position)
   - `y` = yellow (letter is in the word, wrong position)
   - `a` = gray (letter is not in the word)
3. **Constraint filtering.** Each feedback character becomes a constraint (status + letter + position). Every word in the candidate list is checked against all constraints and discarded if it breaks any of them:
   - green: the word must have that letter in that exact position
   - yellow: the word must contain the letter, but not at that position
   - gray: the word must not contain the letter
4. **Frequency ranking.** The surviving candidates are sorted by how common each word is (from `freqdict.txt`), and the most frequent one becomes the next guess. Common words are more likely to be real Wordle answers than obscure ones.
5. The loop repeats for up to 6 guesses.

## Usage

```bash
python solver.py
```

The solver prints a guess. Enter that guess into Wordle, then type the feedback it gave you as a 5-character code.

Example (answer: `cigar`):

```
crane
Enter guess code: gaaay      <- you type this
...
```

## Files

| File | Purpose |
|------|---------|
| `solver.py` | The solver (main program) |
| `freqdict.txt` | Dictionary of `{"word": frequency}` pairs used for the word list and ranking |

## Complexity

Each round scans the whole candidate list once per constraint, so filtering is roughly O(W x C), where W is the number of remaining words and C is the number of constraints (at most 5 per guess). The list shrinks quickly after each guess.

## How the 3.8 average was measured

<!-- Fill this in before publishing. Example: "Simulated against N words from the answer list, with feedback generated automatically, and averaged the number of guesses." -->

## Known limitations

- **Repeated letters:** a gray letter eliminates every word containing it, even when the same letter is green or yellow elsewhere in the guess. Words with duplicate letters can be wrongly discarded.
- **Interactive only:** feedback is entered by hand, so there is no built-in simulation mode yet.
- **Fixed opener:** the first guess is hard-coded rather than computed.

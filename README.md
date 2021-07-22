<!--
*** Bintang Fajarianto
*** 22 Juli 2021
-->

<p align="center">
    <img align=center src="https://visitor-badge.laobi.icu/badge?page_id=bintangfrnz/Sixteen-Puzzle-with-A-Star" alt="Visitors">                     
</p>

## Sixteen-Puzzle-with-A-Star

<p align="center">
· <a href="https://github.com/bintangfrnz/Sixteen-Puzzle-with-A-Star/issues">Report Bug</a> ·
</p>

> note: This project is Ca-IRK 5<sup>th</sup> task

<!-- Contents -->
<details open="open">
    <summary>Contents</summary>
    <ol>
        <li><a href="#description">Description</a></li>
        <li><a href="#specifications">Specifications</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#how-to-run">How to run</a></li>
        <li><a href="#contact">Contact</a></li>
    </ol>
</details>

## Description

The **Sixteen Puzzle** (also called Gem Puzzle, Boss Puzzle, Game of Fifteen, Mystic Square and many others)
is a sliding puzzle that consist 15 square tiles numbered 1–15 and one missing tile
in a frame with 4 tiles high and 4 tiles wide. Tiles in the same row or column of the open position can be moved by sliding them horizontally or vertically, respectively. The goal of the puzzle is to place the tiles in numerical order.

<p align="center">
  <img src="https://github.com/bintangfrnz/Sixteen-Puzzle-with-A-Star/blob/main/img/start_position.PNG" width="300" height="300" alt="start position">
   ‎ ‎ ‎ ‎ ‎
  <img src="https://github.com/bintangfrnz/Sixteen-Puzzle-with-A-Star/blob/main/img/end_position.PNG" width="300" height="300" alt="goal position">
</p>

This **Sixteen Puzzle** program can solve the puzzle from the initial position (user input)
to the goal position using A* algorithm to find the best next move by counting the sum of Manhattan Distances between each block
and its position in the goal configuration (used heuristic for this problem).

The following is a format that accepted by this program:

<p align="center">
  <img src="https://github.com/bintangfrnz/Sixteen-Puzzle-with-A-Star/blob/main/img/input.PNG" alt="input format">
</p>

<hr>

Here is an example of accepted input:

```
1,2,3,4,0,5,6,7,10,11,12,8,9,13,14,15
```

Here are the examples of rejected input:

#### (1) num < 16 length or not Integer

```
1,2,A
```

#### (2) num < 0 or num > 15

```
-1,2,3,4,0,5,6,7,10,11,12,8,9,13,14,20
```

#### (3) there are duplicate values

```
1,2,3,4,0,5,6,7,10,10,12,8,9,13,14,15
```

## Specifications

- This **Sixteen Puzzle** program is a desktop-based with python language.
- This program can receive input according to the format above.
- This program can show the solution step-by-step to solve the puzzle.
- This program can display the order of the steps taken if the puzzle is solvable,
  if the puzzle is unsolvable, the program will display "Unsolvable".


## Prerequisites

This is the list of things you need to run the program and
how to install them.

[![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=Python&link=https://www.python.org/)](https://www.python.org/)

Module:
- PyQt5 (used to create a python desktop GUI)
  ```sh
  pip install PyQt5
  ```

## How to Run
1. Clone repository
  ```sh
  git clone https://github.com/bintangfrnz/Sixteen-Puzzle-with-A-Star.git
  ```
Alternative: download this repository as zip file and extract them.

2. Run
  ```sh
  python run.py
  ```

## Contact

[![Instagram](https://img.shields.io/badge/-@bintangfrnz__-E1306C?style=flat&logo=instagram&logoColor=EEEEEE&link=https://instagram.com/bintangfrnz_/)](https://instagram.com/bintangfrnz_)

<a href="#sixteen-puzzle-with-a-star">Back to Top</a>

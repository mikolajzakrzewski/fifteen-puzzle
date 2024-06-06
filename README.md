
# Fifteen puzzle solver

Program for solving fifteen puzzle layouts using chosen strategies (bfs/dfs/astr) with given search orders (LRUD permutations) or heuristics (hamm/manh).


## Run Locally

Clone the project

```bash
  git clone https://github.com/mikolajzakrzewski/fifteen-puzzle.git
```

Go to the project directory

```bash
  cd fifteen-puzzle
```

Install packages

```bash
  pip install -r requirements.txt
```

Run the program

```bash
python main.py <strategy> <additional_parameter> <input_file> <output_file> <additional_output_file>
```

where:

```bash
<strategy> = bfs/dfs/astr

<additional_parameter> = 'LRUD' permutation for bfs/dfs; hamm/manh for astr

<input_file> = txt file containing the puzzle to solve 

<output_file> = txt file for output data

<additional_output_file> = txt file for additional output data
```


## Authors

- [@xfl0rek](https://github.com/xfl0rek)
- [@mikolajzakrzewski](https://github.com/mikolajzakrzewski)


## License

[MIT](https://choosealicense.com/licenses/mit/)


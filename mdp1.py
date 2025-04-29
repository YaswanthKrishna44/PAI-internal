rows, cols = 3, 3
states = [(i, j) for i in range(rows) for j in range(cols)]
gamma = 0.9
theta = 1e-4
actions = ['up', 'down', 'left', 'right'] 
def reward(state):
    return 1 if state == (2, 2) else 0
def next_state(state, action):
    i, j = state
    if action == 'up': i = max(i - 1, 0)
    elif action == 'down': i = min(i + 1, rows - 1)
    elif action == 'left': j = max(j - 1, 0)
    elif action == 'right': j = min(j + 1, cols - 1)
    return (i, j)
V = {s: 0 for s in states}
iteration = 0
while True:
    delta = 0
    print(f"\nIteration {iteration}:")
    for i in range(rows):
        print([round(V[(i, j)], 3) for j in range(cols)])

    for s in states:
        if s == (2, 2): 
            continue
        v = V[s]
        V[s] = max(reward(next_state(s, a)) + gamma * V[next_state(s, a)] for a in actions)
        delta = max(delta, abs(v - V[s]))
    iteration += 1
    if delta < theta:
        break

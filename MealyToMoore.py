moore_states = {
    'A_A': {'0': 'A_A', '1': 'B_B'},
    'B_B': {'0': 'C_A', '1': 'D_B'},
    'B_A': {'0': 'C_A', '1': 'D_B'},
    'C_A': {'0': 'D_C', '1': 'B_B'},
    'C_C': {'0': 'D_C', '1': 'B_B'},
    'D_B': {'0': 'B_B', '1': 'C_C'},
    'D_C': {'0': 'B_B', '1': 'C_C'},
    'E_C': {'0': 'D_C', '1': 'E_C'}
}

moore_outputs = {
    'A_A': 'A',
    'B_B': 'B',
    'B_A': 'A',
    'C_A': 'A',
    'C_C': 'C',
    'D_B': 'B',
    'D_C': 'C',
    'E_C': 'C'
}

initial_state = 'A_A'

def moore_process(input_str):
    state = initial_state
    output_seq = [moore_outputs[state]]
    for symbol in input_str:
        state = moore_states[state][symbol]
        output_seq.append(moore_outputs[state])
    return ''.join(output_seq)

inputs = ["00110", "11001", "1010110", "101111"]
for inp in inputs:
    print(f"Input: {inp} => Output: {moore_process(inp)}")
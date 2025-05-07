# jump.py

def try_jump(jumps, max_jumps, jump_velocity):
    if jumps < max_jumps:
        jumps += 1
        velocity_y = jump_velocity
        return velocity_y, jumps
    else:
        return None, jumps

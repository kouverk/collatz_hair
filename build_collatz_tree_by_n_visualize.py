import matplotlib.pyplot as plt
import math
import sys
import os
from tqdm import tqdm

def advance_collatz(i):
    if i % 2 == 0:
        return i // 2
    else:
        return i * 3 + 1

def draw_collatz_hair(ax, n, angle_step=1, y_step=1):
    """Draw a single collatz sequence as a 'hair' strand, starting from origin."""
    
    # Build the sequence first
    i = n
    sequence = [n]
    while i != 1:
        i = advance_collatz(i)
        sequence.append(i)
    
    # Reverse it so we start at 1 and end at n
    sequence = sequence[::-1]
    
    # Now draw starting from origin
    x, y = 0, 0
    coords_x, coords_y = [x], [y]
    
    for i in range(len(sequence) - 1):
        current = sequence[i]
        next_val = sequence[i + 1]
        
        # Direction based on whether next value is odd or even
        if next_val % 2 == 1:
            x -= angle_step
        else:
            x += angle_step
        y += y_step
        
        coords_x.append(x)
        coords_y.append(y)
    
    ax.plot(coords_x, coords_y, color='black', alpha=0.2, linewidth=1)

def build_collatz_visualization():
    file_name = os.path.basename(__file__)
    if len(sys.argv) != 2:
        print(f"Usage: python {file_name} <n>")
        sys.exit(1)

    N = int(sys.argv[1])
    
    fig, ax = plt.subplots(figsize=(12, 16))
    
    # Draw each hair iteratively — no storage needed

    for n in tqdm(range(1, N + 1)):
        # Spread starting points along x-axis
        x_offset = (n - N/2) * 0.5
        draw_collatz_hair(ax, n, x_offset=x_offset)
    
    ax.set_aspect('equal')
    #ax.axis('off')
    plt.tight_layout()
    plt.savefig(f'collatz_hair_{N}.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    build_collatz_visualization()
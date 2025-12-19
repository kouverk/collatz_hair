import matplotlib.pyplot as plt
import math
import sys
import os
from tqdm import tqdm

def get_collatz_sequence(n):
    """Get the full collatz sequence from n down to 1."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
    return sequence

def draw_collatz_hair(ax, n, step_length=2):
    """Draw a single collatz sequence as a 'hair' strand.

    Key: Draw REVERSED (from 1 outward to n) so all hairs share a common root.
    Uses Edmund Harriss method with different angles for even/odd.
    """
    # Get sequence and REVERSE it so we draw from 1 outward
    sequence = get_collatz_sequence(n)
    sequence = sequence[::-1]  # Now starts at 1, ends at n

    # All hairs start from the same root point
    x, y = 0, 0
    coords_x, coords_y = [x], [y]

    # Start pointing "up"
    angle = math.pi / 2

    # Different angles for even vs odd - this asymmetry creates the waves
    # Actual Numberphile/Edmund Harriss values (much smaller!)
    angle_even = math.pi / 40   # ~4.5 degrees
    angle_odd = -math.pi / 50   # ~3.6 degrees

    for val in sequence[1:]:  # skip the first (which is 1)
        # Turn based on the current value
        if val % 2 == 0:
            angle += angle_even
        else:
            angle += angle_odd

        # Step forward in current direction
        x += math.cos(angle) * step_length
        y += math.sin(angle) * step_length

        coords_x.append(x)
        coords_y.append(y)

    ax.plot(coords_x, coords_y, color='black', alpha=0.1, linewidth=0.5)

def build_collatz_visualization():
    file_name = os.path.basename(__file__)
    if len(sys.argv) != 2:
        print(f"Usage: python {file_name} <n>")
        sys.exit(1)

    N = int(sys.argv[1])

    fig, ax = plt.subplots(figsize=(16, 16))

    for n in tqdm(range(2, N + 1)):
        draw_collatz_hair(ax, n)

    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(f'collatz_hair_angle_{N}.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    build_collatz_visualization()

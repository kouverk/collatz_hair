import matplotlib.pyplot as plt
import matplotlib.patches as patches

PALETTE_SORTED = [
    (67/255, 5/255, 16/255),      # darkest
    (109/255, 8/255, 22/255),
    (125/255, 49/255, 61/255),
    (149/255, 50/255, 68/255),
    (198/255, 11/255, 44/255),
    (199/255, 14/255, 54/255),
    (204/255, 16/255, 50/255),
    (230/255, 63/255, 92/255),
    (245/255, 5/255, 53/255),
    (225/255, 81/255, 106/255),
    (239/255, 114/255, 136/255),
    (217/255, 120/255, 138/255),
    (229/255, 119/255, 138/255),  # lightest
]

fig, ax = plt.subplots(figsize=(12, 2))

for i, color in enumerate(PALETTE_SORTED):
    rect = patches.Rectangle((i, 0), 1, 1, facecolor=color)
    ax.add_patch(rect)

ax.set_xlim(0, len(PALETTE_SORTED))
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.show()

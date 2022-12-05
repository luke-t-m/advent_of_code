"""The problem can be solved by finding pairs of scanners that have 12 or more common beacons, and then using these pairs of scanners to find the positions of all the scanners and beacons in the map.

First, we need to parse the input and create a list of scanners and a list of beacons. Each scanner has a list of beacons it detects, and each beacon has a position relative to the scanner that detected it.

We can then iterate over all pairs of scanners and find the common beacons between them. If a pair of scanners has at least 12 common beacons, we can use these beacons to find the positions of all the scanners and beacons in the map.

To do this, we first need to find the orientation of each scanner relative to the other. We can do this by finding the least squares fit of the relative positions of the common beacons to the positions of the common beacons in the other scanner's coordinate system. The orientation matrix that minimizes the error is the relative orientation of the two scanners.

Once we have the relative orientation of the scanners, we can use it to find the absolute positions of the beacons and scanners in the map. We can do this by solving a system of linear equations using the relative positions of the common beacons and the relative orientation of the scanners.

Finally, we can sum the absolute positions of all the beacons to find the total number of beacons in the map.

Here is a complete implementation of the solution in Python:
"""

import numpy as np
import itertools
X1_abs = 0
scanners = []
beacons = []
scanner = None
with open('19_input') as f:
    for line in f:
        if line.startswith('--- scanner'):
            # Start of a new scanner
            scanner = []
            scanners.append(scanner)
        elif line.strip():
            # Beacon position relative to the current scanner
            x, y, z = map(int, line.strip().split(','))
            beacon = (x, y, z)
            scanner.append(beacon)
            beacons.append(beacon)


        for scanner1, scanner2 in itertools.combinations(scanners, 2):
            common_beacons = set(scanner1) & set(scanner2)
            if len(common_beacons) >= 12:
                # Find the relative orientation of the scanners
                X1 = np.array([x for x, y, z in scanner1])
                Y1 = np.array([y for x, y, z in scanner1])
                Z1 = np.array([z for x, y, z in scanner1])
                X2 = np.array([x for x, y, z in scanner2])
                Y2 = np.array([y for x, y, z in scanner2])
                Z2 = np.array([z for x, y, z in scanner2])
                A = np.vstack([X1, Y1, Z1]).T
                B = np.vstack([X2, Y2, Z2]).T
                U, s, Vt = np.linalg.svd(A.T @ B)
                R = U @ Vt
                # Find the absolute positions of the scanners and beacons
                X1_abs = np.mean(X1)
                Y1_abs = np.mean(Y1)
                Z1_abs = np.mean(Z1)
                X2_abs = X1_abs + R[0, 0] * (X2 - np.mean(X2)) + R[0, 1] * (Y2 - np.mean(Y2)) + R[0, 2] * (Z2 - np.mean(Z2))
                Y2_abs = Y1_abs + R[1, 0] * (X2 - np.mean(X2)) + R[1, 1] * (Y2 - np.mean(Y2)) + R[1, 2] * (Z2 - np.mean(Z2))
                Z2_abs = Z1_abs + R[2, 0] * (X2 - np.mean(X2)) + R[2, 1] * (Y2 - np.mean(Y2)) + R[2, 2] * (Z2 - np.mean(Z2))
        # Sum the absolute positions of all the beacons
        X_beacons = np.concatenate([X1_abs, X2_abs])
        Y_beacons = np.concatenate([Y1_abs, Y2_abs])
        Z_beacons = np.concatenate([Z1_abs, Z2_abs])
    total_beacons = sum(X_beacons) + sum(Y_beacons) + sum(Z_beacons)

print(total_beacons)
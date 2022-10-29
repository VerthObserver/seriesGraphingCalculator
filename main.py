
import numpy as np
import matplotlib.pyplot as plt

limit = 10

n = np.arange(0, limit, 1)
seq = 1/2**n
ser = np.zeros(shape=limit)
ser[0] = seq[0]

for i in range(0, limit - 1):
    ser[i + 1] = (ser[i] + seq[i + 1])

print(f"Indices: {n}")
print(f"\nSequence: {seq}")
print(f"\nSeries: {ser}")


fig, (ax1, ax2) = plt.subplots(2)

plt.suptitle("Sequence and series")

ax1.bar(n, seq, color='r')
ax1.set_title("Sequence")

ax2.bar(n, ser, color='b')
ax2.set_title("Series")

plt.show()

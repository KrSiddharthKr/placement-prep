import time

# print("Loading", end="", flush=True)
# # print("Loading", end="", flush=True)
# for i in range(5):
#     time.sleep(1)
#     print(".", end="", flush=True)
#     # print(".", end="", flush=True)
# print("Done!")

for i in range(5, 0, -1):
    print(f"Starting in {i}...", end="\r", flush=True)
    time.sleep(1)
print("Go!      ")
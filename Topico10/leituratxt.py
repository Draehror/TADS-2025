path = "./texto.txt"

# with open(path, "r") as f:
#     content = f.read()

#     print(content)

# with open(path, 'r') as f:
#     for i, line in enumerate(f):
#         if line.strip():
#             print(f"Line {i}: ", line.strip())

with open(path, 'r') as f:
    lst = [line.strip() for line in f if line.strip()]
    print(lst[1])
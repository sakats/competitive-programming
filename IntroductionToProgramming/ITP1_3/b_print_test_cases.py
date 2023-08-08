num_list = []
while True:
    input_line = int(input())
    if input_line:
        num_list.append(input_line)
    else:
        break

for i, j  in enumerate(num_list):
    print(f"Case {i+1}: {j}")

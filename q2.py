def create_spiral(n):
    spiral = [[0] * n for _ in range(n)]
    num = 1  # matrix starts with 1
    layers = (n + 1) // 2  # no. of layers
    
    for layer in range(layers):
        # top row
        for i in range(layer, n - layer):
            spiral[layer][i] = num
            num += 1
        
        # right row
        for i in range(layer + 1, n - layer):
            spiral[i][n - layer - 1] = num
            num += 1
        
        # bottom row
        for i in range(n - layer - 2, layer - 1, -1):
            spiral[n - layer - 1][i] = num
            num += 1
        
        # left row
        for i in range(n - layer - 2, layer, -1):
            spiral[i][layer] = num
            num += 1

    for row in spiral:
        print(" ".join(f"{num:2}" for num in row))

n = int(input("Enter the size of the spiral (n): "))
create_spiral(n)

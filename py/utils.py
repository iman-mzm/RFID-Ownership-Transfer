import random
# Function to perform bitwise XOR
def bitwise_xor(binary_str1, binary_str2):
    return ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(binary_str1, binary_str2))

# Function to perform left rotation
def left_rotation(X, Y):
    wt_y = Y.count('1')  # Hamming weight of Y
    L = len(X)  # Calculate L based on the length of X
    wt_y_mod_L = wt_y % L
    return X[wt_y_mod_L:] + X[:wt_y_mod_L]

# Function to perform Right rotation
def right_rotation(X, Y):
    wt_y = Y.count('1')  # Hamming weight of Y
    L = len(X)  # Calculate L based on the length of X
    wt_y_mod_L = wt_y % L
    return X[-wt_y_mod_L:] + X[:-wt_y_mod_L]

# Function to generate a random binary string of a given length
def generate_random_binary_string(length):
    return ''.join(str(random.randint(0, 1)) for _ in range(length))

# Function to simulate the permutation function
def permutation(X, Y):
    assert len(X) == len(Y), "Bit strings X and Y must have equal length"
    m = Y.count('1')  # Hamming weight of Y
    km_indices = [i for i in range(len(Y)) if Y[i] == '1']
    kn_indices = [i for i in range(len(Y)) if Y[i] == '0']
    # Construct the permutation Z 
    Z = ''.join([X[k] for k in km_indices[::-1]]) + ''.join([X[k] for k in kn_indices[::-1]])
    return Z

def inverse_permutation(Z, Y):
    assert len(Z) == len(Y), "Bit strings Z and Y must have equal length"
    m = Y.count('1')  # Hamming weight of Y
    km_indices = [i for i in range(len(Y)) if Y[i] == '1']
    kn_indices = [i for i in range(len(Y)) if Y[i] == '0']
    # Split Z into km and kn parts
    Z_km = Z[:m][::-1]
    Z_kn = Z[m:][::-1]
    # Reconstruct X using Z, km_indices, and kn_indices
    X = ['0'] * len(Y)
    for i in range(m):
        X[km_indices[i]] = Z_km[i]
    for i in range(len(Y) - m):
        X[kn_indices[i]] = Z_kn[i]
    return ''.join(X)




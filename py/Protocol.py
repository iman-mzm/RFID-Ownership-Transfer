import random
from utils import *
# Initialization Phase
l = 128 # The length of the values
# Step 1: Generate a l-bit random value for IDSx
IDSx = generate_random_binary_string(l)

# Step 2: Generate a l-bit random value for IDn
IDn = generate_random_binary_string(l)

# Step 3: Generate a l-bit random value for KR (temporary shared secret)
KR = generate_random_binary_string(l)

# Step 4: Generate a l-bit random value for KT (temporary shared secret)
KT = generate_random_binary_string(l)

# Step 5: Use the permutation function to create index data
index_data = {"fx(IDS1, ID1)": permutation(IDSx, IDn)}

# Define l-bit binary values for K1, K2, and K3 
K1 = generate_random_binary_string(l)
K2 = generate_random_binary_string(l)
K3 = generate_random_binary_string(l)

# Define a l-bit binary value for IDo (Identifier of the old owner)
IDo = generate_random_binary_string(l)

# Print the generated values
print("Initialization Phase:")
print("Generated IDo:", IDo)
print("Generated K1:", K1)
print("Generated K2:", K2)
print("Generated K3:", K3)
print("Generated IDSx:", IDSx)
print("Generated IDn:", IDn)
print("Generated KR:", KR)
print("Generated KT:", KT)
print("Index Data:", index_data)



# Step 1 & 2 (Based on Figure)
# RN

# Generate a random l-bit value for r1 using PRNG
r1 = generate_random_binary_string(l)

# Calculate A = r1 ⊕ KT
A = bitwise_xor(r1, KT)

# Send "hello" and A to the tag
message_to_tag = "hello"
#message_to_tag_binary = ''.join(format(ord(char), '08b') for char in message_to_tag)  # Convert "hello" to binary

# Concatenate the binary message and A
message_to_tag = (message_to_tag, A)

# Print the generated values and the message to the tag
#print("Generated r1:", r1)
#print("Generated A:", A)
print("Message to tag:", message_to_tag)





# Step 3 & 4
# Tag

# Extract r'1 from A by performing a bitwise XOR with KT
r1_prime = bitwise_xor(A, KT)
#print("r1_prime:", r1_prime)

# Calculate B' using the permutation function with inputs (r'1 ⊕ IDSx, KT)
r1_prime_xor_IDSx = bitwise_xor(r1_prime, IDSx)
B_prime = permutation(r1_prime_xor_IDSx, KT)

# Send IDSx and B' to the new owner (RN)
print("IDSx (to be sent to the new owner):", IDSx)
print("Generated B' (to be sent to the new owner):", B_prime)





# Step 5 & 6
# RN

# Calculate B using the permutation function with inputs (r1 ⊕ IDSx, KT)
r1_xor_IDSx = bitwise_xor(r1, IDSx)
B = permutation(r1_xor_IDSx, KT)

# Check if B equals B'
if B == B_prime:
    # Case 1: B equals B'
    # Generate a new random number r2 using PRNG
    r2 = generate_random_binary_string(l)
    #print("r2:", r2)
    
    # Calculate C = fx(r2 ⊕ IDSx, KR)
    r2_xor_IDSx = bitwise_xor(r2, IDSx)
    C = permutation(r2_xor_IDSx, KR)

    # Calculate D = Rot(r2, fx(IDn, KR))
    D = left_rotation(r2, permutation(IDn, KR))

    # Calculate fx(IDSx, IDn)
    fx_IDSx_IDn = permutation(IDSx, IDn)

    # Send IDSx, C, D, and fx(IDSx, IDn) to the old owner (RC)
    print("Generated IDSx (to be sent to the old owner):", IDSx)
    print("Generated C (to be sent to the old owner):", C)
    print("Generated D (to be sent to the old owner):", D)
    print("Generated fx(IDSx, IDn) (to be sent to the old owner):", fx_IDSx_IDn)

else:
    # Case 2: B is not equal to B', terminate the protocol
    print("B is not equal to B'. Protocol terminated.")





# Step 7 & 8
# RC

# Search for the corresponding index content in the index data table

if fx_IDSx_IDn in index_data.values():
    # Case 1: The result matches, ownership transfer request is legal

    # Extract r2 from C using fx, IDSx, and KR
    r2_xor_IDSx = inverse_permutation(C, KR)
    r2_prime = bitwise_xor(r2_xor_IDSx, IDSx)
    #print("r2_extracted:", r2_prime)
    
    # Recalculate D' = Rot(r'2, fx(IDn, KR))
    D_prime = left_rotation(r2_prime, permutation(IDn, KR))

    # Check if D' equals D
    if D_prime == D:
        # Calculate random number r3
        r3 = generate_random_binary_string(l)
        # Calculate E = fx(r3, r2) ⊕ KR
        E = bitwise_xor(permutation(bitwise_xor(r3, r2_prime), KR), KR)

        # Calculate F = Rot(r2 ⊕ KR, fx(IDo, r3))
        F = left_rotation(bitwise_xor(r2_prime, KR), permutation(IDo, r3))

        # Calculate G = fx(K1 ⊕ K2, K2 ⊕ K3)
        G = permutation(bitwise_xor(K1, K2), bitwise_xor(K2, K3))

        # Calculate H = Rot(K2 ⊕ K3, IDn ⊕ KR)
        H = left_rotation(bitwise_xor(K2, K3), bitwise_xor(IDn, KR))

        # Send E, F, G, and H to the new owner (RN)
        print("Generated E (to be sent to the new owner):", E)
        print("Generated F (to be sent to the new owner):", F)
        print("Generated G (to be sent to the new owner):", G)
        print("Generated H (to be sent to the new owner):", H)
    else:
        # D' is not equal to D, terminate the protocol
        print("D' is not equal to D. Protocol terminated.")
else:
    # Case 2: The result does not match, terminate the protocol
    print("Result does not match. Ownership transfer request is not legal. Protocol terminated.")





# Step 9 & 10
# RN

# Extract r'3 from E
E_xor_KR = bitwise_xor(E, KR)
r3_prime = inverse_permutation(E_xor_KR, r2)

# Calculate F' = Rot(r2 ⊕ KR, fx(IDo, r'3))
F_prime = left_rotation(bitwise_xor(r2, KR), permutation(IDo, r3_prime))

# Check if F' equals F
if F_prime == F:
    # Case 1: F is successfully verified
    #Extract K2 ⊕ K3 from H
    K2_xor_K3 = right_rotation(H, bitwise_xor(IDn, KR))
    
    # Generate a random number r4 using PRNG
    r4 = generate_random_binary_string(l)

    # Calculate I = fx(r4 ⊕ KT, K2 ⊕ K3)
    I = permutation(bitwise_xor(r4, KT), K2_xor_K3)

    # Calculate J = Rot(fx(r4, KT), r4 ⊕ IDSx)
    J = left_rotation(permutation(r4, KT), bitwise_xor(r4, IDSx))

    # Calculate G ⊕ I
    G_xor_I = bitwise_xor(G, I)
    
    # Send G ⊕ I and J to the tag
    print("Generated G ⊕ I (to be sent to the tag):", G_xor_I)
    print("Generated J (to be sent to the tag):", J)
else:
    # Case 2: F is not successfully verified, abort the protocol
    print("F is not successfully verified. Protocol aborted.")





# Step 11 & 12
# Tag

#Extract r'4 from G ⊕ I
K1_xor_K2_xor_r4_xor_KT = inverse_permutation(G_xor_I, bitwise_xor(K2, K3))
K1_xor_K2 = bitwise_xor(K1, K2)
K1_xor_K2_xor_KT = bitwise_xor(K1_xor_K2, KT)
r4_prime = bitwise_xor(K1_xor_K2_xor_r4_xor_KT, K1_xor_K2_xor_KT)

# Calculate J' = Rot(fx(r4, KT), r4 ⊕ IDSx)
r4_xor_IDSx = bitwise_xor(r4_prime, IDSx)
fx_r4_KT = permutation(r4_prime, KT)
J_prime = left_rotation(fx_r4_KT, r4_xor_IDSx)

# Check if J' == J
if J_prime == J:
    # Tag deems the old owner authorized to transfer ownership
    print("Tag deems the old owner authorized to transfer ownership")
    # Calculate L = fx(r4 ⊕ r1, KT) ⊕ r4
    r4_xor_r1 = bitwise_xor(r4, r1)
    L = bitwise_xor(permutation(r4_xor_r1, KT), r4)

    # Send L to the new owner
    print("L (to be sent to the new owner):", L)
else:
    # Tag does not authorize ownership transfer
    print("Ownership transfer not authorized.")





# Step 13 & 14
# RN

# Calculate L'
r4_xor_r1 = bitwise_xor(r4, r1)
L_prime = bitwise_xor(permutation(r4_xor_r1, KT), r4)

# Verify L and handle the cases
if L == L_prime:
    # Generate a random value for r5
    r5 = generate_random_binary_string(l)

    # Calculate M = fx(r4, KT) ⊕ r5
    fx_r4_KT = permutation(r4, KT)
    M = bitwise_xor(fx_r4_KT, r5)

    # Calculate N = Rot(r5, fx(r4, KT ⊕ IDSx))
    KT_xor_IDSx = bitwise_xor(KT, IDSx)
    fx_r4_KT_IDSx = permutation(r4, KT_xor_IDSx)
    N = left_rotation(r5, fx_r4_KT_IDSx)

    # Update pseudonym and shared keys
    IDSx_new = permutation(bitwise_xor(IDSx, r4), r5)
    #K1_xor_K2 = inverse_permutation(G, K2_xor_K3)
    K1_new = bitwise_xor(permutation(inverse_permutation(G, K2_xor_K3), r4), r5)
    K2_new = permutation(K2_xor_K3, r5)
    K3_new = permutation(bitwise_xor(KT, r4), r5)
 
    # Case 1: Send M, N to the tag. Update IDSx_new, K1_new, K2_new, K3_new, KT_new
    print("M (to be sent to the tag):", M)
    print("N (to be sent to the tag):", N)
    print("IDSx_new:", IDSx_new)
    print("K1_new:", K1_new)
    print("K2_new:", K2_new)
    print("K3_new:", K3_new)
    
else:
    # Case 2: abort the protocol
    print("Verification failed. Abort the protocol.")





# Step 15
# Tag

# Calculate r'5 from M
r5_prime = bitwise_xor(M, permutation(r4, KT))

# Calculate the local value of N
N_prime = left_rotation(r5_prime, permutation(r4, bitwise_xor(KT, IDSx)))

# Verify if the calculated N matches the received N
if N_prime == N:
    # Verification successful, update the pseudonym and shared secret
    IDSx_new = permutation(bitwise_xor(IDSx, r4), r5_prime)
    K1_new = bitwise_xor(permutation(bitwise_xor(K1, K2), r4), r5_prime)
    K2_new = permutation(bitwise_xor(K2, K3), r5_prime)
    K3_new = permutation(bitwise_xor(KT, r4), r5_prime)

    # Print the updated pseudonym and shared secret
    print("IDSx_new:", IDSx_new)
    print("K1_new:", K1_new)
    print("K2_new:", K2_new)
    print("K3_new:", K3_new)

else:
    # Verification failed
    print("Verification failed. Do not update pseudonym and shared secret.")





#Old Owner

if IDSx_new != IDSx:
    IDSx = IDSx_new
    K1 = K1_new
    K2 = K2_new
    K3 = K3_new
elif IDSx_new == IDSx:
    IDSx = IDSx
    K1 = K1
    K2 = K2
    K3 = K3
    
print("Updated IDSx:", IDSx)
print("Updated K1:", K1)
print("Updated K2:", K2)
print("Updated K3:", K3)








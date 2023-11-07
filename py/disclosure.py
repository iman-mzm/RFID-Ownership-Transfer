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




# Disclosure attack
# The goal is to retrieve the agreed session key between the new owner and the tag

# Tag initialization (unknown to the attacker)
print("IDSx:", IDSx)
print("KT:", KT)

# Attack:
# Attacker (Generate a random value to start the attack)
A1 = generate_random_binary_string(l)  # Send "hello" and A to the tag

#Tag (calculations)
r1_prime = bitwise_xor(A1, KT)
r1_prime_xor_IDSx = bitwise_xor(r1_prime, IDSx)
B_prime = permutation(r1_prime_xor_IDSx, KT)  # Send IDSx and B' to the attacker

#print("length:", l)
KT_R = [1] * l  # The initial value of KT for recovering

# Main loop for the attack
for i in range(l):
    
  # Attacker  
  e = [0 for b in range(l)]  
  e[i] = 1  # Standard basis
  e = "".join(str(element) for element in e) 
  A = bitwise_xor(A1, e)  # Sends A and "hello" to the Tag

  # Tag  
  r = bitwise_xor(A, KT)
  r_xor_IDSx = bitwise_xor(r, IDSx)
  B = permutation(r_xor_IDSx, KT)   # Sends IDSx and B' to the attacker

  # Attacker  
  delta = bitwise_xor(B_prime, B)   
  #print("delta:", delta)  
  m = KT_R[:i].count(0) 
  if delta[(l-1)-m] == '1':
    KT_R[i] = 0
  else:
    KT_R[i] = 1 

KT_R = "".join(str(bit) for bit in KT_R)
print("KT_R (Recovered):", KT_R)
print("KT == KT_R:", KT == KT_R)








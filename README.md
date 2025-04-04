# Evaluating Security Pitfalls of Ultra-Lightweight IoT Authentication
This repository contains simulations of the protocol, analysis, and attacks performed on the proposed protocol in paper [1].

![out2 00_00_00-00_00_09](https://github.com/user-attachments/assets/22493b30-6b7c-48f7-8bec-5862824c598b)

## Project Structure

The project is organized into the following directories:
- `ipynb`: Contains Jupyter notebooks for interactive simulations and analyses.
- `py`: Contains Python scripts for protocol simulations and attacks.

## Instructions for Running the Protocol and Attacks

1. **Navigate to the Python Scripts Directory:**
   - Change directory to the `py` folder:
     ```bash
     cd RFID-Ownership-Transfer/py/
     ```

2. **Run the Protocol Simulation:**
   - Execute the `Protocol.py` script to run the ownership transfer protocol simulation:
     ```bash
     python Protocol.py
     ```

3. **Run Specific Attacks:**
   - To run an attack simulation, execute the corresponding script. For example, to run the privacy violation attack:
     ```bash
     python Privacy_violation.py
     ```

### Example:
```bash
cd RFID-Ownership-Transfer/py/
python Protocol.py
python Privacy_violation.py
```
Additionally, you can explore and simulate specific attacks, such as the **Desynchronization**, **Full Secret Disclosure**, and **Violation of the New Owner's Privacy**, all of which are detailed below, to analyze their impact on the protocol's security.

### Desynchronization Attack

A **Desynchronization attack** is a targeted attempt to disrupt the synchronization of critical elements in the protocol. This includes cryptographic keys and other important parameters that ensure the protocol operates securely. By causing misalignment, this attack can compromise the protocol's effectiveness and security.

#### Attack Scenario:

In this attack, the attacker intercepts and blocks messages from the new owner that are crucial for updating the tag's parameters. Specifically, the attacker blocks the messages **M** and **N** sent by the new owner, preventing the tag from receiving these updates. As a result, the tag does not update its parameters, and the old owner remains unaware of the new owner's actions.

#### Impact of the Attack:

- The tag and the old owner do not update their values after the new owner has made changes.
- This leads to desynchronization between the new owner's state and the tag's state.
- The attacker can then manipulate the tag and the old owner by maintaining their old parameters, undermining the security of the protocol.

#### Steps to Simulate the Desynchronization Attack:

1. **Run the protocol simulation** by following the instructions in the previous section.
2. **Execute the Desynchronization attack** by running the `desynchronization.py` script.

```bash
cd RFID-Ownership-Transfer/py/
python desynchronization.py

```
### Full Secret Disclosure Attack

A **Full Secret Disclosure attack** allows an attacker to recover a secret value of length $l$ by conducting $l+1$ sessions with the tag. The attacker can be anyone, including the old owner $R_C$. By exploiting this attack, the attacker will be able to fully recover the session key $K_T$ shared between the new owner and the tag after executing $l+1$ sessions.

#### Attack Scenario:

The attack begins with the tag receiving a "hello" message and the value $A$ calculated by $R_N$. The tag calculates $B' = f_x(r'_1 \oplus IDS_x, K_T)$ and sends $B'$ along with its identifier to the new owner. The attacker can exploit the first three steps of the protocol to recover the session key $K_T$.

Since the tag is passive, the attacker can start a session with the same secret session parameters. The attacker generates a random value $A$, sends it along with a "hello" message to the tag, and the tag responds with $B'$. By adding the value $A$ to the standard basis vector $e_i$, the attacker generates $A_i = A \oplus e_i$ and sends it to the tag. The tag computes $B'_i = f_x(r'_1,i \oplus IDS_x, K_T)$ and sends $B'_i$ back.

The attacker compares the values of $B'$ and $B'_i$ for each session, using differences in the values to deduce each bit of $K_T$.

#### Impact of the Attack:

- The attacker can recover each bit of $K_T$ by performing $l+1$ sessions with the tag.
- The attack takes advantage of a weakness in the permutation function, where small differences in $B'$ and $B'_i$ reveal information about the corresponding bit of the secret $K_T$.
- After $l+1$ sessions, the attacker will know the entire value of $K_T$.

#### Steps to Simulate the Full Secret Disclosure Attack:

1. **Run the protocol simulation** by following the instructions in the previous section.
2. **Execute the Full Secret Disclosure attack** by running the `disclosure.py` script.

```bash
cd RFID-Ownership-Transfer/py/
python disclosure.py
```

### Violation of the New Owner's Privacy

The **Violation of the New Owner's Privacy** attack targets the privacy of the new owner in an ownership transfer protocol. It ensures that the adversary, including the previous owner, cannot infer or track the private information of the new owner. However, as described in [1], the old owner is believed to be unable to track the tag or guess the new shared keys. Contrary to this, we present an attack where the previous owner can fully recover the session key and updated parameters, compromising the new owner's privacy.

#### Attack Scenario:

In this attack, the previous owner, after recovering the session key $K_T$ in the **Full Secret Disclosure attack**, can eavesdrop on messages **$G \oplus I$** and **$M$** that the new owner sends to the tag. By doing so, the previous owner can extract the random values $r_4$ and $r_5$ and use these to compute the new tag ID and the updated keys for the new owner.

After obtaining $K_T$, $r_4$, and $r_5$, the attacker (previous owner) can compute the new tag ID and updated keys using the relationships derived from the protocol.

#### Steps to Simulate the Privacy Violation Attack:

1. **Run the protocol simulation** by following the instructions in the previous section.
2. **Execute the Violation of the New Owner's Privacy attack** by running the `Privacy_violation.py` script.

```bash
cd RFID-Ownership-Transfer/py/
python Privacy_violation.py
```
```bash
[1] Bi, Y., Fan, K., Zhang, K., Bai, Y., Li, H., & Yang, Y. (2023). A secure and efficient two-party protocol enabling ownership transfer of RFID objects. IEEE Internet of Things Journal.
```

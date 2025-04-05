# Evaluating Security Pitfalls of Ultra-Lightweight IoT Authentication
This repository contains simulations of the protocol, analysis, and attacks performed on the proposed protocol in paper [1].

![out2 00_00_00-00_05_48](https://github.com/user-attachments/assets/b1e62f5f-91c7-4cd9-831d-871adab3a73c)

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

A **Desynchronization attack** involves an adversary intentionally interfering with the synchronization of key cryptographic components used in the IoT authentication protocol, such as cryptographic keys and associated values. This type of attack disrupts the regular update process of these keys and other critical elements, which undermines the integrity and security of the protocol.

#### Attack Scenario:

In this attack, an adversary intercepts and blocks critical messages (specifically $M$ and $N$) during the ownership transfer process. Since the tag and the old owner rely on the successful reception of these messages to update their values, blocking them results in a misalignment between the new and old owners' parameters, leaving the system vulnerable to impersonation.

1. The new owner updates their keys and the tag’s ID as per the protocol. However, the attacker blocks the transmission of the update messages ($M$ and $N$) sent to the tag, preventing it from receiving the new values.

2. The tag and old owner remain with outdated values because they were not updated with the new messages.

3. The new owner (now under the assumption that the update was successful) proceeds with actions that should have been verified by the tag and the old owner. However, since the tag and old owner have not received the update, they cannot authenticate the new owner.

#### Impact of the Attack:

- The tag and the old owner do not update their values after the new owner has made changes.
- This leads to desynchronization between the new owner's state and the tag's state.
- The attacker can then manipulate the tag and the old owner by maintaining their old parameters, undermining the security of the protocol.

#### Steps to Simulate the Desynchronization Attack:

1. Clone the repository and navigate to the **py** folder.
2. **Execute the Desynchronization attack** by running the `desynchronization.py` script.

```bash
cd RFID-Ownership-Transfer/py/
python desynchronization.py

```
The following steps illustrate how the attack unfolds in the simulation:
   1. The protocol initiates by generating random values for the identifiers ($IDSx$, $IDn$) and cryptographic keys ($K1$, $K2$, $K3$, etc.).
   2. During the simulation, the attacker blocks the transmission of the crucial messages ($M$ and $N$) from the new owner to the tag.
   3. The tag and old owner retain their outdated values while the new owner continues with actions based on incorrect assumptions.

The output will display the internal secret values of each entity involved in the protocol after the desynchronization attack, showing that the tag and old owner retain their original values while the new owner proceeds without proper authentication from the tag.

### Full Secret Disclosure Attack

A **Full Secret Disclosure attack** allows an attacker to recover a secret value of length $l$ by conducting $l+1$ sessions with the tag. The attacker can be anyone, including the old owner $R_C$. By exploiting this attack, the attacker will be able to fully recover the session key $K_T$ shared between the new owner and the tag after executing $l+1$ sessions.

#### Attack Scenario:

In this attack, the adversary can recover the secret session key $K_T$, which is shared between the new owner and the tag, by conducting $l+1$ sessions with the tag. The attacker can be any participant, including the old owner $R_C$. After executing the attack, the attacker will fully disclose the secret key $K_T$.

The attack begins with the tag receiving a "hello" message and the value $A$ calculated by $R_N$. The tag calculates $B' = f_x(r'_1 \oplus IDS_x, K_T)$ and sends $B'$ along with its identifier to the new owner. The attacker can exploit the first three steps of the protocol to recover the session key $K_T$.

Since the tag is passive, the attacker can start a session with the same secret session parameters. The attacker generates a random value $A$, sends it along with a "hello" message to the tag, and the tag responds with $B'$. By adding the value $A$ to the standard basis vector $e_i$, the attacker generates $A_i = A \oplus e_i$ and sends it to the tag. The tag computes $B'_i = f_x(r'_1,i \oplus IDS_x, K_T)$ and sends $B'_i$ back.

The attacker compares the values of $B'$ and $B'_i$ for each session, using differences in the values to deduce each bit of $K_T$.

#### Impact of the Attack:

- The attacker can recover each bit of $K_T$ by performing $l+1$ sessions with the tag.
- The attack takes advantage of a weakness in the permutation function, where small differences in $B'$ and $B'_i$ reveal information about the corresponding bit of the secret $K_T$.
- After $l+1$ sessions, the attacker will know the entire value of $K_T$.

#### Steps to Simulate the Full Secret Disclosure Attack:

1. Clone the repository and navigate to the **py** folder.
2. **Execute the Full Secret Disclosure attack** by running the `disclosure.py` script.

```bash
cd RFID-Ownership-Transfer/py/
python disclosure.py
```
The repository contains the Python code for simulating the attack in the disclosure.py file. The following steps are performed in the code:
   1. Initialization Phase: Random values for $IDS_x$, $ID_n$, $K_T$, and other parameters are generated.
   2. Attack Phase: The attacker generates a random value $A$, sends it to the tag, and performs $l$ sessions to extract each bit of the key $K_T$.
   3. Key Recovery: The attacker compares the received $B'_i$ values and recovers the $K_T$ key bit by bit.

The output will display the recovered session key $K_T$ and compare it with the original key. The attack is considered successful if $K_T == KT_R$.

### Violation of the New Owner's Privacy

In ownership transfer protocols, the privacy of both the previous and new owners must be carefully protected. It is essential that neither the adversary nor the previous owner can deduce any private information about the new owner. However, in this attack, we demonstrate that the previous owner (or attacker) can compromise the new owner's privacy by recovering the new owner's session key and tracking the tag.

#### Attack Scenario:

In this attack, the previous owner leverages the Disclosure Attack (described in a previous section) to recover the session key $K_T$ shared between the tag and the new owner. After obtaining $K_T$, the attacker can eavesdrop on the messages $G \oplus I$ and $M$ sent by the new owner to the tag during the protocol.

With the knowledge of $K_T$, $r_4$, and $r_5$, the attacker can compute the new tag ID and the updated keys of the new owner. The attacker can extract the random values $r_4$ and $r_5$ from the eavesdropped messages and use the relationships in the protocol to compute the new tag ID and updated session keys for the new owner.

#### Steps to Simulate the Privacy Violation Attack:

1. Clone the repository and navigate to the **py** folder.
2. **Execute the Violation of the New Owner's Privacy attack** by running the `Privacy_violation.py` script.

```bash
cd RFID-Ownership-Transfer/py/
python Privacy_violation.py
```
The following steps are performed in the code:
   1. Initialization Phase: Random values for $IDS_x$, $ID_n$, $K_T$, and other parameters are generated.
   2. Main Protocol: The protocol proceeds with the standard ownership transfer steps, and the attacker monitors the messages exchanged between the new owner and the tag.
   3. Key and ID Extraction: The attacker uses the homomorphic property of the permutation function to extract the random values $r_4$ and $r_5$ and computes the updated values for the tag ID and the new owner's keys.

The output will display the recovered new tag ID and the updated keys for the new owner. It will also confirm whether the attacker was able to successfully compromise the new owner's privacy.

```bash
[1] Bi, Y., Fan, K., Zhang, K., Bai, Y., Li, H., & Yang, Y. (2023). A secure and efficient two-party protocol enabling ownership transfer of RFID objects. IEEE Internet of Things Journal.
```

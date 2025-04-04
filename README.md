# Evaluating Security Pitfalls of Ultra-Lightweight IoT Authentication
This repository contains simulations of the protocol, analysis, and attacks performed on the proposed protocol in paper [1].

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

## Desynchronization Attack

A **Desynchronization attack** is a targeted attempt to disrupt the synchronization of critical elements in the protocol. This includes cryptographic keys and other important parameters that ensure the protocol operates securely. By causing misalignment, this attack can compromise the protocol's effectiveness and security.

# Attack Scenario:

In this attack, the attacker intercepts and blocks messages from the new owner that are crucial for updating the tag's parameters. Specifically, the attacker blocks the messages **M** and **N** sent by the new owner, preventing the tag from receiving these updates. As a result, the tag does not update its parameters, and the old owner remains unaware of the new owner's actions.

# Impact of the Attack:

- The tag and the old owner do not update their values after the new owner has made changes.
- This leads to desynchronization between the new owner's state and the tag's state.
- The attacker can then manipulate the tag and the old owner by maintaining their old parameters, undermining the security of the protocol.

### Steps to Simulate the Desynchronization Attack:

1. **Run the protocol simulation** by following the instructions in the previous section.
2. **Execute the Desynchronization attack** by running the `desynchronization.py` script.

```bash
cd RFID-Ownership-Transfer/py/
python desynchronization.py

```
[1] Bi, Y., Fan, K., Zhang, K., Bai, Y., Li, H., & Yang, Y. (2023). A secure and efficient two-party protocol enabling ownership transfer of RFID objects. IEEE Internet of Things Journal.
```

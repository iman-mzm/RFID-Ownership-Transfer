# RFID Ownership Transfer Protocol
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


[1] Bi, Y., Fan, K., Zhang, K., Bai, Y., Li, H., & Yang, Y. (2023). A secure and efficient two-party protocol enabling ownership transfer of RFID objects. IEEE Internet of Things Journal.

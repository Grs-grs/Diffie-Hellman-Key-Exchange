# Diffie-Hellman-Key-Exchange
A simple Python implementation of the **Diffie-Hellman Key Exchange**, built as a hands-on exercise while studying introductory cryptography.

This project demonstrates how two participants can:

- generate their own public values
- exchange those public values openly
- independently calculate the same shared secret

The goal of this project is not to provide production-ready cryptography, but to reinforce the fundamentals behind modular exponentiation, public/private values, and secure key exchange concepts.

---

## What is Diffie-Hellman?

The Diffie-Hellman Key Exchange is a cryptographic method that allows two parties to establish a **shared secret** over an insecure channel.

Instead of sending the secret directly, both participants:

1. agree on public parameters
2. choose private secrets
3. calculate their own public values
4. exchange those public values
5. compute the same shared secret independently

This shared secret can later be used as the basis for symmetric encryption.

---

## How It Works

The protocol uses two public values:

- `p`: a public prime number
- `g`: a public base (generator)

Each participant chooses a private secret:

- Alice chooses `a`
- Bob chooses `b`

Then each one calculates a public value:

- `A = g^a mod p`
- `B = g^b mod p`

After exchanging `A` and `B`, both compute the shared secret:

- Alice computes: `B^a mod p`
- Bob computes: `A^b mod p`

Both results must be equal.

---

## Features

- Generates a public key from a private secret
- Generates a shared secret using the other participant's public value
- Uses two participant objects to simulate both sides of the exchange
- Prints both public values and both shared secrets
- Verifies whether the shared secrets match

---

## Project Structure

`DiffieHellman.py`  
`user.py`

Main elements of the project:

- `DiffieHellman` class
- `generate_public_key()` method
- `generate_shared_secret()` method
- `Person` class
- `main()` function

---

## Code Design

### `DiffieHellman` class

This class contains the core logic of the protocol.

#### `generate_public_key(private_secret, g, p)`

Calculates the participant's public value using:

`g^private_secret mod p`

#### `generate_shared_secret(other_user_public_value, private_secret, p)`

Calculates the shared secret using:

`other_user_public_value^private_secret mod p`

### `Person` class

This class represents a participant in the key exchange.

Each participant stores:

- `name`
- `private_secret`
- `public_value`
- `shared_secret`

---

## Example

Consider:

- `p = 29`
- `g = 5`
- Alice's private secret = `12`
- Bob's private secret = `17`

### Step 1: Generate public values

- `A = 5^12 mod 29 = 7`
- `B = 5^17 mod 29 = 9`

### Step 2: Generate shared secrets

- Alice computes: `9^12 mod 29 = 24`
- Bob computes: `7^17 mod 29 = 24`

Final result:

- both participants get the same shared secret: `24`

---

## Example Program Flow

Example input:

```text
Enter the public prime number (p): 29
Enter the public base (g): 5
Enter the first one's name: Alice
Enter Alice's private secret: 12
Enter the second one's name: Bob
Enter Bob's private secret: 17
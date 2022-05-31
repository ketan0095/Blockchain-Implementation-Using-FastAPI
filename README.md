# Simple Implementation of Blockchain with FastAPI

## What is Blockchain ?

*Blockchain technology is a structure that stores transactional records, also known as the **block**, of the public in several databases, known as the **chain**, in a network connected through peer-to-peer nodes. Typically, this storage is referred to as a ‘digital ledger.’*  

*In simpler words, the digital ledger is like a Google spreadsheet shared among numerous computers in a network and it is **immutable**.*
- - -

## Why Blockchain is popular ?

* Decentralized Syetem :  No central authority, No chance of corruption
* Highly Secure : Blocks are Immutable
* Automation Capabilities : can generate systematic actions, events, scalable
- - -

## What is a Block?

*A block is a place in a blockchain where information is **stored and encrypted**.*

*A Block consist of :*

| Block  | Example |
| ------------- |:-------------:|
| Block Index      | 0001     |
| Timestamp      | 1654021620     |
| Data      | "Send 0.5 BTC to User 2."     |
| Nonce/Proof      | 2335     |
| Previous Hash      | 26F673806ED0E3B5CBF52B3F25D02BF1BC09449DFBB7A6E6B739118F0D246644     |

*Proof & Timestamp are used to calculate **Target value ( hash )** in real Blockchain.*
- - -

## Blocks of code

```
class Blockchain:
    def __init__(self) -> None:
        ....
```
*Whenever an object of Block is instantiated , an **Gensis block** ( First block ) will be created to kick start the chain.*


```
class Blockchain:
    def get_prev_block(self) -> dict:
    ....
```
*Function used to get the **previous block** data .*



```
class Blockchain:
    def to_digest(self, new_proof: int, prev_proof: int, index: int, data: str) -> bytes:
    ....
```
*Function used to implement a **mathamatical equation** for calulating different hashes.*

```
class Blockchain:
    def proof_of_work(self, prev_proof: int, index: int, data: str) -> int:
    ....
```
*Function used to generate **new proof** value when Target value is satisfied.*

```
class Blockchain:
    def mine_block(self, data: str) -> dict:
    ....
```
*Function used to **mine a new transaction** & create new block to chain.*

```
class Blockchain:
    def _create_block(self, data: str, proof: int, previous_hash: str, index: int) -> dict:
    ....
```
*Function used to **create a new Block**.*

```
class Blockchain:
    def is_chain_valid(self) -> bool:
    ....
```
*Check the **validity of chain** by computing hashes from genesisi block to last block.*
- - -

## What is FastAPI ?

*FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.*

[More about FastAPI](https://fastapi.tiangolo.com/)

```
FastAPI app:
    @app.post("/mine_block/")
    ....
```
*API used to mine a block .Requires data input from user.*

```
FastAPI app:
    @app.get("/blockchain/")
    ....
```
*API used to access whole blockchain in network.*

```
FastAPI app:
    @app.get("/validity/")
    ....
```
*API used to check the validity of Blockchain in network.*

```
FastAPI app:
    @app.get("/prev_block/")
    ....
```
*API used to access prev block.*

- - -

## Requirements :

```
pip install "fastapi[all]" ipython
```

```
pip install -r requirements.txt
```

*To host FastAPI server :*

```
uvicorn main:app --reload
```

*To access FastAPI server :*

```
http://localhost:8000/docs
```
- - -

## FastAPI Example :

![This is a alt text.](/sample1.png "This is a sample image.")

- - -

## Summary

> This is a simple implementation of a Blockchain using python . Hope you learned something interesting from it .

- - -


"""
Genesis Block :
{
    index:0,
    timestamp:current time,
    data:"i am first block",
    proof:3,
    previous_hash:"0",
} --> hash --> 637hhaa 

Next Block :
{
    index:1,
    timestamp:current time,
    data:"i am second block",
    proof:233,
    previous_hash:"637hhaa",
} --> hash --> whdfk88 

Next Block :
{
    index:2,
    timestamp:current time,
    data:"i am second block",
    proof:24533,
    previous_hash:"whdfk88",
} --> hash --> kksl89 

"""

import datetime as _dt
import hashlib as _hashlib
from hmac import digest
import json as _json

from numpy import block


class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        # create the first block
        genesis_block = self._create_block(
            data="i am first block", proof=1, previous_hash="0", index=1
        )
        # add block to chain
        self.chain.append(genesis_block)

    def mine_block(self, data: str) -> dict:
        # get latest block
        prev_block = self.get_prev_block()
        prev_proof = prev_block["proof"]
        index = len(self.chain) + 1
        proof = self.proof_of_work(prev_proof=prev_proof, index=index, data=data)
        prev_hash = self.create_hash(prev_block)
        new_block = self._create_block(
            data=data, proof=proof, previous_hash=prev_hash, index=index
        )
        self.chain.append(new_block)
        return new_block

    def create_hash(self, block: dict) -> str:
        """
        Create a hash of block provided.
        """
        encoded_hash = _json.dumps(block, sort_keys=True).encode()
        return _hashlib.sha256(encoded_hash).hexdigest()

    def to_digest(
        self, new_proof: int, prev_proof: int, index: int, data: str
    ) -> bytes:
        # can define any maths equation , must be complex & ?secret
        _digest = str(new_proof**3 - prev_proof**2 + index) + data
        return _digest.encode()

    def proof_of_work(self, prev_proof: int, index: int, data: str) -> int:
        new_proof = 1
        check_proof = False

        while not check_proof:
            # create a mathamatical problem here
            to_digest = self.to_digest(
                new_proof=new_proof, prev_proof=prev_proof, index=index, data=data
            )
            hash_value = _hashlib.sha256(to_digest).hexdigest()

            if (
                hash_value[:4] == "0000"
            ):  # here if we increase index , lets say 6 or 8 , it will take more time to compute the required result
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def get_prev_block(self) -> dict:
        return self.chain[-1]

    def _create_block(
        self, data: str, proof: int, previous_hash: str, index: int
    ) -> dict:
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "data": data,
            "proof": proof,
            "previous_hash": previous_hash,
        }
        return block

    def is_chain_valid(self) -> bool:
        current_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            next_block = self.chain[block_index]

            if next_block["previous_hash"] != self.create_hash(current_block):
                return False

            current_proof = current_block["proof"]
            next_index, next_data, next_proof = (
                next_block["index"],
                next_block["data"],
                next_block["proof"],
            )

            hash_val = _hashlib.sha256(
                self.to_digest(
                    new_proof=next_proof,
                    prev_proof=current_proof,
                    index=next_index,
                    data=next_data,
                )
            ).hexdigest()

            if hash_val[:4] != "0000":
                return False

            current_block = next_block
            block_index += 1
        return True


# b = Blockchain()


# print(b.mine_block("hiiii"))
# print(b.mine_block("helloo"))
# print(b.is_chain_valid())

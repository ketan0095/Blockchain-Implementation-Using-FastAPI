import fastapi as _fastapi
import blockchain as _blockchain

BC = _blockchain.Blockchain()
app = _fastapi.FastAPI()

# to mine block
@app.post("/mine_block/")
def mine_block(data: str):
    if not BC.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The blockchain is invalid !"
        )

    block = BC.mine_block(data=data)
    return block


# return entire blockchain
@app.get("/blockchain/")
def get_block():
    if not BC.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The blockchain is invalid !"
        )
    return BC.chain


# check if chain is valid
@app.get("/validity/")
def check_val():
    return BC.is_chain_valid()


# return previos block
@app.get("/prev_block/")
def prev_block():
    if not BC.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The blockchain is invalid !"
        )
    return BC.get_prev_block()

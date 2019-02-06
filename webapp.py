# Creating a Web App
app = Flask(name)

# Creating a Blockchain
blockchain = Blockchain()

@app.route('/')
def hello_world():
    return 'Welcome To Blockchain Practical Demonstration'

# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Block Is Mined',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/print_chain', methods = ['GET'])
def print_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/check_blockchain', methods = ['GET'])
def check_blockchain():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'The Blockchain is Right.'}
    else:
        response = {'message': 'The Blockchain is not Right.'}
    return jsonify(response), 200


app.run(host = '0.0.0.0', port = 5000)
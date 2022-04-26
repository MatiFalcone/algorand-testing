import json
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))


def first_nft_example(private_key, my_address):
    # Connect to node
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    # Get account information
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

    # Build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE

    try:
        unsigned_txn = transaction.AssetConfigTxn(
            sender=my_address,
            sp=params,
            total=1000000000000,
            default_frozen = False,
            unit_name = "SEED",
            asset_name = "Parsl Seed Token",
            manager = "",
            reserve = "",
            freeze = "",
            clawback = "",
            url = "https://shorturl.at/fvPS6",
            metadata_hash = bytes.fromhex("1c99542617d9ce928712b53a34f1608cb0dcc33750d4667fa97eed57b14197a7"),
            strict_empty_address_check=False,
            decimals = 2)
    except Exception as err:
        print(err)
        return

    # Sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # Submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')))
    print("Fee: {} microAlgos".format(params.fee))

    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")


first_nft_example("Bvfv4aN37SJ+MLA+FGRPxdRwToUYOP1A7qP0koCelx0h8sxddp/K106y0Ovn8gMfhKGsaQdXN9nZ+qBAejERkg==", "EHZMYXLWT7FNOTVS2DV6P4QDD6CKDLDJA5LTPWOZ7KQEA6RRCGJJSLPEDM")

# My address: EHZMYXLWT7FNOTVS2DV6P4QDD6CKDLDJA5LTPWOZ7KQEA6RRCGJJSLPEDM
# My private key: Bvfv4aN37SJ+MLA+FGRPxdRwToUYOP1A7qP0koCelx0h8sxddp/K106y0Ovn8gMfhKGsaQdXN9nZ+qBAejERkg==
# My passphrase: this save valley kick sustain master loop rabbit march motion police era ticket fatal service day cabbage ribbon faint consider abuse tray uncover abandon pig
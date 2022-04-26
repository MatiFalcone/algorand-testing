import json
import os
import base64
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))


def first_transaction_example(private_key, my_address):
    # Connect to node
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    # Get account information
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")
    zero_address = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ"

    # Build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE

    metadata = {
        "Status": "1",
        "Metric": {
            "MetricType": "2",
            "UnitOfMeasure": "2",
            "Value": "1.0"
        },
        "TagId": "31390",
        "SerialCode": "123",
        "GrowthPhaseId": "7",
        "PlantBatchId": "13",
        "Room": {
            "Id": "207",
            "Name": "varsha_hands on test_Room1",
            "Description": "edit 1 test",
            "Facility": {
                "Id": "100",
                "Name": "varsha_hands on test facility 3",
                "Description": "Pune India",
                "Type": "null",
                "CompanyId": "47",
                "Address": {
                    "StreetAddress": "Indian Hut Rd",
                    "City": "MORADABAD",
                    "State": "UTTAR PRADESH",
                    "ZipCode": "244001",
                    "Country": "India"
                },
                "FacilityLicense": {
                    "LicenseType": "two wheeler",
                    "LicenseNumber": "VK1111",
                    "IssuedOn": "2020-10-06T00:00:00",
                    "Expiry": "2021-01-14T00:00:00"
                },
            },
        },
        "CompanyId": "47",
        "MotheringPlantId": "null",
        "MotheringPlantSource": "null",
        "ExternalMotheringPlantText": "null",
        "Version": "1",
        "UserProfileId": "1280",
        "UserId": "1280",
        "Id": "00024ce4-e581-47b0-8bce-21857db2f131",
        "AggregateRootId": "1680df47-670b-4177-8c12-e5fe54eb23a7",
        "CommandId": "4b9223cb-bb9e-4c65-a53c-c18507d61562",
    }

    output = json.dumps(metadata)

    with open("test.json", "w") as outfile:
        outfile.write(output)

    print("Actual size: " + str(os.path.getsize("test.json") / 1024) + "KB")

    unsigned_txn = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata))

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
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')))
    print("Fee: {} microAlgos".format(params.fee))

    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

first_transaction_example("Bvfv4aN37SJ+MLA+FGRPxdRwToUYOP1A7qP0koCelx0h8sxddp/K106y0Ovn8gMfhKGsaQdXN9nZ+qBAejERkg==", "EHZMYXLWT7FNOTVS2DV6P4QDD6CKDLDJA5LTPWOZ7KQEA6RRCGJJSLPEDM")

# My address: EHZMYXLWT7FNOTVS2DV6P4QDD6CKDLDJA5LTPWOZ7KQEA6RRCGJJSLPEDM
# My private key: Bvfv4aN37SJ+MLA+FGRPxdRwToUYOP1A7qP0koCelx0h8sxddp/K106y0Ovn8gMfhKGsaQdXN9nZ+qBAejERkg==
# My passphrase: this save valley kick sustain master loop rabbit march motion police era ticket fatal service day cabbage ribbon faint consider abuse tray uncover abandon pig

# My participation address: HJWE5XR6MXXEMXBDAWLGDFQOEPA4XK6QASYY4RNKTIMAMRIR5XHRE7OWVY
# My participation key: play cigar express remember warrior double young ostrich select amused apple purpose trip diagram accident online dad admit excite canoe mom balcony grid abandon permit
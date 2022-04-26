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


def group_transaction_example(private_key, my_address):
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

    metadata1 = {
        "Status": "10",
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

    metadata2 = {
        "Status": "20",
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

    metadata3 = {
        "Status": "30",
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

    metadata4 = {
        "Status": "40",
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

    metadata5 = {
        "Status": "50",
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

    metadata6 = {
        "Status": "60",
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

    metadata7 = {
        "Status": "70",
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

    metadata8 = {
        "Status": "80",
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

    metadata9 = {
        "Status": "90",
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

    metadata10 = {
        "Status": "100",
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

    metadata11 = {
        "Status": "101",
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

    metadata12 = {
        "Status": "102",
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

    metadata13 = {
        "Status": "103",
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

    metadata14 = {
        "Status": "104",
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

    metadata15 = {
        "Status": "105",
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

    metadata16 = {
        "Status": "106",
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

    unsigned_txn1 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata1))
    unsigned_txn2 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata2))
    unsigned_txn3 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata3))
    unsigned_txn4 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata4))
    unsigned_txn5 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata5))
    unsigned_txn6 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata6))
    unsigned_txn7 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata7))
    unsigned_txn8 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata8))
    unsigned_txn9 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata9))
    unsigned_txn10 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata10))
    unsigned_txn11 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata11))
    unsigned_txn12 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata12))
    unsigned_txn13 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata13))
    unsigned_txn14 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata14))
    unsigned_txn15 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata15))
    unsigned_txn16 = transaction.PaymentTxn(my_address, params, zero_address, 0, None, json.dumps(metadata16))

    # Get group id
    gid = transaction.calculate_group_id([
        unsigned_txn1,
        unsigned_txn2,
        unsigned_txn3,
        unsigned_txn4,
        unsigned_txn5,
        unsigned_txn6,
        unsigned_txn7,
        unsigned_txn8,
        unsigned_txn9,
        unsigned_txn10,
        unsigned_txn11,
        unsigned_txn12,
        unsigned_txn13,
        unsigned_txn14,
        unsigned_txn15,
        unsigned_txn16
    ])

    # Assign it to transactions
    unsigned_txn1.group = gid
    unsigned_txn2.group = gid
    unsigned_txn3.group = gid
    unsigned_txn4.group = gid
    unsigned_txn5.group = gid
    unsigned_txn6.group = gid
    unsigned_txn7.group = gid
    unsigned_txn8.group = gid
    unsigned_txn9.group = gid
    unsigned_txn10.group = gid
    unsigned_txn11.group = gid
    unsigned_txn12.group = gid
    unsigned_txn13.group = gid
    unsigned_txn14.group = gid
    unsigned_txn15.group = gid
    unsigned_txn16.group = gid

    # Sign transactions
    signed_txn1 = unsigned_txn1.sign(private_key)
    signed_txn2 = unsigned_txn2.sign(private_key)
    signed_txn3 = unsigned_txn3.sign(private_key)
    signed_txn4 = unsigned_txn4.sign(private_key)
    signed_txn5 = unsigned_txn5.sign(private_key)
    signed_txn6 = unsigned_txn6.sign(private_key)
    signed_txn7 = unsigned_txn7.sign(private_key)
    signed_txn8 = unsigned_txn8.sign(private_key)
    signed_txn9 = unsigned_txn9.sign(private_key)
    signed_txn10 = unsigned_txn10.sign(private_key)
    signed_txn11 = unsigned_txn11.sign(private_key)
    signed_txn12 = unsigned_txn12.sign(private_key)
    signed_txn13 = unsigned_txn13.sign(private_key)
    signed_txn14 = unsigned_txn14.sign(private_key)
    signed_txn15 = unsigned_txn15.sign(private_key)
    signed_txn16 = unsigned_txn16.sign(private_key)

    # Assemble transaction group
    signed_group = [
        signed_txn1,
        signed_txn2,
        signed_txn3,
        signed_txn4,
        signed_txn5,
        signed_txn6,
        signed_txn7,
        signed_txn8,
        signed_txn9,
        signed_txn10,
        signed_txn11,
        signed_txn12,
        signed_txn13,
        signed_txn14,
        signed_txn15,
        signed_txn16
    ]

    # Send transaction group
    tx_id = algod_client.send_transactions(signed_group)

    # wait for confirmation
    confirmed_txn = transaction.wait_for_confirmation(algod_client, tx_id, 4)

    print("txID: {}".format(tx_id), " confirmed in round: {}".format(confirmed_txn.get("confirmed-round", 0)))


group_transaction_example("Bvfv4aN37SJ+MLA+FGRPxdRwToUYOP1A7qP0koCelx0h8sxddp/K106y0Ovn8gMfhKGsaQdXN9nZ+qBAejERkg==", "EHZMYXLWT7FNOTVS2DV6P4QDD6CKDLDJA5LTPWOZ7KQEA6RRCGJJSLPEDM")

# My address: EHZMYXLWT7FNOTVS2DV6P4QDD6CKDLDJA5LTPWOZ7KQEA6RRCGJJSLPEDM
# My private key: Bvfv4aN37SJ+MLA+FGRPxdRwToUYOP1A7qP0koCelx0h8sxddp/K106y0Ovn8gMfhKGsaQdXN9nZ+qBAejERkg==
# My passphrase: this save valley kick sustain master loop rabbit march motion police era ticket fatal service day cabbage ribbon faint consider abuse tray uncover abandon pig

# My participation address: HJWE5XR6MXXEMXBDAWLGDFQOEPA4XK6QASYY4RNKTIMAMRIR5XHRE7OWVY
# My participation key: play cigar express remember warrior double young ostrich select amused apple purpose trip diagram accident online dad admit excite canoe mom balcony grid abandon permit
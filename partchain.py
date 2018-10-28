"""
                                                                                                                                             
8 888888888o      .8.          8 888888888o. 8888888 8888888888 ,o888888o.    8 8888        8          .8.           8 8888 b.             8 
8 8888    `88.   .888.         8 8888    `88.      8 8888      8888     `88.  8 8888        8         .888.          8 8888 888o.          8 
8 8888     `88  :88888.        8 8888     `88      8 8888   ,8 8888       `8. 8 8888        8        :88888.         8 8888 Y88888o.       8 
8 8888     ,88 . `88888.       8 8888     ,88      8 8888   88 8888           8 8888        8       . `88888.        8 8888 .`Y888888o.    8 
8 8888.   ,88'.8. `88888.      8 8888.   ,88'      8 8888   88 8888           8 8888        8      .8. `88888.       8 8888 8o. `Y888888o. 8 
8 888888888P'.8`8. `88888.     8 888888888P'       8 8888   88 8888           8 8888        8     .8`8. `88888.      8 8888 8`Y8o. `Y88888o8 
8 8888      .8' `8. `88888.    8 8888`8b           8 8888   88 8888           8 8888888888888    .8' `8. `88888.     8 8888 8   `Y8o. `Y8888 
8 8888     .8'   `8. `88888.   8 8888 `8b.         8 8888   `8 8888       .8' 8 8888        8   .8'   `8. `88888.    8 8888 8      `Y8o. `Y8 
8 8888    .888888888. `88888.  8 8888   `8b.       8 8888      8888     ,88'  8 8888        8  .888888888. `88888.   8 8888 8         `Y8o.` 
8 8888   .8'       `8. `88888. 8 8888     `88.     8 8888       `8888888P'    8 8888        8 .8'       `8. `88888.  8 8888 8            `Yo 

Testing:

neo> build partchain.py test 0710 05 True False False registerpart ["1234567890","Radar","Wavelength: 10.71 cm , Peak transmit power: 500 kW (250 kW horizontal, 250 kW vertical) , Pulse duration: 0.72 microseconds , Minimum detectable signal: -108 dBm", "2018-10-27", "10 years", "New", "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]

RegisterPart(serial_number, part_name, tech_spec, manufacture_date, lifespan, current_status, owner)

Importing:

> import contract partchain.avm  0710 05 True False False

Using:
neo> testinvoke 0x2df618fb7d04f69a4d3f8c9da33982fbb5c80e4a  registerpart ["1234567890","Radar","Wavelength: 10.71 cm , Peak transmit power: 500 kW (250 kW horizontal, 250 kW vertical) , Pulse duration: 0.72 microseconds , Minimum detectable signal: -108 dBm", "2018-10-27", "10 years", "New", "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]

"""
from boa.builtins import concat
from boa.interop.Neo.Action import RegisterAction
from boa.interop.Neo.App import DynamicAppCall
from boa.interop.Neo.Blockchain import GetContract
from boa.interop.Neo.Iterator import Iterator
from boa.interop.Neo.Runtime import (CheckWitness, GetTrigger, Log,
                                     Notify, Serialize)
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete, Find
from boa.interop.Neo.TriggerType import Application, Verification
from boa.interop.System.ExecutionEngine import (GetCallingScriptHash,
                                                GetEntryScriptHash,
                                                GetExecutingScriptHash)
import json


TOKEN_CONTRACT_OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'
TOKEN_NAME = 'Non-Fungible Token Template'
TOKEN_SYMBOL = 'NFT'
TOKEN_CIRC_KEY = b'in_circulation'

# Smart Contract Event Notifications
OnApprove = RegisterAction('approve', 'addr_from', 'addr_to', 'amount')
OnNFTApprove = RegisterAction('NFTapprove', 'addr_from', 'addr_to', 'tokenid')
OnTransfer = RegisterAction('transfer', 'addr_from', 'addr_to', 'amount')
OnNFTTransfer = RegisterAction('NFTtransfer', 'addr_from', 'addr_to', 'tokenid')
OnMint = RegisterAction('mint', 'addr_to', 'amount')
OnNFTMint = RegisterAction('NFTmint', 'addr_to', 'tokenid')

# common errors
ARG_ERROR = 'incorrect arg length'
INVALID_ADDRESS_ERROR = 'invalid address'
PERMISSION_ERROR = 'incorrect permission'
TOKEN_DNE_ERROR = 'token does not exist'


# datastructure
#  _   _           _       ______                           _   _       _
# | \ | |         | |     |  ____|                         (_) | |     | |         
# |  \| |   ___   | |_    | |__     _   _   _ __     __ _   _  | |__   | |   ___   
# | . ` |  / _ \  | __|   |  __|   | | | | | '_ \   / _` | | | | '_ \  | |  / _ \  
# | |\  | | (_) | | |_    | |      | |_| | | | | | | (_| | | | | |_) | | | |  __/  
# |_| \_|  \___/   \__|   |_|       \__,_| |_| |_|  \__, | |_| |_.__/  |_|  \___|  
#                                                    __/ |                         
#  _______           _                              |___/   _   ______   _______   
# |__   __|         | |                                | \ | | |  ____| |__   __|  
#    | |      ___   | | __   ___   _ __      ______    |  \| | | |__       | |     
#    | |     / _ \  | |/ /  / _ \ | '_ \    |______|   | . ` | |  __|      | |     
#    | |    | (_) | |   <  |  __/ | | | |              | |\  | | |         | |     
#    |_|     \___/  |_|\_\  \___| |_| |_|              |_| \_| |_|         |_|     
#                                                                                  
                                                                                  
manufacture_data_json = { 
    "Manufacture_name": "",
    "Serial_number": "", 
    "Part_name": "",
    "TechSpec": "",
    "Certified_by": "",
    "Manufacture_date": "",
    "Lifespan": "", # Hours of flight, Km, 
    "blockchain_address": "" # This will contain the Fungible Token adress
}

# The follow data will be added in the Fungible Token 
#  ______                           _   _       _            _______           _                   
# |  ____|                         (_) | |     | |          |__   __|         | |                  
# | |__     _   _   _ __     __ _   _  | |__   | |   ___       | |      ___   | | __   ___   _ __  
# |  __|   | | | | | '_ \   / _` | | | | '_ \  | |  / _ \      | |     / _ \  | |/ /  / _ \ | '_ \ 
# | |      | |_| | | | | | | (_| | | | | |_) | | | |  __/      | |    | (_) | |   <  |  __/ | | | |
# |_|       \__,_| |_| |_|  \__, | |_| |_.__/  |_|  \___|      |_|     \___/  |_|\_\  \___| |_| |_|
#                            __/ |                                                                 
#                           |___/                                                                 

history_data_json = {
    "Current_status": "New / Certified / Uncertified / Implemented / Refurbished / Out of order", 
    "Repair_history": { "Repair_company": "", "Status": "Ok/Failure", "ID_technician": "", "Current_usage": "Km, hours" },
                        "Ownerhip_history": { Owner: "Boing", Aircraft_ID: "2312321386213" }
                    }


def Main(operation, args):
    nargs = len(args)
    if nargs == 0:
        print("No domain name supplied")
        return 0

    ctx = GetContext()

    if operation == 'query':
        domain_name = args[0]
        return QueryDomain(domain_name)

    elif operation == 'delete':
        domain_name = args[0]
        return DeleteDomain(domain_name)

#    # Administrative operations
#    elif CheckWitness(TOKEN_CONTRACT_OWNER):
#        if operation == 'mintToken':
#            if len(args) >= 3:
#                return mint_nft_token(ctx, args)
#
#            Notify(ARG_ERROR)
#            return False

    elif operation == 'registerpart':
        if nargs < 7:
            print("required arguments: Manufacture_name Serial_number Part_name TechSpec Manufacture_date Lifespan Owner")
            return 0
        manufacture_name = args[0]
        serial_number = args[1]
        part_name = args[2]
        tech_spec = args[3]
        manufacture_date = args[4]
        lifespan = args[5]
        owner = args[6]

        return registerpart(manufacture_name, serial_number, part_name, tech_spec, manufacture_date, lifespan, owner)

    elif operation == 'registerpart_nft':
        if nargs < 7:
            print("required arguments: Manufacture_name Serial_number Part_name TechSpec Manufacture_date Lifespan Owner")
            return 0
        manufacture_name = args[0]
        serial_number = args[1]
        part_name = args[2]
        tech_spec = args[3]
        manufacture_date = args[4]
        lifespan = args[5]
        owner = args[6]

        return registerpart_nft(manufacture_name, serial_number, part_name, tech_spec, manufacture_date, lifespan, owner)

    elif operation == 'certification':
        if nargs < 7:
            print("required arguments: Serial_number Part_name TechSpec Manufacture_date Lifespan Current_status Owner")
            return 0
        serial_number = args[0]
        part_name = args[1]
        tech_spec = args[2]
        manufacture_date = args[3]
        lifespan = args[4]
        current_status = args[5]
        owner = args[6]

        return registerpart(serial_number, part_name, tech_spec, manufacture_date, lifespan, current_status)

    elif operation == 'transfer':
        if nargs < 3:
            print("required arguments: [serial_number] [part_name] [to_address]")
            return 0
        serial_number = args[0]
        part_name = args[0]
        to_address = args[1]
        return TransferDomain(domain_name, to_address)


def registerpart(manufacture_name, serial_number, part_name, tech_spec, manufacture_date, lifespan, current_status):
    """ The manufacture will register the new component
    """
    msg = concat("Manufacture_name: ", manufacture_name)
    msg = concat("Part_name: ", part_name)
    msg = concat("Tech_spec: ", tech_spec)
    msg = concat("Manufacture_date: ", manufacture_date)
    msg = concat("Lifespan: ", lifespan)
    msg = concat("Current_status: ", current_status)

    print(msg)
    Notify(msg)
    # Put data in a Key/Value datastore

    context = GetContext()

    Put(context, serial_number, msg)
    return True


def registerpart_nft(manufacture_name, serial_number, part_name, tech_spec, manufacture_date, lifespan, current_status):
    """ The manufacture will register the new component with NFT
    """
    msg = concat("Manufacture_name: ", manufacture_name)
    msg = concat("Part_name: ", part_name)
    msg = concat("Tech_spec: ", tech_spec)
    msg = concat("Manufacture_date: ", manufacture_date)
    msg = concat("Lifespan: ", lifespan)
    msg = concat("Current_status: ", current_status)

    print(msg)
    Notify(msg)
    # Put data in a Key/Value datastore

    context = GetContext()

    Put(context, serial_number, msg)
    return True


def mint_nft_token(ctx, args):
    """Mints a new NFT token; stores it's properties, URI info, and
    owner on the blockchain; updates the totalSupply

    :param StorageContext ctx: current store context
    :param list args:
        0: byte[] t_owner: token owner
        1: byte[] t_properties: manufacture_data_json
        2: extra_arg (optional): extra arg to be passed to a smart
            contract
    :return: mint success
    :rtype: bool

    build partchain.py test 0710 05 True False False mint_nft_token ["AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y", '{"Manufacture_name": "ROLLSROYCE", "Part_name": "Radar", "Serial_number":"1234567890"}']
    """

    details = json.loads(args[1])

    t_id = Get(ctx, TOKEN_CIRC_KEY)
    # the int 0 is represented as b'' in neo-boa, this caused bugs
    # throughout my code
    # This is the reason why token id's start at 1 instead
    t_id += 1

    # this should never already exist
    if len(Get(ctx, t_id)) == 20:
        Notify('token already exists')
        return False

    t_owner = args[0]
    if len(t_owner) != 20:
        Notify(INVALID_ADDRESS_ERROR)
        return False

    t_properties = args[1]
    if len(t_properties) == b'\x00':
        Notify('missing properties data string')
        return False

    t_uri = details['Manufacture_name'] + "_" + details['Part_name'] + "_" + details['Serial_number']
    print(t_uri)

    if GetContract(t_owner):
        contract_args = [t_owner, t_id]
        if len(args) == 3:  # append optional extra arg
            contract_args.append(args[2])

        success = transfer_to_smart_contract(ctx, GetExecutingScriptHash(), contract_args, True)
        if success is False:
            return False

    Put(ctx, t_id, t_owner)  # update token's owner
    Put(ctx, concat('properties/', t_id), t_properties)
    Put(ctx, concat('uri/', t_id), t_uri)
    add_token_to_owners_list(ctx, t_owner, t_id)
    Put(ctx, TOKEN_CIRC_KEY, t_id)  # update total supply

    # Log this minting event
    OnMint(t_owner, 1)
    OnNFTMint(t_owner, t_id)
    return True


def QueryDomain(domain_name):
    msg = concat("QueryDomain: ", domain_name)
    Notify(msg)

    context = GetContext()
    owner = Get(context, domain_name)
    if not owner:
        Notify("Domain is not yet registered")
        return False

    Notify(owner)
    return owner


def TransferDomain(domain_name, to_address):
    msg = concat("TransferDomain: ", domain_name)
    Notify(msg)

    context = GetContext()
    owner = Get(context, domain_name)
    if not owner:
        Notify("Domain is not yet registered")
        return False

    if not CheckWitness(owner):
        Notify("Sender is not the owner, cannot transfer")
        return False

    if not len(to_address) != 34:
        Notify("Invalid new owner address. Must be exactly 34 characters")
        return False

    Put(context, domain_name, to_address)
    return True


def DeleteDomain(domain_name):
    msg = concat("DeleteDomain: ", domain_name)
    Notify(msg)

    context = GetContext()
    owner = Get(context, domain_name)
    if not owner:
        Notify("Domain is not yet registered")
        return False

    if not CheckWitness(owner):
        Notify("Sender is not the owner, cannot transfer")
        return False

    Delete(context, domain_name)
    return True


def transfer_to_smart_contract(ctx, t_from, args, is_mint):
    """Transfers a token to a smart contract and triggers the
    receiving contract's onNFTTransfer event.

    :param StorageContext ctx: current store context
    :param byte[] t_from: transfer from address (who is sending the NFT)
    :param list args:
        0: byte[] t_to: transfer to address (who is receiving the NFT)
        1: bytes t_id: token id
        2: extra_arg (optional)
    :param bool is_mint: whether or not the token is being minted
    :return: transfer success
    :rtype: bool
    """
    t_to = args[0]
    t_id = args[1]

    if len(t_from) != 20 or len(t_to) != 20:
        Notify(INVALID_ADDRESS_ERROR)
        return False

    # invoke the onNFTTransfer operation of the recipient contract,
    # if it returns False, then reject the transfer
    success = DynamicAppCall(t_to, 'onNFTTransfer', args)

    if success is False:
        Notify('transfer rejected by recipient contract')
        return False

    # need to check funds again in case a transfer or approval
    # change happened inside the onTokenTransfer call
    # the `is_mint` check is needed because you can't get the token

    # owner for a token that hasn't finished being minted yet
    if is_mint is False:
        t_owner = Get(ctx, t_id)
        if t_owner != t_from:
            Notify('insufficient funds')
            return False

    Log('transfer accepted by recipient contract')
    return True


def add_token_to_owners_list(ctx, t_owner, t_id):
    """Adds a token to the owner's list of tokens

    :param StorageContext ctx: current store context
    :param byte[] t_owner: token owner (could be either a smart
        contract or a wallet address)
    :param bytes t_id: token ID
    :return: successfully added token to owner's list
    :rtype: bool
    """
    length = Get(ctx, t_owner)  # number of tokens the owner has
    Put(ctx, concat(t_owner, t_id), t_id)  # store owner's new token
    length += 1  # increment the owner's balance
    Put(ctx, t_owner, length)  # store owner's new balance
    Log("added token to owner's list and incremented owner's balance")
    return True

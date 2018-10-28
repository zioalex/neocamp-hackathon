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



## datastructure
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
                                                                                  
manufacture_data_json = {   "Serial_number": "", 
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

    if operation == 'query':
        domain_name = args[0]
        return QueryDomain(domain_name)

    elif operation == 'delete':
        domain_name = args[0]
        return DeleteDomain(domain_name)

    elif operation == 'registerpart':
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

        return registerpart(serial_number, part_name, tech_spec, manufacture_date, lifespan, current_status, owner)
    
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


def registerpart(serial_number, part_name, tech_spec, manufacture_date, lifespan, current_status):
    """ The manufacture will register the new component
    """
    msg = concat("Part_name: ", part_name)
    msg = concat("Tech_spec: ", tech_spec)
    msg = concat("Manufacture_date: ", manufacture_date)
    msg = concat("Lifespan: ", lifespan)
    msg = concat("Current_status: ", current_status)

    Notify(msg)
    # Put data in a Key/Value datastore

#    if not CheckWitness(owner):
#        Notify("Owner argument is not the same as the sender")
#        return False

    context = GetContext()
#    exists = Get(context, domain_name)
#    if exists:
#        Notify("Domain is already registered")
#        return False

    Put(context, serial_number, msg)
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

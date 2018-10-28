#!/home/asurace/VirtualEnvs/blockchain/bin/python3.6
"""
Testing:

neo> build 4-domain.py test 0710 05 True False query ["test.com"]
neo> build 4-domain.py test 0710 05 True False register ["test.com","AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]
neo> build 4-domain.py test 0710 05 True False delete ["test.com"]
neo> build 4-domain.py test 0710 05 True False transfer ["test.com","AK2nJJpJr6o664CWJKi1QRXjqeic"]

build 4-domain.py test 0710 05 True False False register ["test.com","AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]
build partchain.py test 0710 05 True False False registerpart ["1234567890","Radar","Wavelength: 10.71 cm , Peak transmit power: 500 kW (250 kW horizontal, 250 kW vertical) , Pulse duration: 0.72 microseconds , Minimum detectable signal: -108 dBm", "2018-10-27", "10 years", "New", "AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]

RegisterPart(serial_number, part_name, tech_spec, manufacture_date, lifespan, current_status, owner)

Importing:

neo> import contract 4-domain.avm 0710 05 True False False
neo> contract search ...

import contract partchain.avm  0710 05 True False False

Using:

neo> testinvoke 5030694901a527908ab0a1494670109e7b85e3e4 query ["test.com"]
neo> testinvoke 5030694901a527908ab0a1494670109e7b85e3e4 register ["test.com","AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"]
neo> testinvoke 5030694901a527908ab0a1494670109e7b85e3e4 delete ["test.com"]
neo> testinvoke 5030694901a527908ab0a1494670109e7b85e3e4 transfer ["test.com","AZ9Bmz6qmboZ4ry1z8p2KF3ftyA2ckJAym"]
"""
from boa.interop.Neo.Runtime import Log, Notify
from boa.interop.Neo.Storage import Get, Put, GetContext
from boa.interop.Neo.Runtime import GetTrigger,CheckWitness
from boa.builtins import concat



## datastructure

manufacture_data_json = {   "Serial_number": "", 
                            "Part_name": "",
                            "TechSpec": "",
                            "Certified_by": "",
                            "Manufacture_date": "",
                            "Lifespan": "", # Hours of flight, Km, 
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

# neocamp-hackathon
https://www.eventbrite.de/e/neo-camp-neo-blockchain-hackathon-tickets-49932369060

# Requirements
    python > 3.6

# Useful
* https://github.com/CityOfZion/neo-python
* [Start a local NEO blockchain with a single command](https://github.com/CityOfZion/neo-local)
* [Neo Collection Resources](https://github.com/CityOfZion/awesome-neo)
* [neo-privatenet Docker method](https://github.com/CityOfZion/neo-privatenet-docker)
* [neo-gui for windows](https://github.com/neo-project/neo-gui.git)
* [TestNet Neo scanner](https://neoscan-testnet.io)
* [Neo-boa compiler is a tool for compiling Python files to the .avm](https://github.com/CityOfZion/neo-boa)
* [NEO Smart Contracts (Python) Tutorial by Dean van Dugteren at NEO Amsterdam](https://www.youtube.com/watch?v=yLPEsst_SVw)

# Get ready
    conda update --prefix /home/$USER/anaconda3 anaconda
    conda update python
    mkvirtualenv -p python3.6 blockchain
    pip install neo-python
    np-bootstrap # Download the testnet chain

## Docker alternatives
    docker pull cityofzion/neo-privatenet
    docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp cityofzion/neo-privatenet


    docker exec -it neo-privatenet /bin/bash
    rm -rf /root/.neopython/Chains/privnet/
    neopy
    create wallet privnet1
    pw: neocamp2018
    import wif KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr
    open wallet privnet1
    pw: neocamp2018
    build ./neosense.py
    import contract ./neosense.avm 8172 01 True False False

        Contract Version] > 01
    [Contract Author] > Alex
    [Contract Email] > alex@myemail.com
    [Contract Description] >
    Creating smart contract....
                     Name: Test contract name
                  Version: 01
                   Author: Alex
                    Email: alex@myemail.com
              Description:
            Needs Storage: True
     Needs Dynamic Invoke: False
               Is Payable: False
    {
        "hash": "0x20e01f4299ba22b1d151a7ec6c15eb2034e26ae2",
        "script": "013ac56b6a00527ac46a51527ac46a51c300c36a52527ac46a52c368184e656f2e52756e74696d652e436865636b5769746e657373616a53527ac46a53c36327000e4e6f7420417574686f72697a6564680f4e656f2e52756e74696d652e4c6f67006c7566610a417574686f72697a6564680f4e656f2e52756e74696d652e4c6f676a51c351c36a54527ac46a52c36a54c37e6a55527ac46a51c3c053876448001a4c6963656e736520666f7220646966666572656e742075736572680f4e656f2e52756e74696d652e4c6f676a51c352c36a56527ac46a56c36a54c37e6a57527ac4623400610e4c6963656e736520666f72206d65680f4e656f2e52756e74696d652e4c6f676a52c36a56527ac46a55c36a57527ac4616a00c3009e649b036a00c30f526567697374657250726f647563748764b9000f526567697374657250726f64756374680f4e656f2e52756e74696d652e4c6f6768164e656f2e53746f726167652e476574436f6e74657874616a54c37c680f4e656f2e53746f726167652e476574616a58527ac46a58c3635e0068164e656f2e53746f726167652e476574436f6e74657874616a54c36a52c35272680f4e656f2e53746f726167652e507574611250726f647563742052656769737465726564680f4e656f2e52756e74696d652e4c6f67516c7566616a00c30e4c6963656e736550726f64756374876485000e4c6963656e736550726f64756374680f4e656f2e52756e74696d652e4c6f676a54c3659602645c0068164e656f2e53746f726167652e476574436f6e74657874616a57c36a56c35272680f4e656f2e53746f726167652e507574611050726f64756374204c6963656e736564680f4e656f2e52756e74696d652e4c6f67516c7566616a00c30f5472616e736665724c6963656e736587643e0168164e656f2e53746f726167652e476574436f6e74657874616a55c37c680f4e656f2e53746f726167652e476574616a59527ac46a59c36404010e4c6963656e736520657869737473680f4e656f2e52756e74696d652e4c6f676a59c368184e656f2e52756e74696d652e436865636b5769746e657373616a5a527ac46a5ac364bb001555736572206973204c6963656e7365204f776e6572680f4e656f2e52756e74696d652e4c6f676a51c352c36a5b527ac46a5bc36a54c37e6a5c527ac468164e656f2e53746f726167652e476574436f6e74657874616a55c37c68124e656f2e53746f726167652e44656c657465616a5cc36a5bc3527268164e656f2e53746f726167652e476574436f6e7465787461124c6963656e7365205472616e736665726564680f4e656f2e52756e74696d652e4c6f67516c7566616a00c30d52656d6f76654c6963656e7365876458006a54c365cb00644f006a51c352c36a5d527ac46a5dc36a54c37e6a5e527ac468164e656f2e53746f726167652e476574436f6e74657874616a5ec37c68124e656f2e53746f726167652e44656c65746561516c7566616a00c30a4765744c6963656e736587645f000a4765744c6963656e7365680f4e656f2e52756e74696d652e4c6f6768164e656f2e53746f726167652e476574436f6e74657874616a57c37c680f4e656f2e53746f726167652e476574616a59527ac46a59c36409006a59c36c756661006c756661006c756659c56b6a00527ac417416d2049207468652070726f64756374206f776e65723f680f4e656f2e52756e74696d652e4c6f6768164e656f2e53746f726167652e476574436f6e74657874616a00c37c680f4e656f2e53746f726167652e476574616a51527ac46a51c368184e656f2e52756e74696d652e436865636b5769746e657373616a52527ac46a52c3632b00164e6f74207468652070726f64756374206f776e657221680f4e656f2e52756e74696d652e4c6f67616a52c36c75665ec56b6a00527ac46a51527ac46a51c36a00c3946a52527ac46a52c3c56a53527ac4006a54527ac46a00c36a55527ac461616a00c36a51c39f6433006a54c36a55c3936a56527ac46a56c36a53c36a54c37bc46a54c351936a54527ac46a55c36a54c3936a00527ac462c8ff6161616a53c36c7566",
        "parameters": "8172",
        "returntype": 1
    }
    Used 500.0 Gas


    -------------------------------------------------------------------------------------------------------------------------------------
    Test deploy invoke successful
    Total operations executed: 11
    Results:
    [<neo.Core.State.ContractState.ContractState object at 0x7f5ddd736a58>]
    Deploy Invoke TX GAS cost: 490.0
    Deploy Invoke TX Fee: 0.0
    -------------------------------------------------------------------------------------------------------------------------------------

    Enter your password to continue and deploy this contract
    [password]> ***********
    [I 181024 22:38:42 Transaction:617] Verifying transaction: b'c8cf5e1c0ab02199846b271a3c101e4e98412165bf1cc440de2d79e5ba043004'
    Relayed Tx: c8cf5e1c0ab02199846b271a3c101e4e98412165bf1cc440de2d79e5ba043004
  
    # Contract details
    contract 0x20e01f4299ba22b1d151a7ec6c15eb2034e26ae2 



# Neo operations
    np-prompt
      state

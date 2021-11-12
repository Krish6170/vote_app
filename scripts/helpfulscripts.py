from brownie import network,accounts,config,interface
import yaml
import json
import os
import shutil

local=["mainnet-fork-dev","Ganache-CLI","ganache-cli-test","development"]


def getAccounts(id=None,index=0):
    if id:
        return accounts.load(id)
    if (network.show_active() in local):
        if index:
            return accounts[index]
        
        return accounts[0]    
    else:
        return accounts.add(config["wallets"]["from_key"][index])



def update_front_end():
    # Send the build folder
    copy_folders_to_front_end("./build", "./front-end/src/chain-info")

    # Sending the front end our config in JSON format
    with open("brownie-config.yaml", "r") as brownie_config:
        config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
        with open("./front-end/src/brownie-config.json", "w") as brownie_config_json:
            json.dump(config_dict, brownie_config_json)
    print("Front end updated!")


def copy_folders_to_front_end(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


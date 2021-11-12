from brownie import Vote,test_try
from scripts.helpfulscripts import getAccounts
from scripts.helpfulscripts import update_front_end

def deploys(frontend_update=True):
    account=getAccounts()
    Vote.deploy({"from":account})
    if(frontend_update):
        update_front_end()
    print("deployed")



def test(): 
    acc=getAccounts()
    Vote[-1].addCandidate("bjp",{"from":acc}) 
    Vote[-1].addCandidate("cpim",{"from":acc})
    Vote[-1].addVoter(getAccounts(index=0),{"from":acc})
    Vote[-1].addVoter(getAccounts(index=1),{"from":acc})
    Vote[-1].addVoter(getAccounts(index=2),{"from":acc})
    Vote[-1].addVoter(getAccounts(index=3),{"from":acc})
    Vote[-1].startVote(120,{"from":acc})



    Vote[-1].voteCandidate(0,{"from":getAccounts(index=0)})
    Vote[-1].voteCandidate(0,{"from":getAccounts(index=1)})
    Vote[-1].voteCandidate(0,{"from":getAccounts(index=2)})
    Vote[-1].voteCandidate(1,{"from":getAccounts(index=3)})


    print("winner")
    
    print(Vote[-1].getCandidateArray({"from":acc}))
    print(Vote[-1].total_voters({"from":acc}))

def test2():
    acc=getAccounts()
    Vote[-1].addCandidate("bjp",{"from":acc}) 
    Vote[-1].addCandidate("cpim",{"from":acc})
    Vote[-1].addVoter(getAccounts(index=0),{"from":acc})
    Vote[-1].addVoter(getAccounts(index=1),{"from":acc})
    Vote[-1].addVoter(getAccounts(index=2),{"from":acc})
    Vote[-1].addVoter(getAccounts(index=3),{"from":acc})
    Vote[-1].startVote(600,{"from":acc})
    print("done set up")


def deploy_test():
    acc=getAccounts(index=2)
    v=test_try.deploy({"from":acc})
    print(v.win({"from":acc}))
    tx=v.Increase({"from":acc})
    tx.wait(1)
    print(v.win({"from":acc}))



def main():
    deploys()
    test2()
    # deploy_test()

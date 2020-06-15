from pprint import pprint
from urllib import parse
def test_ooo():
    data = "agentId=8142f6027ad344e49e9e7cc63f34dbef&authentBankPhone=18791076614&cityCode=610116&authentBankCard=64646&operatorTel=%E6%98%AF&preApprovedLoanAmount=4557676&agentName=%E8%B1%86%E7%AB%8B%E8%88%AA&lenderIdcardAddress=656767667&easyBuyId=eec425377e61497fa21ea1e0e641f466&maritalStatus=1"
    data = parse.unquote(data)
    datas = data.split("&")
    dict1 = {}
    for data in datas:
        key = data.split("=")[0]
        value = data.split("=")[1]
        dict1[key] = value
    print()
    pprint(dict1)
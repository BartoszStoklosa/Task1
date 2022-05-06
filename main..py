import urllib.request, json
from urllib.request import Request, urlopen
from urllib.error import HTTPError

class Seller:
    def __init__(self, seller_id, name, domain, seller_type, deph, above_seller = None):
        self.deph = deph
        self.seller_id = seller_id
        self.name = name
        self.domain = domain
        self.seller_type = seller_type
        self.above_seller = above_seller
        self.list_of_direct_sellers = []
        self.list_of_indirect_sellers = []

    def insert_direct_seller(self, seller):
        if seller not in self.list_of_direct_sellers:
            self.list_of_direct_sellers.append(seller)

    def insert_indirect_seller(self, seller):
        if seller not in self.list_of_indirect_sellers:
            self.list_of_indirect_sellers.append(seller)

    def __eq__(self, other):
        if isinstance(other, str):
            if self.name == other:
                return True
        elif self.name == other.name:
            return True
        return False

    def __str__(self):
        return self.name

def get_sellers_from_json(domain, above_seller, list_of_all_sellers):
    req = Request(domain, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        webpage = urlopen(req).read()
        try:
            data = json.loads(webpage.decode())
            for el in data["sellers"]:
                seller = Seller(el['seller_id'], el['name'], el['domain'], el['seller_type'], above_seller.deph + 1, above_seller)
                if el['seller_type'] == "PUBLISHER":
                    above_seller.insert_direct_seller(seller)
                    if seller not in list_of_all_sellers:
                        list_of_all_sellers.append(seller)
                if el['seller_type'] == "BOTH" or el['seller_type'] == "INTERMEDIARY":
                    above_seller.insert_inderect_seller(seller)
                    url_ = "https://" + el['domain'] + "/sellers.json"
                    if seller not in list_of_all_sellers:
                        list_of_all_sellers.append(seller)
                        get_sellers_from_json(url_, seller, list_of_all_sellers)
        except:
            None
    except HTTPError as err:
        if err.code == 404:
            None
        else:
            raise ValueError("HTTPError")

def find_seller_by_name(list_of_all_sellers, seller):
    elem_id = None
    for id_, el in enumerate(list_of_all_sellers):
        if el == seller:
            elem_id = id_
            break
    if elem_id is None:
        print("not found")
        return None
    return list_of_all_sellers[elem_id]

def find_max_deph_and_its_id(list_of_all_sellers):
    max_deph = 0
    id_of_max_deph = 0
    for id_, el in enumerate(list_of_all_sellers):
        if el.deph > max_deph:
            max_deph = el.deph
            id_of_max_deph = id_
    return max_deph, id_of_max_deph

def find_supply_chain(list_of_all_sellers, seller_name):
    if isinstance(seller_name, str):
        seller = find_seller_by_name(list_of_all_sellers, seller_name)
    else:
        seller = seller_name
    supply_chain = []
    while seller is not None:
        supply_chain.append(seller)
        seller = seller.above_seller
    supply_chain.reverse()
    return supply_chain

def main():
    domain = "openx.com"
    url_ = "https://" + domain + "/sellers.json"
    head_seller = Seller(0, "OpenX", "openx.com", "INTERMEDIARY", 0)
    list_of_all_sellers = [head_seller]
    get_sellers_from_json(url_, head_seller, list_of_all_sellers)


if __name__ == "__main__":
    main()
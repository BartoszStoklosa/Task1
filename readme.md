**Taks1**

Script that will help to present Supply Chain for OpenX by allowing to represent chain of under sellers of chosen Company and define it as direct or indirect.

**How to use script**

All sellers are represented by class Seller with parameters:


**Seller(seller_id, name_domain, seller_type, deph, above_seller)**

     Seller_id = ID of seller (str)
 
     Name_domain = Name of domain (str)

    Seller_type = Type of seller (“Publisher”, “both”, Intermediary”) type(str)

    Deph = represents how deep seller is places (how many sellers are above him) (int)

    above_seller = a seller that is above in supply chain.
  
  

When user runs script all sellers will append in variable “list_of_all_sellers”.

**Warning**

Script avoid all http addresses that caused problem Error 404 and other.

Direct sellers will append in “head_seller.list_of_direct_sellers” and all indirect sellers in “head_seller.list_of_indirect_sellers”.

**“find_seller_by_name”**

Parameters:

    Seller – name of seller

Return:

    object seller with name “seller”

**“find_max_deph_and_its_id”**

Parameters:

    “list_of_all_sellers” – list of sellers

Return:

    number of steps done inside and id of deepest placed seller in “list_of_all_sellers”.

**”find_supply_chain”**

Parameters:

    “list_of_all_sellers” – list of sellers

    Seller_name  - name of seller (str) or seller (obs class Seller)

Return:

    List of sellers from top to seler_name

from typing import NamedTuple, List, Union

# pip install py-money : https://pypi.org/project/py-money/
#from money.money import Money # type: ignore


class Item_Struct(NamedTuple):
    item_ID: str
    item_name: str
    list_price: 'Money'
    
class Bill_Entry(NamedTuple):
    item : Item_Struct
    quantity: int
    tax_percents: List[Union[int, float]]
    net_price: 'Money'

class Payment_Info_Struct(NamedTuple):
    source: str # bank name / account number
    method: str # netbanking / check / cash 
    platform: str # PC / Phone / Retail
    location: str # Home / Office / Retail / Other
    
class Bill_Struct(NamedTuple):
    bill_ID: str
    bill_date: str
    entries: List[Bill_Entry]
    payment_info: Payment_Info_Struct
    
class Item:
    """
    <summary> Each item is one product with its base price, taxes, discounts, given_final_price </summary>
    """
    def __init__(self, item_name = None, base = 0, taxes = [], given_item_final_price = 0):
        self.list_price = base
        self.item_name = item_name
        # a list of additive tax rates
        self.tax_percents = taxes
        self.given_final_price = given_item_final_price

    @staticmethod
    def static_create_item(item_ID: str, item_name: str, list_price: Money):
        return Item_Struct(
            item_ID = item_ID,
            item_name = item_name,
            list_price = list_price
            )

    def calc_final_price(self):
        #  step 1: calculate taxed amounts for each tax in self.taxes using basics.n_percentage_x(n,x)
        return self.list_price + sum(
            (basics.n_percentage_of_x(tax_percent, self.list_price) for tax_percent in self.tax_percents)
            )

class Bill:
        
    def __init__(self, *args, **kwargs):
        self.bill_data : Bill_Struct = None
        if "bill_data" in kwargs.keys():
            if isinstance(kwargs["bill_data"], Bill_Struct):
                self.bill_data = kwargs["bill_data"]
            else:
                pass
    
    def add_entries(self, **kwargs):
        # kwargs: 
        #   item: Item_Struct
        #   items_list: List[Item_Struct]
        #   bill_ID: str
        if self.bill_data == None :
            if ("bill_ID", "item", "bill_date") in kwargs.keys():
                self.bill_data = Bill_Struct(
                    bill_ID = kwargs["bill_ID"],
                    bill_date = kwargs["bill_date"],
                    entries = [kwargs["item"]],
                    payment_info = None
                    )
        else:
            # create a entry
            entry = Bill_Entry(
                item = kwargs["item"], 
                quantity = kwargs["quantity"],
                tax_percents = kwargs["tax_percents"],
                total_price = kwargs["total_price"]
                )
            # 
            self.bill_data.entries.append(entry)
            
                
        #self.bill_data.item_list.append(item)
    
    @staticmethod
    def static_create_bill(bill_ID: str, bill_date: str, entries: List[Bill_Entry]):
        return Bill_Struct(
            bill_ID = bill_ID,
            bill_date = bill_date,
            entries = entries,
            payment_info = None
            )
        
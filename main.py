#from lib.Bills import Bills_Commons
from lib import Bills
#import lib.math_extras
#import nodeLib

if True:
    bill = Bills.bills_commons2.Bill.create_bill(
        bill_node_ID = { 'ID': 00, 'node_name': 'bill'},
        bill_data = {}
    )
    Bills.bills_commons2.Bill.describe_bill(bill, 'compact')
    Bills.bills_commons2.Bill.add_entry(
        bill_= bill, 
        entry_data= {
            
        }
        )
    
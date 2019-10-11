from typing import NamedTuple, List, Union

import nodeLib

"""
Bill contains all the details it can
Bill entries are also entries to 

"""
class Bill:
    
    @staticmethod
    def create_bill(bill_node_ID, bill_data):
        bill_ = nodeLib.node.Node_Manager.create_node(
            node_ID = bill_node_ID,
            data = bill_data
        )
        nodeLib.node.Node_Manager.create_related_node(
            from_node = bill_,
            node_ID = { 
                       'ID' : bill_.node_ID.ID+1,
                       'node_name' : 'entries'
            },
            rel_from_to_to = 'member',
            rel_to_to_from = 'group'
        )
        return bill_
    
    @staticmethod
    def add_entry(bill_, entry_data):
        first_entry = True if nodeLib.node.Node_Manager.get_rel_node(bill_, [0]) else False
    
    @staticmethod
    def describe_bill(bill_, mode):
        nodeLib.debug.Debug_Node.describe(bill_, mode)
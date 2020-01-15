from typing import NamedTuple, List, Union

import nodeLib
from nodeLib import structure

"""
Bill contains all the details it can
Bill entries are also entries to 

"""
# todo create default cluster
class report:
    """
    
    TODO 
        properties - 
    
    Returns:
        [type] -- [description]
    """
    @staticmethod
    def create_report():
        report_ = nodeLib.cluster.create_cluster('report')
        return report_
    
    @staticmethod
    def add_entry(report_:structure.node_structs.NodeClusterStruct, entry_data: dict):
        report_.nodes.add(
            nodeLib.node.create_node(
                node_ID = {'node_name' : 'entry'},
                data = entry_data,
            )
        )
    @staticmethod
    def describe_report(report_ : nodeLib.structure.node_structs.NodeStruct, mode=None):
        #assert report_.node_ID.node_name == 'bill'
        print()
        #nodeLib.node.Node_Manager.describe(report_, mode)
        #nodeLib.node.Node_Manager.describe(nodeLib.node.Node_Manager.get_rel_node(report_, nodeID_deep=[{'ID':1},{'ID':0}]), mode)
        # does the bill have any entries?
        
        #for relation_claim in report_.relation_claims[0].to_node.relation_claims[2::2]:
        #    nodeLib.node.Node_Manager.describe(relation_claim.to_node, mode)
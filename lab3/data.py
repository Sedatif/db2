from controller.Neo4jController import Neo4jController
from controller.Controller import Controller, Tags
from servers.neo4j_server.Neo4jServer import Neo4jServer

menu_list = {
    'Neo4j menu': {
        'Find all users that sent or received messages with a set of tags.(6.1)': Neo4jController.get_users_with_tagged_messages,
        'Find all pairs of connected users length N through sent or received messages(6.2)': Neo4jController.get_users_with_n_long_relations,
        'Find on the graph the shortest path between users through sent or received messages.(6.3)': Neo4jController.shortest_way_between_users,
        'Find authors of messages that are only related to each other messages marked as spam(6.4)': Neo4jController.get_users_wicth_have_only_spam_conversation,
        'Find all users that sent or received messages with a set of tags, but these users are not connected.(6.5)': Neo4jController.get_unrelated_users_with_tagged_messages,
        'Exit': Controller.stop_loop,
    }
}

roles = {
    'utilizer': 'Utilizer menu',
    'admin': 'Admin menu'
}

neo4j = Neo4jServer()
special_parameters = {
    'role': '(admin or utilizer)',
    'tags': '('+', '.join(x.name for x in list(Tags))+')(Enter comma-separated values)',
    'username1': '(' + ', '.join(x for x in neo4j.get_users()) + ')',
    'username2': '(' + ', '.join(x for x in neo4j.get_users()) + ')'
}
import networkx as nx
import matplotlib.pyplot as plt
import time
import vk

session = vk.Session(access_token='e265afa8e265afa8e265afa808e200e113ee265e265afa8b936e5e4ed11ff63210c0601')
api = vk.API(session)

# создаем пустой граф
G = nx.Graph()

# выбираем группу
members = api.friends.get(user_id='13163380', fields='domain', v=5.74)

# каждого участника добавляем в граф
for member in members['items']:
    G.add_node(member['domain'], label='{} {}'.format(member['first_name'], member['last_name']))



for member in members['items']:
    try:
        print("current user: {} {}".format(member['first_name'], member['last_name']))
        # TODO: получить список друзей
        friends = None

        for friend in friends['items']:
            # если друг есть в графе - добавить связь
            if G.has_node(friend):
                # TODO: добавить ребро в граф
                pass

        time.sleep(0.2)
    except Exception as e:
        print(e)

# сохраняем в файле
nx.write_gexf(G, 'friends.gexf')

# рисуем
pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50) 
nx.draw_networkx_edges(G, pos, edge_color='green')
nx.draw_networkx_labels(G, pos, font_size=11, font_family='Arial')
plt.axis('off')
plt.show()

{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"mount_file_id":"1U1lb5J8c2kjpArgU-rMncRsxq65enRtC","authorship_tag":"ABX9TyNUM5E9vCiVtkHnVDmNZyN3"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":1,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"FPspV6zt1gp3","executionInfo":{"status":"ok","timestamp":1741791108769,"user_tz":-420,"elapsed":10,"user":{"displayName":"Mochamad Risyad Fauzan","userId":"10143685887636129384"}},"outputId":"05ff748b-302e-4b35-edbc-b8dbba830975"},"outputs":[{"output_type":"stream","name":"stdout","text":["Simpul tujuan ditemukan!\n","Jalur yang ditemukan: S → A → C → G\n","Total biaya jalur: 10\n"]},{"output_type":"execute_result","data":{"text/plain":["True"]},"metadata":{},"execution_count":1}],"source":["from queue import PriorityQueue\n","\n","def a_star_graph_search(graph, start, goal, heuristic):\n","    frontier = PriorityQueue()\n","    frontier.put((0, start))  # (f(n), node)\n","\n","    came_from = {}  # Menyimpan jalur terpendek\n","    cost_so_far = {start: 0}  # Menyimpan biaya g(n)\n","    explored = set()  # Simpan simpul yang sudah dieksplorasi\n","\n","    while not frontier.empty():\n","        current_cost, current_node = frontier.get()  # Ambil simpul dengan f(n) terendah\n","\n","        if current_node in explored:\n","            continue  # Lewati jika sudah dieksplorasi\n","\n","        explored.add(current_node)  # Tandai sebagai dieksplorasi\n","\n","        if current_node == goal:\n","            # Rekonstruksi jalur dari goal ke start\n","            path = []\n","            while current_node:\n","                path.append(current_node)\n","                current_node = came_from.get(current_node, None)\n","            path.reverse()\n","\n","            print(\"Simpul tujuan ditemukan!\")\n","            print(\"Jalur yang ditemukan:\", \" → \".join(path))\n","            print(\"Total biaya jalur:\", cost_so_far[goal])\n","            return True\n","\n","        for neighbor, step_cost in graph[current_node].items():\n","            new_cost = cost_so_far[current_node] + step_cost  # g(n) + biaya langkah\n","\n","            if neighbor not in explored and (neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]):\n","                cost_so_far[neighbor] = new_cost\n","                priority = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)\n","                frontier.put((priority, neighbor))\n","                came_from[neighbor] = current_node  # Simpan jalur\n","\n","    print(\"Simpul tujuan tidak ditemukan!\")\n","    return False\n","\n","# Heuristik (h(n))\n","heuristic = {\n","    'A': 9,\n","    'B': 4,\n","    'C': 2,\n","    'D': 5,\n","    'E': 3,\n","    'S': 7,\n","    'G': 0\n","}\n","\n","# Graph dengan biaya antar simpul (g(n))\n","graph = {\n","    'S': {'A': 3, 'E': 2},\n","    'A': {'B': 3, 'C': 4},\n","    'B': {'D': 5},\n","    'C': {'G': 3},\n","    'D': {'G': 3},\n","    'E': {'D': 6}\n","}\n","\n","start_node = 'S'\n","goal_node = 'G'\n","\n","a_star_graph_search(graph, start_node, goal_node, heuristic)"]}]}
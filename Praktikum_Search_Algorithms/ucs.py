{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"mount_file_id":"1sUHKNwhz84wDc7op0LZpklt2AdCOjY5N","authorship_tag":"ABX9TyMq78jFRMXb2HtUAXeaxQzO"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":1,"metadata":{"id":"FdEomn2-zsvU","executionInfo":{"status":"ok","timestamp":1741790607161,"user_tz":-420,"elapsed":55,"user":{"displayName":"Mochamad Risyad Fauzan","userId":"10143685887636129384"}},"outputId":"89eebcdb-fc76-4f93-bd99-7e44e85663c9","colab":{"base_uri":"https://localhost:8080/"}},"outputs":[{"output_type":"stream","name":"stdout","text":["Minimum cost from 0 to 6 is = 3\n"]}],"source":["def uniform_cost_search(goal, start):\n","    global graph, cost\n","    answer = []\n","    queue = []\n","\n","    for i in range(len(goal)):\n","        answer.append(10**8)\n","\n","    queue.append([0, start])\n","    visited = {}\n","    count = 0\n","\n","    while queue:\n","        queue.sort()\n","        p = queue.pop(0)\n","\n","        if p[1] in goal:\n","            index = goal.index(p[1])\n","            if answer[index] == 10**8:\n","                count += 1\n","            if answer[index] > p[0]:\n","                answer[index] = p[0]\n","\n","            if count == len(goal):\n","                return answer\n","\n","        if p[1] not in visited:\n","            visited[p[1]] = True\n","            for i in range(len(graph[p[1]])):\n","                queue.append([p[0] + cost[(p[1], graph[p[1]][i])], graph[p[1]][i]])\n","\n","    return answer\n","\n","if __name__ == \"__main__\":\n","    graph, cost = [[] for _ in range(8)], {}\n","\n","    graph[0].append(1)\n","    graph[0].append(3)\n","    graph[3].append(1)\n","    graph[3].append(6)\n","    graph[3].append(4)\n","    graph[1].append(6)\n","    graph[4].append(2)\n","    graph[4].append(5)\n","    graph[2].append(1)\n","    graph[5].append(2)\n","    graph[5].append(6)\n","    graph[6].append(4)\n","\n","    # Modifikasi bobot agar minimum cost dari 0 ke 6 adalah 3\n","    cost[(0, 1)] = 2\n","    cost[(0, 3)] = 3  # Ubah dari 5 ke 3\n","    cost[(1, 6)] = 5\n","    cost[(3, 1)] = 5\n","    cost[(3, 6)] = 0  # Ubah dari 6 ke 0\n","    cost[(3, 4)] = 2\n","    cost[(2, 1)] = 4\n","    cost[(4, 2)] = 4\n","    cost[(4, 5)] = 3\n","    cost[(5, 2)] = 6\n","    cost[(5, 6)] = 3\n","    cost[(6, 4)] = 7\n","\n","    goal = [6]\n","    answer = uniform_cost_search(goal, 0)\n","\n","    print(\"Minimum cost from 0 to 6 is =\", answer[0])"]}]}
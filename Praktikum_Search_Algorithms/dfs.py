{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"mount_file_id":"1-OrPNZNJXsLGGgXI_Yf6vRhDwDZBzhoA","authorship_tag":"ABX9TyOlw159YHx+ehmHdJXAK60O"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":4,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"tdxjKBzdvUdC","executionInfo":{"status":"ok","timestamp":1741790077454,"user_tz":-420,"elapsed":55,"user":{"displayName":"Mochamad Risyad Fauzan","userId":"10143685887636129384"}},"outputId":"75189ea7-958f-4cea-cea5-a70546355c30"},"outputs":[{"output_type":"stream","name":"stdout","text":["Berikut adalah jalur DFS dari node 1 ke node 3:\n","[1, 2, 3]\n"]}],"source":["from collections import defaultdict\n","\n","class Graph:\n","    def __init__(self):\n","        self.graph = defaultdict(list)\n","\n","    def addEdge(self, u, v):\n","        self.graph[u].append(v)\n","\n","    def DFSUtil(self, v, visited, path, target):\n","        visited.add(v)\n","        path.append(v)\n","\n","        if v == target:\n","            return True\n","\n","        for neighbour in self.graph[v]:\n","            if neighbour not in visited:\n","                if self.DFSUtil(neighbour, visited, path, target):\n","                    return True\n","\n","        path.pop()\n","        return False\n","\n","    def findPathDFS(self, start, target):\n","        visited = set()\n","        path = []\n","\n","        if self.DFSUtil(start, visited, path, target):\n","            return path\n","        else:\n","            return \"Tidak ada jalur yang ditemukan.\"\n","\n","if __name__ == \"__main__\":\n","    g = Graph()\n","    g.addEdge(0, 1)\n","    g.addEdge(0, 2)\n","    g.addEdge(1, 2)\n","    g.addEdge(2, 0)\n","    g.addEdge(2, 3)\n","    g.addEdge(3, 3)\n","\n","    start_node = 1\n","    target_node = 3\n","\n","    print(f\"Berikut adalah jalur DFS dari node {start_node} ke node {target_node}:\")\n","    print(g.findPathDFS(start_node, target_node))"]}]}
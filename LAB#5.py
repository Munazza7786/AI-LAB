def iterative_deepening_dfs(start, target):
    depth = 1
    bottom_reached = False
    while not bottom_reached:
        result,bottom_reached = iterative_deepening_dfs_rec(start, target, 0, depth)
        if result is not None:
            return result
        depth *= 2
        print("Increasing depth to " + str(depth))
    return None

def iterative_deepening_dfs_rec(node, target, current_depth, max_depth):
    print("Visting Node" + str (node["value"]))

    if node["value"] == target:
        print("Found the node we are looking for!")
        return node, True
    if current_depth == max_depth:
        print("Current maximum depth reached, returing....")
        if len(node["Children"])>0:
            return None, False
        else:
            return None, True

    bottom_reached = True
    for i in range (len(node["Children"])):
        result, bottom_reached_rec = iterative_deepening_dfs_rec(node["Children"][i], target, current_depth + 1,
                                                                 max_depth)
        if result is not None:
            return result, True
        bottom_reached =  bottom_reached and bottom_reached_rec
    return None, bottom_reached
start = {
    "value": 0, "Children" : [
        {"value": 1, "Children" : [
          {"value": 3, "Children" : []},
           {"value": 4, "Children" : []}
          ]},{
              "value": 2, "Children" : [
                  {"value": 5, "Children" : []},
                  {"value": 6, "Children" : []}
                  ]
              }
        ]
}

print(iterative_deepening_dfs(start, 6)["value"])

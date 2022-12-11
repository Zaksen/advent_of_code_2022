file_path = 'inputs/day_8.txt'
with open(file_path, 'r') as f:
    trees = [[x for x in l.rstrip()] for l in f]

def is_visible(height, *args):
    for trees in args:
        if height > max(trees):
            return True
    return False
        
def count_visible_trees(trees):
    nb_visible_trees = 2 * (len(trees) + (len(trees[0]) - 2)) 
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            trees_left = [trees[i][k] for k in range(j)]
            trees_right = [trees[i][k] for k in range(j + 1, len(trees))]
            trees_top = [trees[k][j] for k in range(i)]
            trees_bottom = [trees[k][j] for k in range(i +1, len(trees[0]))]
            if is_visible(trees[i][j], trees_left, trees_top, trees_right, trees_bottom):
                nb_visible_trees += 1
    return nb_visible_trees

print(count_visible_trees(trees))
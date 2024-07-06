def get_all_cell_candidates(grid):
    
    boxes = []
    
    for box_row in range(3):
        for box_col in range(3):
            box_candidates = []
            for i in range(3):
                for j in range(3):
                    row, col = 3 * box_row + i, 3 * box_col + j
                    candidates = get_possible_cell_values(grid, row, col)
                    if candidates:
                        box_candidates.append({
                            'row': row,
                            'col': col,
                            'candidates': candidates
                        })
            
            if box_candidates:
                boxes.append({
                    'box_row': box_row,
                    'box_col': box_col,
                    'candidates': box_candidates
                })
    
    return boxes


def get_possible_cell_values(grid, row, col):
    if grid[row][col] != None:
        return []
    
    possible_values = set(range(1, 10))
    
    # Remove values already present in the same row
    possible_values -= set(grid[row])
    
    # Remove values already present in the same column
    possible_values -= set(grid[i][col] for i in range(9))
    
    # Remove values already present in the same 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            possible_values.discard(grid[i][j])
            
    return list(possible_values)


def get_cell_sole_candidates(grid):
    allCandidates = get_all_cell_candidates(grid)
    
    filteredCandidates = []
    for box in allCandidates:
        box['candidates'] = [cell for cell in box['candidates'] if len(cell['candidates']) == 1] 
        filteredCandidates.append(box) if len(box['candidates']) > 0 else None

    return filteredCandidates




print("hello")
# # Example usage
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

grid = [[ None if cell == 0 else cell for cell in row] for row in grid]
snyder_boxes = get_cell_sole_candidates(grid)

print(snyder_boxes)
# for box in snyder_boxes:
#     print(f"Box ({box['box_row']}, {box['box_col']}):")
#     for candidate in box['candidates']:
#         print(f"  Cell ({candidate['row']}, {candidate['col']}): {candidate['candidates']}")

print("done")

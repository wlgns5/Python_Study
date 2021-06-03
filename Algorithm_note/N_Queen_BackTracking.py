def is_available(candidate, current_col):
    # 현재 행
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True


# current_candidate: 지금 까지 배치된 queen의 정보
def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row +1, current_candidate, final_result)
            current_candidate.pop()
# N x N 체스판
def solve_n_queens(N):
    # 최종 결과
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


print(solve_n_queens(4))
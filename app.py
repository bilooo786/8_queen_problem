import streamlit as st

N = 8

st.title("8-Queens CSP Analyzer")

st.write("""
This tool lets you **place queens manually** and see if the placement satisfies
the **CSP (Constraint Satisfaction Problem) rules**.

Constraints:
1. No two queens in the same column
2. No two queens in the same diagonal
3. One queen per row
""")

# Initialize board
if "board" not in st.session_state:
    st.session_state.board = [-1] * N


# -------- Constraint Checking --------
def check_constraints(board, row, col):

    conflicts = []

    for r in range(N):

        if board[r] == -1:
            continue

        # Column conflict
        if board[r] == col:
            conflicts.append(f"❌ Column conflict with queen in Row {r+1}")

        # Diagonal conflict
        if abs(board[r] - col) == abs(r - row):
            conflicts.append(f"❌ Diagonal conflict with queen in Row {r+1}")

    if conflicts:
        return False, conflicts
    else:
        return True, ["✅ Placement satisfies all CSP constraints"]


# -------- Draw Board --------
def draw_board(board):

    board_display = ""

    for r in range(N):

        for c in range(N):

            if board[r] == c:
                board_display += "♛ "
            else:
                board_display += "⬜ "

        board_display += "\n"

    st.text(board_display)


# -------- Show Board --------
st.subheader("Current Chess Board")
draw_board(st.session_state.board)


# -------- Input Section --------
st.subheader("Enter Queen Position")

col1, col2 = st.columns(2)

with col1:
    row = st.number_input("Row", 1, 8, step=1)

with col2:
    col = st.number_input("Column", 1, 8, step=1)


# -------- Analyze Button --------
if st.button("Analyze Placement"):

    row_index = row - 1
    col_index = col - 1

    valid, messages = check_constraints(st.session_state.board, row_index, col_index)

    for msg in messages:
        if valid:
            st.success(msg)
        else:
            st.error(msg)

    if valid:
        st.session_state.board[row_index] = col_index


# -------- Reset Button --------
if st.button("Reset Board"):
    st.session_state.board = [-1] * N
    st.experimental_rerun()

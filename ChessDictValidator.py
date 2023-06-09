"""Write a function named isValidChessBoard() that takes a dictionary argument and
returns True or False depending on if the board is valid.
A valid board will have exactly one black king and exactly one white king. Each
player can only have at-most 16 pieces, at most 8 pawns and all pieces must be on a
valid space from '1a' to '8h'; that is, a piece can't be on space '9z'. The names
begin with an 'b' or 'w' to represent black or white respectively, followed by 'pawn',
'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug
has resulted in an improper chess board."""

sample_board = {'8h': 'brook', '8g': 'bknight', '8f': 'bbishop', '8e': 'bking',
         '8d': 'wqueen', '8c': 'wbishop', '8b': 'wknight', '8a': 'wrook',
         '7a': 'bpawn', '7b': 'bpawn', '1c': 'bpawn', '1d': 'wking',
         '1e': 'wpawn', '1f': 'wpawn', '1g': 'wpawn', '1h': 'wpawn'}

bb = {}

def isValidChessBoard(board):
  """
  Returns True if the given board is a valid chess board, False otherwise.

  Args:
    board: A dictionary mapping from space to piece.

  Returns:
    True if the board is valid, False otherwise.
  """

  # Check that there is exactly one black king and one white king.
  black_king_count = 0
  white_king_count = 0
  for space, piece in board.items():
    if piece.startswith('b') and piece.endswith('king'):
      black_king_count += 1
    elif piece.startswith("w") and piece.endswith("king"):
      white_king_count += 1

    #print(black_king_count)
  if black_king_count != 1 or white_king_count != 1:
    return "less or excess kings"
    #print("Excess kings")

  # Check that each player has at most 16 pieces and at most 8 pawns.
  for color in ["b", "w"]:
    piece_count = 0
    pawn_count = 0
    for space, piece in board.items():
      if piece.startswith(color):
        piece_count += 1
        if piece.endswith("pawn"):
          pawn_count += 1

    if piece_count > 16 or pawn_count > 8:
      return "more pieces or pawns"

  # Check that all pieces are on valid spaces.
  for space, piece in board.items():
    if not space[1].isalpha() or not space[0].isdigit() or int(space[0]) > 8 or \
            ord(space[1]) > ord('h'):
      return "exceeded board size"
      #print('board range exceeded')

  return True

isValidChessBoard(bb)




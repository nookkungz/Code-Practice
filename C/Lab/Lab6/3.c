int numPieces;
    char board[BOARD_SIZE][BOARD_SIZE];

   
    for (int i = 0; i < BOARD_SIZE; i++) {
        for (int j = 0; j < BOARD_SIZE; j++) {
            board[i][j] = ' ';
        }
    }

    printf("Enter the number of pieces: ");
    if (scanf("%d", &numPieces) != 1) {
        printf("Invalid input for number of pieces.\n");
        return 1;
    }

 
    for (int i = 0; i < numPieces; i++) {
        char piece;
        int x, y;
        printf("Enter piece %d (format: A(x, y)): ", i + 1);
        if (scanf(" %c(%d, %d)", &piece, &x, &y) != 3) {
            printf("Invalid input format. Please use the format A(x, y).\n");
            i--; 
            continue;
        }
        setPieceOnTable(board, piece, x, y);
    }

    // Print the board
    printf("  ");
    for (int i = 0; i < BOARD_SIZE; i++) {
        printf("%d ", i);
    }
    printf("\n");

    for (int i = 0; i < BOARD_SIZE; i++) {
        printf("%d|", i);
        for (int j = 0; j < BOARD_SIZE; j++) {
            printf("%c|", board[i][j]);
        }
        printf("\n");
    }

    return 0;
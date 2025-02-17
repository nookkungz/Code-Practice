void str_extract(char** source, char** vowel)
{
    int len = 0;
    while ( (*source)[len] != '\0' ) {
        len++;
    }

    *vowel = (char*) malloc(sizeof(char)*(len+1));
    if (*vowel == NULL) {
        return;
    }

    int writeSource = 0; 
    int writeVowel  = 0; 

    for(int i = 0; i < len; i++) {
        char c = (*source)[i];
        int isVowel = 0;
        switch(c) {
            case 'a': case 'A':
            case 'e': case 'E':
            case 'i': case 'I':
            case 'o': case 'O':
            case 'u': case 'U':
                isVowel = 1;
                break;
        }

        if (isVowel) {
            (*vowel)[writeVowel++] = c;
        } else {
            (*source)[writeSource++] = c;
        }
    }

    (*source)[writeSource] = '\0';
    (*vowel)[writeVowel]   = '\0';
}
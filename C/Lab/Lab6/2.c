if (n == 0) {
        *golden_ratio = 0; 
        return NULL;
    }

    unsigned long *fib_array = (unsigned long *)malloc(n * sizeof(unsigned long));
    if (!fib_array) {
        printf("Memory allocation failed.\n");
        *golden_ratio = 0;
        return NULL;
    }

    fib_array[0] = 0;
    if (n > 1) {
        fib_array[1] = 1;
        for (unsigned int i = 2; i < n; i++) {
            fib_array[i] = fib_array[i - 1] + fib_array[i - 2];
        }
    }

    if (n > 2) {
        *golden_ratio = (double)fib_array[n - 1] / fib_array[n - 2];
    } else {
        *golden_ratio = 1; 
    }

    return fib_array;
}

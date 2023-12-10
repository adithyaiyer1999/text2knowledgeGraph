THRESHOLD_FOR_ITERATIVE_UPDATE=80000  #This variable states that if the length of characters is less this then we will call normal create graph function,
                                    #if the length of characters is greater than this then will call multithreading iterative update function
MAX_TOKEN_LENGTH=40000 # Max token length we are permitting for chunking a big paragraph
NUMBER_OF_WORKERS=10 # Number of threads you want to create for launching multithreading setup for calling open ai apis in parallel

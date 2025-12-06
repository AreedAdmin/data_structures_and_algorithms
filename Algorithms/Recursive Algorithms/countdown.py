def countdown(n):
    """
    Prints numbers from n down to 1.
    When n is 0, print "Blastoff!" instead of the number.
    
    Example:
    countdown(3)
    # Output:
    # 3
    # 2
    # 1
    # Blastoff!
    """
    # TODO: Write your code here
    print(n)

    if n <= 1:
        return 'Blastoff!'

    return countdown(n-1)

x=countdown(3)
print(x)
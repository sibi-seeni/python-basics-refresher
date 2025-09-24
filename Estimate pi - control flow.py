#   A program to estimate pi
#
#   Pseudocode:
#   1) Display a welcome message
#   2) Get input from the user for no. of decimals of pi
#   3) Initiate a loop and compute the estimated pi
#   4) Compute the error between estimate and pi
#   5) Format and display the result
#
# by: Sibi Seenivasan

def main():
    # display a welcome message
    print("\nWelcome to Pi Calculator!")
    num = float(0.0)
    den = float(0.0)
    summ = float(0.0)

    # Get input
    N = int(input("\nEnter the number of terms (N): "))
    Pi = 3.141592653589793

    # Loop through the Gregor-Leibnitz formula
    for k in range(0, N):
        num = (-1) ** k
        den = (2*k) + 1
        summ += (num/den)
    
    estimate = 4 * summ
    error = round(Pi - estimate, 6)

    # Output
    print(f"\nThe actual value of pi upto 15 digits is:\t{Pi}")
    print(f"The estimated pi with the series is: \t\t{estimate}")
    print(f"The error of the estimation is:\t\t\t{error}")

if __name__ == "__main__":
    main()
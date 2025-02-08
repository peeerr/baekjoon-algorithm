import sys

def main():
    try:
        n = int(sys.stdin.readline().strip())
        numbers = list(map(int, sys.stdin.readline().split()))
        unique_numbers = sorted(set(numbers))
        print(" ".join(map(str, unique_numbers)))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()

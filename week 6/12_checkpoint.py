

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    # reverse list
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

    fruit_list.append("orange")
    print(f"Append orange: {fruit_list}")

    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    pop = fruit_list.pop()
    print(f"popped item: '{pop}' updated list: {fruit_list}")

    fruit_list.sort()
    print(fruit_list)

    fruit_list.clear()
    print(fruit_list)
    

if __name__ == "__main__":
    main()






def main():
    provinces_list = read_provinces("provinces.txt")
    print(provinces_list)
    

def read_provinces(filename):
    text_list = []
    count = 0
    with open(filename, "rt") as provinces_file:
        for line in provinces_file:
            clean_line = line.strip()
            text_list.append(clean_line)
        for i in range(len(text_list)):
            if text_list[i] == "AB":
                text_list[i] = "Alberta"
            if text_list[i] == "Alberta":
                count = count + 1

                

        text_list.pop(0)
        text_list.pop(-1)
    

    
    return text_list, count

if __name__ == "__main__":
    main()
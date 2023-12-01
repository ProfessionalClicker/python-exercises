import re

def main():
    #open file
    input_path = "./human_insulin/preproinsulin-seq.txt"
    output_path = "./human_insulin/preproinsulin-seq-clean.txt"
    with open(input_path, "r") as file:
        text = file.read()
        #find only words of lowercase letters, 1 character or more
        pattern = r"\b[a-z]+"
        matches = re.findall(pattern, text, flags=0)

    #format list of words into a single str
    sequence = "".join(matches)

    #save sequence to file path
    with open(output_path, "w") as file:
        file.write(sequence)
    
    #define character ranges for each insulin type
    lsinsulin_range = range(0, 24, 1)
    binsulin_range = range(24, 54, 1)
    cinsulin_range = range(54, 89, 1)
    ainsulin_range = range(89, 110, 1)


    #lsinsulin
    ls_path = "./human_insulin/lsinsulin-seq-clean.txt"
    with open(ls_path, "w") as file:
        for index in lsinsulin_range:
            file.write(sequence[index])
    
    #binsulin
    b_path = "./human_insulin/binsulin-seq-clean.txt"
    with open(b_path, "w") as file:
        for index in binsulin_range:
            file.write(sequence[index])
    
    #cinsulin
    c_path = "./human_insulin/cinsulin-seq-clean.txt"
    with open(c_path, "w") as file:
        for index in cinsulin_range:
            file.write(sequence[index])
    
    #ainsulin
    a_path = "./human_insulin/ainsulin-seq-clean.txt"
    with open(a_path, "w") as file:
        for index in ainsulin_range:
            file.write(sequence[index])


if __name__ == "__main__":
    main()
def get_course_name(course_no):
    course_list = ["BabyLuigi", "Peach", "Daisy", "Luigi", "Mario", "Yoshi", 
    "Nokonoko", "Patapata", "Waluigi", "Wario", "Diddy", "Donkey", "Koopa", 
    "you shouldn't get this", "Rainbow", "Desert", "Snow"]
    return course_list[course_no - 33]




if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("input",
                        help="Filepath to .gci fie to be converted into .ght")
                        
    args = parser.parse_args()
    
    with open(args.input, "rb") as f:
        f.seek(5251)
        course_id = f.read(1)
        print(course_id)
        course_id = ord(course_id)
        
        output = get_course_name(course_id) + ".ght"
        print(output)
        with open(output, "wb") as o:
            f.seek(5248)
            o.write(f.read())
            f.close()
            o.close()
        #print(course_id)
        
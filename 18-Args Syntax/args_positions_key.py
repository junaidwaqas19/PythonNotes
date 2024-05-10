def animal_names(animal_type,*names,habitate="unknown"):
    animal_list  = ",  ".join(names)
    descriptions =f"The {animal_type} animals in the {habitate} are:"\
                   f"{animal_list}."
    return descriptions 
result = animal_names("gerifie",*['spike','melvin'],habitate='savannah')
print(result)
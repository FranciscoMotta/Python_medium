DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # high order func - lamnda func

    adults = list(filter(lambda worker: worker["age"] > 18 , DATA))

    # MAPS

    adults = list(map(lambda worker: worker["name"], adults))

    # MAPS 2.0

    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    print("PYTHON DEVS")

    for worker in all_python_devs:
        print(worker)

    print("///")
    print("PLATZI WORKERS")
    for worker in all_platzi_workers:
        print(worker)
    print("///")
    print("ADULTS WORKERS")
    for worker in adults:
        print(worker)
    print("///")
    print("OLDS WORKERS")
    for worker in old_people:
        print(worker)
    print("///")
if __name__ == '__main__':
    main()
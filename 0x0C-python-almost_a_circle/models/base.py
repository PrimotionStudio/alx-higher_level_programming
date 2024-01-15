#!/usr/bin/python3
"""
A module with a class
called Base
by Martins Okanlawon
"""
import json
import turtle


class Base:
    """
    A class called Base
    and its contents
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        the init function that
        create an instance of the Base Object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Adding JSON to the Base class
        """

        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save obj to json
        to file
        """

        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string([i.to_dictionary() for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Update the class Base by adding the static method
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Im bored and outta ideas
        """

        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        else:
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """
        I give zero f**k
        """

        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_attr = Base.from_json_string(f.read())
                return [cls.create(**i) for i in list_attr]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This is the most tough opart
        i jsut wanna sleep
        """

        with open(cls.__name__ + ".csv", "w") as f:
            if list_objs is None or list_objs == []:
                f.write("")
            else:
                for i in list_objs:
                    dt = i.to_dictionary()
                    if i.__class__.__name__ == "Rectangle":
                        f.write("{},{},{},{},{}\n".format(dt["id"],
                                                        dt["width"], dt["height"], dt["x"], dt["y"]))
                    elif i.__class__.__name__ == "Square":
                        f.write("{},{},{},{}\n".format(dt["id"],
                                                     dt["size"], dt["x"], dt["y"]))

    @classmethod
    def load_from_file_csv(cls):
        """
        Never mind
        """

        list_objs = []
        with open(cls.__name__ + ".csv", "r") as f:
            csv = f.readlines()
            for i in csv:
                lt = i[:-1].split(',')
                if len(lt) == 5:
                    dt = dict()
                    lst = ['id', 'width', 'height', 'x', 'y']
                    for j in range(len(lt)):
                        dt[lst[j]] = lt[j]
                elif len(lt) == 4:
                    dt = dict()
                    lst = ['id', 'size', 'x', 'y']
                    for j in range(len(lt)):
                        dt[lst[j]] = lt[j]
                list_objs.append(cls.create(**dt))
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        The turtule drawing GUI
        """

        turtle.speed(1)
        turtle.shape("turtle")

        for r in list_rectangles:
            turtle.penup()
            turtle.goto(r.x, r.y)
            turtle.pendown()
            turtle.color("red")
            for _ in range(2):
                turtle.forward(r.width)
                turtle.left(90)
                turtle.forward(r.height)
                turtle.left(90)

        for s in list_squares:
            turtle.penup()
            turtle.goto(s.x, s.y)
            turtle.pendown()
            turtle.color("green")
            for _ in range(4):
                turtle.forward(s.size)
                turtle.left(90)

        turtle.done()

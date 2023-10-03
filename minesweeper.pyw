from tkinter import Tk, Label, PhotoImage, Button
import random
import time


class play(Label):

    playing = True
    select_neighbors = []
    select_count = 0
    index_selection = None
    index_selection_list = []
    bomb_neighbors = []
    bomb_locations = None
    duplicate_bomb_neighbors = []
    select_neighborhood = []
    select_neighborhood1 = []
    select_neighborhood2 = []
    select_neighborhood3 = []
    
    def __init__(self):
        Label.__init__(self)
        self.select = PhotoImage(file='png\\select.png')
        self.explosive = PhotoImage(file='png\\bomb.png')
        self.explosion = PhotoImage(file='png\\explosion.png')
        self.no_neighbor_bomb = PhotoImage(file='png\\empty_mine.png')
        self.number1 = PhotoImage(file='png\\n1.png')
        self.number2 = PhotoImage(file='png\\n2.png')
        self.number3 = PhotoImage(file='png\\n3.png')
        self.number4 = PhotoImage(file='png\\n4.png')
        self.number5 = PhotoImage(file='png\\n5.png')
        self.bomb = lambda:Label(image=self.explosive, borderwidth=0)
        self.bomb_triggered = lambda:Label(image=self.explosion, borderwidth=0)
        self.neighbor0 = lambda:Label(image=self.no_neighbor_bomb, bd=0, background="white")
        self.neighbor1 = lambda:Label(image=self.number1, bd=0, background="white")
        self.neighbor2 = lambda:Label(image=self.number2, bd=0, background="white")
        self.neighbor3 = lambda:Label(image=self.number3, bd=0, background="white")
        self.neighbor4 = lambda:Label(image=self.number4, bd=0, background="white")
        self.neighbor5 = lambda:Label(image=self.number5, bd=0, background="white")
        self.user_choice()
    
    def user_choice(self):

        def click0():
            if self.playing == True:
                self.select_neighbors.extend([1, 5, 6])
                self.select_count += 1
                self.index_selection = 0
                self.index_selection_list.append(0)
                self.results()

        def click1():
            if self.playing == True:
                self.select_neighbors.extend([0, 2, 5, 6, 7])
                self.select_count += 1
                self.index_selection = 1
                self.index_selection_list.append(1)
                self.results()

        def click2():
            if self.playing == True:
                self.select_neighbors.extend([1, 3, 6, 7, 8])
                self.select_count += 1
                self.index_selection = 2
                self.index_selection_list.append(2)
                self.results()

        def click3():
            if self.playing == True:
                self.select_neighbors.extend([2, 4, 7, 8, 9])
                self.select_count += 1
                self.index_selection = 3
                self.index_selection_list.append(3)
                self.results()

        def click4():
            if self.playing == True:
                self.select_neighbors.extend([3, 8, 9])
                self.select_count += 1
                self.index_selection = 4
                self.index_selection_list.append(4)
                self.results()

        def click5():
            if self.playing == True:
                self.select_neighbors.extend([0, 1, 6, 10, 11])
                self.select_count += 1
                self.index_selection = 5
                self.index_selection_list.append(5)
                self.results()

        def click6():
            if self.playing == True:
                self.select_neighbors.extend([0, 1, 2, 5, 7, 10, 11, 12])
                self.select_count += 1
                self.index_selection = 6
                self.index_selection_list.append(6)
                self.results()

        def click7():
            if self.playing == True:
                self.select_neighbors.extend([1, 2, 3, 6, 8, 11, 12, 13])
                self.select_count += 1
                self.index_selection = 7
                self.index_selection_list.append(7)
                self.results()

        def click8():
            if self.playing == True:
                self.select_neighbors.extend([2, 3, 4, 7, 9, 12, 13, 14])
                self.select_count += 1
                self.index_selection = 8
                self.index_selection_list.append(8)
                self.results()

        def click9():
            if self.playing == True:
                self.select_neighbors.extend([3, 4, 8, 13, 14])
                self.select_count += 1
                self.index_selection = 9
                self.index_selection_list.append(9)
                self.results()

        def click10():
            if self.playing == True:
                self.select_neighbors.extend([5, 6, 11, 15, 16])
                self.select_count += 1
                self.index_selection = 10
                self.index_selection_list.append(10)
                self.results()

        def click11():
            if self.playing == True:
                self.select_neighbors.extend([5, 6, 7, 10, 12, 15, 16, 17])
                self.select_count += 1
                self.index_selection = 11
                self.index_selection_list.append(11)
                self.results()

        def click12():
            if self.playing == True:
                self.select_neighbors.extend([6, 7, 8, 11, 13, 16, 17, 18])
                self.select_count += 1
                self.index_selection = 12
                self.index_selection_list.append(12)
                self.results()

        def click13():
            if self.playing == True:
                self.select_neighbors.extend([7, 8, 9, 12, 14, 17, 18, 19])
                self.select_count += 1
                self.index_selection = 13
                self.index_selection_list.append(13)
                self.results()

        def click14():
            if self.playing == True:
                self.select_neighbors.extend([8, 9, 13, 18, 19])
                self.select_count += 1
                self.index_selection = 14
                self.index_selection_list.append(14)
                self.results()

        def click15():
            if self.playing == True:
                self.select_neighbors.extend([10,11, 16, 20, 21])
                self.select_count += 1
                self.index_selection = 15
                self.index_selection_list.append(15)
                self.results()

        def click16():
            if self.playing == True:
                self.select_neighbors.extend([10, 11, 12, 15, 17, 20, 21, 22])
                self.select_count += 1
                self.index_selection = 16
                self.index_selection_list.append(16)
                self.results()

        def click17():
            if self.playing == True:
                self.select_neighbors.extend([11, 12, 13, 16, 18, 21, 22, 23])
                self.select_count += 1
                self.index_selection = 17
                self.index_selection_list.append(17)
                self.results()

        def click18():
            if self.playing == True:
                self.select_neighbors.extend([12, 13, 14, 17, 19, 22, 23, 24])
                self.select_count += 1
                self.index_selection = 18
                self.index_selection_list.append(18)
                self.results()

        def click19():
            if self.playing == True:
                self.select_neighbors.extend([13, 14, 18, 23, 24])
                self.select_count += 1
                self.index_selection_list.append(19)
                self.index_selection = 19
                self.results()

        def click20():
            if self.playing == True:
                self.select_neighbors.extend([15, 16, 21])
                self.select_count += 1
                self.index_selection_list.append(20)
                self.index_selection = 20
                self.results()

        def click21():
            if self.playing == True:
                self.select_neighbors.extend([15, 16, 17, 20, 22])
                self.select_count += 1
                self.index_selection_list.append(21)
                self.index_selection = 21
                self.results()

        def click22():
            if self.playing == True:
                self.select_neighbors.extend([16, 17, 18, 21, 23])
                self.select_count += 1
                self.index_selection_list.append(22)
                self.index_selection = 22
                self.results()

        def click23():
            if self.playing == True:
                self.select_neighbors.extend([17, 18, 19, 22, 24])
                self.select_count += 1
                self.index_selection = 23
                self.index_selection_list.append(23)
                self.results()

        def click24():
            if self.playing == True:
                self.select_neighbors.extend([18, 19, 23])
                self.select_count += 1
                self.index_selection = 24
                self.index_selection_list.append(24)
                self.results()


        choice0 = Button(image=self.select, command=click0, borderwidth=0)
        choice1 = Button(image=self.select, command=click1, borderwidth=0)
        choice2 = Button(image=self.select, command=click2, borderwidth=0)
        choice3 = Button(image=self.select, command=click3, borderwidth=0)
        choice4 = Button(image=self.select, command=click4, borderwidth=0)
        choice5 = Button(image=self.select, command=click5, borderwidth=0)
        choice6 = Button(image=self.select, command=click6, borderwidth=0)
        choice7 = Button(image=self.select, command=click7, borderwidth=0)
        choice8 = Button(image=self.select, command=click8, borderwidth=0)
        choice9 = Button(image=self.select, command=click9, borderwidth=0)
        choice10 = Button(image=self.select, command=click10, borderwidth=0)
        choice11 = Button(image=self.select, command=click11, borderwidth=0)
        choice12 = Button(image=self.select, command=click12, borderwidth=0)
        choice13 = Button(image=self.select, command=click13, borderwidth=0)
        choice14 = Button(image=self.select, command=click14, borderwidth=0)
        choice15 = Button(image=self.select, command=click15, borderwidth=0)
        choice16 = Button(image=self.select, command=click16, borderwidth=0)
        choice17 = Button(image=self.select, command=click17, borderwidth=0)
        choice18 = Button(image=self.select, command=click18, borderwidth=0)
        choice19 = Button(image=self.select, command=click19, borderwidth=0)
        choice20 = Button(image=self.select, command=click20, borderwidth=0)
        choice21 = Button(image=self.select, command=click21, borderwidth=0)
        choice22 = Button(image=self.select, command=click22, borderwidth=0)
        choice23 = Button(image=self.select, command=click23, borderwidth=0)
        choice24 = Button(image=self.select, command=click24, borderwidth=0)

        choice0.place(x=9, y=10)
        choice1.place(x=110, y=10)
        choice2.place(x=211, y=10)
        choice3.place(x=312, y=10)
        choice4.place(x=413, y=10)
        choice5.place(x=9, y=111)
        choice6.place(x=110, y=111)
        choice7.place(x=211, y=111)
        choice8.place(x=312, y=111)
        choice9.place(x=413, y=111)
        choice10.place(x=9, y=212)
        choice11.place(x=110, y=212)
        choice12.place(x=211, y=212)
        choice13.place(x=312, y=212)
        choice14.place(x=413, y=212)
        choice15.place(x=9, y=313)
        choice16.place(x=110, y=313)
        choice17.place(x=211, y=313)
        choice18.place(x=312, y=313)
        choice19.place(x=413, y=313)
        choice20.place(x=9, y=414)
        choice21.place(x=110, y=414)
        choice22.place(x=211, y=414)
        choice23.place(x=312, y=414)
        choice24.place(x=413, y=414)

    def results(self):
        
        if self.select_count == 1:
            self.bomb_locations = random.sample([i for i in range(24) if i != self.index_selection], k=5)
            for x in self.bomb_locations:
                if x == 0:
                    self.bomb_neighbors.extend([1, 5, 6])
                if x == 1:
                    self.bomb_neighbors.extend([0, 2, 5, 6, 7])
                if x == 2:
                    self.bomb_neighbors.extend([1, 3, 6, 7, 8])
                if x == 3:
                    self.bomb_neighbors.extend([2, 4, 7, 8, 9])
                if x == 4:
                    self.bomb_neighbors.extend([3, 8, 9])
                if x == 5:
                    self.bomb_neighbors.extend([0, 1, 6, 10, 11])
                if x == 6:
                    self.bomb_neighbors.extend([0, 1, 2, 5, 7, 10, 11, 12])
                if x == 7:
                    self.bomb_neighbors.extend([1, 2, 3, 6, 8, 11, 12, 13])
                if x == 8:
                    self.bomb_neighbors.extend([2, 3, 4, 7, 9, 12, 13, 14])
                if x == 9:
                    self.bomb_neighbors.extend([3, 4, 8, 13, 14])
                if x == 10:
                    self.bomb_neighbors.extend([5, 6, 11, 15, 16])
                if x == 11:
                    self.bomb_neighbors.extend([5, 6, 7, 10, 12, 15, 16, 17])
                if x == 12:
                    self.bomb_neighbors.extend([6, 7, 8, 11, 13, 16, 17, 18])
                if x == 13:
                    self.bomb_neighbors.extend([7, 8, 9, 12, 14, 17, 18, 19])
                if x == 14:
                    self.bomb_neighbors.extend([8, 9, 13, 18, 19])
                if x == 15:
                    self.bomb_neighbors.extend([10, 11, 16, 20, 21])
                if x == 16:
                    self.bomb_neighbors.extend([10, 11, 12, 15, 17, 20, 21, 22])
                if x == 17:
                    self.bomb_neighbors.extend([11, 12, 13, 16, 18, 21, 22, 23])
                if x == 18:
                    self.bomb_neighbors.extend([12, 13, 14, 17, 19, 22, 23, 24])
                if x == 19:
                    self.bomb_neighbors.extend([13, 14, 18, 23, 24])
                if x == 20:
                    self.bomb_neighbors.extend([15, 16, 21])
                if x == 21:
                    self.bomb_neighbors.extend([15, 16, 17, 20, 22])
                if x == 22:
                    self.bomb_neighbors.extend([16, 17, 18, 21, 23])
                if x == 23:
                    self.bomb_neighbors.extend([17, 18, 19, 22, 24])
                if x == 24:
                    self.bomb_neighbors.extend([18, 19, 23])

            for y in self.bomb_neighbors:
                if (y in self.bomb_locations):
                    self.bomb_neighbors.remove(y)
            for y in self.bomb_neighbors:
                if (y in self.bomb_locations):
                    self.bomb_neighbors.remove(y)

            self.duplicate_bomb_neighbors = dict(set((x, self.bomb_neighbors.count(x)) for x in filter(lambda rec:self.bomb_neighbors.count(rec)>0, self.bomb_neighbors)))

        if self.index_selection in self.bomb_locations:
            if self.index_selection == 0:
                self.bomb().place(x=9, y=10)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 1:
                self.bomb().place(x=110, y=10)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 2:
                self.bomb().place(x=211, y=10)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 3:
                self.bomb().place(x=312, y=10)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 4:
                self.bomb().place(x=413, y=10)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 5:
                self.bomb().place(x=9, y=111)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 6:
                self.bomb().place(x=110, y=111)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 7:
                self.bomb().place(x=211, y=111)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 8:
                self.bomb().place(x=312, y=111)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 9:
                self.bomb().place(x=413, y=111)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 10:
                self.bomb().place(x=9, y=212)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 11:
                self.bomb().place(x=110, y=212)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 12:
                self.bomb().place(x=211, y=212)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 13:
                self.bomb().place(x=312, y=212)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 14:
                self.bomb().place(x=413, y=212)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 15:
                self.bomb().place(x=9, y=313)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 16:
                self.bomb().place(x=110, y=313)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 17:
                self.bomb().place(x=211, y=313)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 18:
                self.bomb().place(x=312, y=313)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 19:
                self.bomb().place(x=413, y=313)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 20:
                self.bomb().place(x=9, y=414)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 21:
                self.bomb().place(x=110, y=414)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 22:
                self.bomb().place(x=211, y=414)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 23:
                self.bomb().place(x=312, y=414)
                self.playing = False
                self.after(500, self.user_lose)
            elif self.index_selection == 24:
                self.bomb().place(x=413, y=414)
                self.playing = False
                self.after(500, self.user_lose)

        elif self.index_selection in self.bomb_neighbors:
            for k, v in self.duplicate_bomb_neighbors.items():
                if k == self.index_selection:
                    if self.index_selection == 0:
                        if v == 1:
                            self.neighbor1().place(x=9, y=10)
                        elif v == 2:
                            self.neighbor2().place(x=9, y=10)
                        elif v == 3:
                            self.neighbor3().place(x=9, y=10)
                        elif v == 4:
                            self.neighbor4().place(x=9, y=10)
                        elif v == 5:
                            self.neighbor5().place(x=9, y=10)
                    elif self.index_selection == 1:
                        if v == 1:
                            self.neighbor1().place(x=110, y=10)
                        elif v == 2:
                            self.neighbor2().place(x=110, y=10)
                        elif v == 3:
                            self.neighbor3().place(x=110, y=10)
                        elif v == 4:
                            self.neighbor4().place(x=110, y=10)
                        elif v == 5:
                            self.neighbor5().place(x=110, y=10)
                    elif self.index_selection == 2:
                        if v == 1:
                            self.neighbor1().place(x=211, y=10)
                        elif v == 2:
                            self.neighbor2().place(x=211, y=10)
                        elif v == 3:
                            self.neighbor3().place(x=211, y=10)
                        elif v == 4:
                            self.neighbor4().place(x=211, y=10)
                        elif v == 5:
                            self.neighbor5().place(x=211, y=10)
                    elif self.index_selection == 3:
                        if v == 1:
                            self.neighbor1().place(x=312, y=10)
                        elif v == 2:
                            self.neighbor2().place(x=312, y=10)
                        elif v == 3:
                            self.neighbor3().place(x=312, y=10)
                        elif v == 4:
                            self.neighbor4().place(x=312, y=10)
                        elif v == 5:
                            self.neighbor5().place(x=312, y=10)
                    elif self.index_selection == 4:
                        if v == 1:
                            self.neighbor1().place(x=413, y=10)
                        elif v == 2:
                            self.neighbor2().place(x=413, y=10)
                        elif v == 3:
                            self.neighbor3().place(x=413, y=10)
                        elif v == 4:
                            self.neighbor4().place(x=413, y=10)
                        elif v == 5:
                            self.neighbor5().place(x=413, y=10)
                    elif self.index_selection == 5:
                        if v == 1:
                            self.neighbor1().place(x=9, y=111)
                        elif v == 2:
                            self.neighbor2().place(x=9, y=111)
                        elif v == 3:
                            self.neighbor3().place(x=9, y=111)
                        elif v == 4:
                            self.neighbor4().place(x=9, y=111)
                        elif v == 5:
                            self.neighbor5().place(x=9, y=111)
                    elif self.index_selection == 6:
                        if v == 1:
                            self.neighbor1().place(x=110, y=111)
                        elif v == 2:
                            self.neighbor2().place(x=110, y=111)
                        elif v == 3:
                            self.neighbor3().place(x=110, y=111)
                        elif v == 4:
                            self.neighbor4().place(x=110, y=111)
                        elif v == 5:
                            self.neighbor5().place(x=110, y=111)
                    elif self.index_selection == 7:
                        if v == 1:
                            self.neighbor1().place(x=211, y=111)
                        elif v == 2:
                            self.neighbor2().place(x=211, y=111)
                        elif v == 3:
                            self.neighbor3().place(x=211, y=111)
                        elif v == 4:
                            self.neighbor4().place(x=211, y=111)
                        elif v == 5:
                            self.neighbor5().place(x=211, y=111)
                    elif self.index_selection == 8:
                        if v == 1:
                            self.neighbor1().place(x=312, y=111)
                        elif v == 2:
                            self.neighbor2().place(x=312, y=111)
                        elif v == 3:
                            self.neighbor3().place(x=312, y=111)
                        elif v == 4:
                            self.neighbor4().place(x=312, y=111)
                        elif v == 5:
                            self.neighbor5().place(x=312, y=111)
                    elif self.index_selection == 9:
                        if v == 1:
                            self.neighbor1().place(x=413, y=111)
                        elif v == 2:
                            self.neighbor2().place(x=413, y=111)
                        elif v == 3:
                            self.neighbor3().place(x=413, y=111)
                        elif v == 4:
                            self.neighbor4().place(x=413, y=111)
                        elif v == 5:
                            self.neighbor5().place(x=413, y=111)
                    elif self.index_selection == 10:
                        if v == 1:
                            self.neighbor1().place(x=9, y=212)
                        elif v == 2:
                            self.neighbor2().place(x=9, y=212)
                        elif v == 3:
                            self.neighbor3().place(x=9, y=212)
                        elif v == 4:
                            self.neighbor4().place(x=9, y=212)
                        elif v == 5:
                            self.neighbor5().place(x=9, y=212)
                    elif self.index_selection == 11:
                        if v == 1:
                            self.neighbor1().place(x=110, y=212)
                        elif v == 2:
                            self.neighbor2().place(x=110, y=212)
                        elif v == 3:
                            self.neighbor3().place(x=110, y=212)
                        elif v == 4:
                            self.neighbor4().place(x=110, y=212)
                        elif v == 5:
                            self.neighbor5().place(x=110, y=212)
                    elif self.index_selection == 12:
                        if v == 1:
                            self.neighbor1().place(x=211, y=212)
                        elif v == 2:
                            self.neighbor2().place(x=211, y=212)
                        elif v == 3:
                            self.neighbor3().place(x=211, y=212)
                        elif v == 4:
                            self.neighbor4().place(x=211, y=212)
                        elif v == 5:
                            self.neighbor5().place(x=211, y=212)
                    elif self.index_selection == 13:
                        if v == 1:
                            self.neighbor1().place(x=312, y=212)
                        elif v == 2:
                            self.neighbor2().place(x=312, y=212)
                        elif v == 3:
                            self.neighbor3().place(x=312, y=212)
                        elif v == 4:
                            self.neighbor4().place(x=312, y=212)
                        elif v == 5:
                            self.neighbor5().place(x=312, y=212)
                    elif self.index_selection == 14:
                        if v == 1:
                            self.neighbor1().place(x=413, y=212)
                        elif v == 2:
                            self.neighbor2().place(x=413, y=212)
                        elif v == 3:
                            self.neighbor3().place(x=413, y=212)
                        elif v == 4:
                            self.neighbor4().place(x=413, y=212)
                        elif v == 5:
                            self.neighbor5().place(x=413, y=212)
                    elif self.index_selection == 15:
                        if v == 1:
                            self.neighbor1().place(x=9, y=313)
                        elif v == 2:
                            self.neighbor2().place(x=9, y=313)
                        elif v == 3:
                            self.neighbor3().place(x=9, y=313)
                        elif v == 4:
                            self.neighbor4().place(x=9, y=313)
                        elif v == 5:
                            self.neighbor5().place(x=9, y=313)
                    elif self.index_selection == 16:
                        if v == 1:
                            self.neighbor1().place(x=110, y=313)
                        elif v == 2:
                            self.neighbor2().place(x=110, y=313)
                        elif v == 3:
                            self.neighbor3().place(x=110, y=313)
                        elif v == 4:
                            self.neighbor4().place(x=110, y=313)
                        elif v == 5:
                            self.neighbor5().place(x=110, y=313)
                    elif self.index_selection == 17:
                        if v == 1:
                            self.neighbor1().place(x=211, y=313)
                        elif v == 2:
                            self.neighbor2().place(x=211, y=313)
                        elif v == 3:
                            self.neighbor3().place(x=211, y=313)
                        elif v == 4:
                            self.neighbor4().place(x=211, y=313)
                        elif v == 5:
                            self.neighbor5().place(x=211, y=313)
                    elif self.index_selection == 18:
                        if v == 1:
                            self.neighbor1().place(x=312, y=313)
                        elif v == 2:
                            self.neighbor2().place(x=312, y=313)
                        elif v == 3:
                            self.neighbor3().place(x=312, y=313)
                        elif v == 4:
                            self.neighbor4().place(x=312, y=313)
                        elif v == 5:
                            self.neighbor5().place(x=312, y=313)
                    elif self.index_selection == 19:
                        if v == 1:
                            self.neighbor1().place(x=413, y=313)
                        elif v == 2:
                            self.neighbor2().place(x=413, y=313)
                        elif v == 3:
                            self.neighbor3().place(x=413, y=313)
                        elif v == 4:
                            self.neighbor4().place(x=413, y=313)
                        elif v == 5:
                            self.neighbor5().place(x=413, y=313)
                    elif self.index_selection == 20:
                        if v == 1:
                            self.neighbor1().place(x=9, y=414)
                        elif v == 2:
                            self.neighbor2().place(x=9, y=414)
                        elif v == 3:
                            self.neighbor3().place(x=9, y=414)
                        elif v == 4:
                            self.neighbor4().place(x=9, y=414)
                        elif v == 5:
                            self.neighbor5().place(x=9, y=414)
                    elif self.index_selection == 21:
                        if v == 1:
                            self.neighbor1().place(x=110, y=414)
                        elif v == 2:
                            self.neighbor2().place(x=110, y=414)
                        elif v == 3:
                            self.neighbor3().place(x=110, y=414)
                        elif v == 4:
                            self.neighbor4().place(x=110, y=414)
                        elif v == 5:
                            self.neighbor5().place(x=110, y=414)
                    elif self.index_selection == 22:
                        if v == 1:
                            self.neighbor1().place(x=211, y=414)
                        elif v == 2:
                            self.neighbor2().place(x=211, y=414)
                        elif v == 3:
                            self.neighbor3().place(x=211, y=414)
                        elif v == 4:
                            self.neighbor4().place(x=211, y=414)
                        elif v == 5:
                            self.neighbor5().place(x=211, y=414)
                    elif self.index_selection == 23:
                        if v == 1:
                            self.neighbor1().place(x=312, y=414)
                        elif v == 2:
                            self.neighbor2().place(x=312, y=414)
                        elif v == 3:
                            self.neighbor3().place(x=312, y=414)
                        elif v == 4:
                            self.neighbor4().place(x=312, y=414)
                        elif v == 5:
                            self.neighbor5().place(x=312, y=414)
                    elif self.index_selection == 24:
                        if v == 1:
                            self.neighbor1().place(x=413, y=414)
                        elif v == 2:
                            self.neighbor2().place(x=413, y=414)
                        elif v == 3:
                            self.neighbor3().place(x=413, y=414)
                        elif v == 4:
                            self.neighbor4().place(x=413, y=414)
                        elif v == 5:
                            self.neighbor5().place(x=413, y=414)

        elif self.index_selection not in self.bomb_neighbors:
            if self.index_selection == 0:
                self.neighbor0().place(x=9, y=10)
            elif self.index_selection == 1:
                self.neighbor0().place(x=110, y=10)
            elif self.index_selection == 2:
                self.neighbor0().place(x=211, y=10)
            elif self.index_selection == 3:
                self.neighbor0().place(x=312, y=10)
            elif self.index_selection == 4:
                self.neighbor0().place(x=413, y=10)
            elif self.index_selection == 5:
                self.neighbor0().place(x=9, y=111)
            elif self.index_selection == 6:
                self.neighbor0().place(x=110, y=111)
            elif self.index_selection == 7:
                self.neighbor0().place(x=211, y=111)
            elif self.index_selection == 8:
                self.neighbor0().place(x=312, y=111)
            elif self.index_selection == 9:
                self.neighbor0().place(x=413, y=111)
            elif self.index_selection == 10:
                self.neighbor0().place(x=9, y=212)
            elif self.index_selection == 11:
                self.neighbor0().place(x=110, y=212)
            elif self.index_selection == 12:
                self.neighbor0().place(x=211, y=212)
            elif self.index_selection == 13:
                self.neighbor0().place(x=312, y=212)
            elif self.index_selection == 14:
                self.neighbor0().place(x=413, y=212)
            elif self.index_selection == 15:
                self.neighbor0().place(x=9, y=313)
            elif self.index_selection == 16:
                self.neighbor0().place(x=110, y=313)
            elif self.index_selection == 17:
                self.neighbor0().place(x=211, y=313)
            elif self.index_selection == 18:
                self.neighbor0().place(x=312, y=313)
            elif self.index_selection == 19:
                self.neighbor0().place(x=413, y=313)
            elif self.index_selection == 20:
                self.neighbor0().place(x=9, y=414)
            elif self.index_selection == 21:
                self.neighbor0().place(x=110, y=414)
            elif self.index_selection == 22:
                self.neighbor0().place(x=211, y=414)
            elif self.index_selection == 23:
                self.neighbor0().place(x=312, y=414)
            elif self.index_selection == 24:
                self.neighbor0().place(x=413, y=414)

            for x in self.select_neighbors:
                if x in self.index_selection_list:
                    self.select_neighbors.remove(x)
            for x in self.select_neighbors:
                if x in self.index_selection_list:
                    self.select_neighbors.remove(x)
            for x in self.select_neighbors:
                if x in self.index_selection_list:
                    self.select_neighbors.remove(x)

            for n in self.select_neighbors:
                if n in self.bomb_neighbors:
                    for k, v in self.duplicate_bomb_neighbors.items():
                        if k == n:
                            if n == 0:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=10)
                                self.select_count += 1
                                
                            if n == 1:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=10)
                                self.select_count += 1
                                
                            if n == 2:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=10)
                                self.select_count += 1
                                
                            if n == 3:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=10)
                                self.select_count += 1
                                
                            if n == 4:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=10)
                                self.select_count += 1
                                
                            if n == 5:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=111)
                                self.select_count += 1
                                
                            if n == 6:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=111)
                                self.select_count += 1
                                
                            if n == 7:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=111)
                                self.select_count += 1
                                
                            if n == 8:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=111)
                                self.select_count += 1
                                
                            if n == 9:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=111)
                                self.select_count += 1
                                
                            if n == 10:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=212)
                                self.select_count += 1
                                
                            if n == 11:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=212)
                                self.select_count += 1
                                
                            if n == 12:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=212)
                                self.select_count += 1
                                
                            if n == 13:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=212)
                                self.select_count += 1
                                
                            if n == 14:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=212)
                                self.select_count += 1
                                
                            if n == 15:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=313)
                                self.select_count += 1
                                
                            if n == 16:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=313)
                                self.select_count += 1
                                
                            if n == 17:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=313)
                                self.select_count += 1
                                
                            if n == 18:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=313)
                                self.select_count += 1
                                
                            if n == 19:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=313)
                                self.select_count += 1
                                
                            if n == 20:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=414)
                                self.select_count += 1
                                
                            if n == 21:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=414)
                                self.select_count += 1
                                
                            if n == 22:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=414)
                                self.select_count += 1
                                
                            if n == 23:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=414)
                                self.select_count += 1
                                
                            if n == 24:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=414)
                                self.select_count += 1
                                
                elif n not in self.bomb_neighbors:
                    if n == 0:
                        self.neighbor0().place(x=9, y=10)
                        self.select_count += 1
                        self.select_neighborhood.extend([1, 5, 6])
                    if n == 1:
                        self.neighbor0().place(x=110, y=10)
                        self.select_count += 1
                        self.select_neighborhood.extend([0, 2, 5, 6, 7])
                    if n == 2:
                        self.neighbor0().place(x=211, y=10)
                        self.select_count += 1
                        self.select_neighborhood.extend([1, 3, 6, 7, 8])
                    if n == 3:
                        self.neighbor0().place(x=312, y=10)
                        self.select_count += 1
                        self.select_neighborhood.extend([2, 4, 7, 8, 9])
                    if n == 4:
                        self.neighbor0().place(x=413, y=10)
                        self.select_count += 1
                        self.select_neighborhood.extend([3, 8, 9])
                    if n == 5:
                        self.neighbor0().place(x=9, y=111)
                        self.select_count += 1
                        self.select_neighborhood.extend([0, 1, 6, 10, 11])
                    if n == 6:
                        self.neighbor0().place(x=110, y=111)
                        self.select_count += 1
                        self.select_neighborhood.extend([0, 1, 2, 5, 7, 10, 11, 12])
                    if n == 7:
                        self.neighbor0().place(x=211, y=111)
                        self.select_count += 1
                        self.select_neighborhood.extend([1, 2, 3, 6, 8, 11, 12, 13])
                    if n == 8:
                        self.neighbor0().place(x=312, y=111)
                        self.select_count += 1
                        self.select_neighborhood.extend([2, 3, 4, 7, 9, 12, 13, 14])
                    if n == 9:
                        self.neighbor0().place(x=413, y=111)
                        self.select_count += 1
                        self.select_neighborhood.extend([3, 4, 8, 13, 14])
                    if n == 10:
                        self.neighbor0().place(x=9, y=212)
                        self.select_count += 1
                        self.select_neighborhood.extend([5, 6, 11, 15, 16])
                    if n == 11:
                        self.neighbor0().place(x=110, y=212)
                        self.select_count += 1
                        self.select_neighborhood.extend([5, 6, 7, 10, 12, 15, 16, 17])
                    if n == 12:
                        self.neighbor0().place(x=211, y=212)
                        self.select_count += 1
                        self.select_neighborhood.extend([6, 7, 8, 11, 13, 16, 17, 18])
                    if n == 13:
                        self.neighbor0().place(x=312, y=212)
                        self.select_count += 1
                        self.select_neighborhood.extend([7, 8, 9, 12, 14, 17, 18, 19])
                    if n == 14:
                        self.neighbor0().place(x=413, y=212)
                        self.select_count += 1
                        self.select_neighborhood.extend([8, 9, 13, 18, 19])
                    if n == 15:
                        self.neighbor0().place(x=9, y=313)
                        self.select_count += 1
                        self.select_neighborhood.extend([10, 11, 16, 20, 21])
                    if n == 16:
                        self.neighbor0().place(x=110, y=313)
                        self.select_count += 1
                        self.select_neighborhood.extend([10, 11, 12, 15, 17, 20, 21, 22])
                    if n == 17:
                        self.neighbor0().place(x=211, y=313)
                        self.select_count += 1
                        self.select_neighborhood.extend([11, 12, 13, 16, 18, 21, 22, 23])
                    if n == 18:
                        self.neighbor0().place(x=312, y=313)
                        self.select_count += 1
                        self.select_neighborhood.extend([12, 13, 14, 17, 19, 22, 23, 24])
                    if n == 19:
                        self.neighbor0().place(x=413, y=313)
                        self.select_count += 1
                        self.select_neighborhood.extend([13, 14, 18, 23, 24])
                    if n == 20:
                        self.neighbor0().place(x=9, y=414)
                        self.select_count += 1
                        self.select_neighborhood.extend([15, 16, 21])
                    if n == 21:
                        self.neighbor0().place(x=110, y=414)
                        self.select_count += 1
                        self.select_neighborhood.extend([15, 16, 17, 20, 22])
                    if n == 22:
                        self.neighbor0().place(x=211, y=414)
                        self.select_count += 1
                        self.select_neighborhood.extend([16, 17, 18, 21, 23])
                    if n == 23:
                        self.neighbor0().place(x=312, y=414)
                        self.select_count += 1
                        self.select_neighborhood.extend([17, 18, 19, 22, 24])
                    if n == 24:
                        self.neighbor0().place(x=413, y=414)
                        self.select_count += 1
                        self.select_neighborhood.extend([18, 19, 23])

                    self.select_neighborhood = list(set(self.select_neighborhood))

        if self.select_neighborhood:

            for y in self.select_neighborhood:
                if (y in self.index_selection_list):
                    self.select_neighborhood.remove(y)
            for y in self.select_neighborhood:
                if (y in self.index_selection_list):
                    self.select_neighborhood.remove(y)
            for y in self.select_neighborhood:
                if (y in self.index_selection_list):
                    self.select_neighborhood.remove(y)
            
            for y in self.select_neighborhood:
                if (y in self.select_neighbors):
                    self.select_neighborhood.remove(y)
            for y in self.select_neighborhood:
                if (y in self.select_neighbors):
                    self.select_neighborhood.remove(y)
            for y in self.select_neighborhood:
                if (y in self.select_neighbors):
                    self.select_neighborhood.remove(y)

            for n in self.select_neighborhood:
                if n in self.bomb_neighbors:
                    for k, v in self.duplicate_bomb_neighbors.items():
                        if k == n:
                            if n == 0:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=10)
                                self.select_count += 1
                                
                            if n == 1:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=10)
                                self.select_count += 1
                                
                            if n == 2:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=10)
                                self.select_count += 1
                                
                            if n == 3:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=10)
                                self.select_count += 1
                                
                            if n == 4:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=10)
                                self.select_count += 1
                                
                            if n == 5:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=111)
                                self.select_count += 1
                                
                            if n == 6:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=111)
                                self.select_count += 1
                                
                            if n == 7:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=111)
                                self.select_count += 1
                                
                            if n == 8:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=111)
                                self.select_count += 1
                                
                            if n == 9:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=111)
                                self.select_count += 1
                                
                            if n == 10:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=212)
                                self.select_count += 1
                                
                            if n == 11:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=212)
                                self.select_count += 1
                                
                            if n == 12:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=212)
                                self.select_count += 1
                                
                            if n == 13:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=212)
                                self.select_count += 1
                                
                            if n == 14:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=212)
                                self.select_count += 1
                                
                            if n == 15:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=313)
                                self.select_count += 1
                                
                            if n == 16:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=313)
                                self.select_count += 1
                                
                            if n == 17:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=313)
                                self.select_count += 1
                                
                            if n == 18:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=313)
                                self.select_count += 1
                                
                            if n == 19:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=313)
                                self.select_count += 1
                                
                            if n == 20:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=414)
                                self.select_count += 1
                                
                            if n == 21:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=414)
                                self.select_count += 1
                                
                            if n == 22:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=414)
                                self.select_count += 1
                                
                            if n == 23:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=414)
                                self.select_count += 1
                                
                            if n == 24:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=414)
                                self.select_count += 1
                                
                elif n not in self.bomb_neighbors:
                    if n == 0:
                        self.neighbor0().place(x=9, y=10)
                        self.select_count += 1
                        self.select_neighborhood1.extend([1, 5, 6])
                    if n == 1:
                        self.neighbor0().place(x=110, y=10)
                        self.select_count += 1
                        self.select_neighborhood1.extend([0, 2, 5, 6, 7])
                    if n == 2:
                        self.neighbor0().place(x=211, y=10)
                        self.select_count += 1
                        self.select_neighborhood1.extend([1, 3, 6, 7, 8])
                    if n == 3:
                        self.neighbor0().place(x=312, y=10)
                        self.select_count += 1
                        self.select_neighborhood1.extend([2, 4, 7, 8, 9])
                    if n == 4:
                        self.neighbor0().place(x=413, y=10)
                        self.select_count += 1
                        self.select_neighborhood1.extend([3, 8, 9])
                    if n == 5:
                        self.neighbor0().place(x=9, y=111)
                        self.select_count += 1
                        self.select_neighborhood1.extend([0, 1, 6, 10, 11])
                    if n == 6:
                        self.neighbor0().place(x=110, y=111)
                        self.select_count += 1
                        self.select_neighborhood1.extend([0, 1, 2, 5, 7, 10, 11, 12])
                    if n == 7:
                        self.neighbor0().place(x=211, y=111)
                        self.select_count += 1
                        self.select_neighborhood1.extend([1, 2, 3, 6, 8, 11, 12, 13])
                    if n == 8:
                        self.neighbor0().place(x=312, y=111)
                        self.select_count += 1
                        self.select_neighborhood1.extend([2, 3, 4, 7, 9, 12, 13, 14])
                    if n == 9:
                        self.neighbor0().place(x=413, y=111)
                        self.select_count += 1
                        self.select_neighborhood1.extend([3, 4, 8, 13, 14])
                    if n == 10:
                        self.neighbor0().place(x=9, y=212)
                        self.select_count += 1
                        self.select_neighborhood1.extend([5, 6, 11, 15, 16])
                    if n == 11:
                        self.neighbor0().place(x=110, y=212)
                        self.select_count += 1
                        self.select_neighborhood1.extend([5, 6, 7, 10, 12, 15, 16, 17])
                    if n == 12:
                        self.neighbor0().place(x=211, y=212)
                        self.select_count += 1
                        self.select_neighborhood1.extend([6, 7, 8, 11, 13, 16, 17, 18])
                    if n == 13:
                        self.neighbor0().place(x=312, y=212)
                        self.select_count += 1
                        self.select_neighborhood1.extend([7, 8, 9, 12, 14, 17, 18, 19])
                    if n == 14:
                        self.neighbor0().place(x=413, y=212)
                        self.select_count += 1
                        self.select_neighborhood1.extend([8, 9, 13, 18, 19])
                    if n == 15:
                        self.neighbor0().place(x=9, y=313)
                        self.select_count += 1
                        self.select_neighborhood1.extend([10, 11, 16, 20, 21])
                    if n == 16:
                        self.neighbor0().place(x=110, y=313)
                        self.select_count += 1
                        self.select_neighborhood1.extend([10, 11, 12, 15, 17, 20, 21, 22])
                    if n == 17:
                        self.neighbor0().place(x=211, y=313)
                        self.select_count += 1
                        self.select_neighborhood1.extend([11, 12, 13, 16, 18, 21, 22, 23])
                    if n == 18:
                        self.neighbor0().place(x=312, y=313)
                        self.select_count += 1
                        self.select_neighborhood1.extend([12, 13, 14, 17, 19, 22, 23, 24])
                    if n == 19:
                        self.neighbor0().place(x=413, y=313)
                        self.select_count += 1
                        self.select_neighborhood1.extend([13, 14, 18, 23, 24])
                    if n == 20:
                        self.neighbor0().place(x=9, y=414)
                        self.select_count += 1
                        self.select_neighborhood1.extend([15, 16, 21])
                    if n == 21:
                        self.neighbor0().place(x=110, y=414)
                        self.select_count += 1
                        self.select_neighborhood1.extend([15, 16, 17, 20, 22])
                    if n == 22:
                        self.neighbor0().place(x=211, y=414)
                        self.select_count += 1
                        self.select_neighborhood1.extend([16, 17, 18, 21, 23])
                    if n == 23:
                        self.neighbor0().place(x=312, y=414)
                        self.select_count += 1
                        self.select_neighborhood1.extend([17, 18, 19, 22, 24])
                    if n == 24:
                        self.neighbor0().place(x=413, y=414)
                        self.select_count += 1
                        self.select_neighborhood1.extend([18, 19, 23])

                    self.select_neighborhood1 = list(set(self.select_neighborhood1))

        if self.select_neighborhood1:

            for y in self.select_neighborhood1:
                if (y in self.index_selection_list):
                    self.select_neighborhood1.remove(y)
            for y in self.select_neighborhood1:
                if (y in self.index_selection_list):
                    self.select_neighborhood1.remove(y)
            for y in self.select_neighborhood1:
                if (y in self.index_selection_list):
                    self.select_neighborhood1.remove(y)
            
            for y in self.select_neighborhood1:
                if (y in self.select_neighbors):
                    self.select_neighborhood1.remove(y)
            for y in self.select_neighborhood1:
                if (y in self.select_neighbors):
                    self.select_neighborhood1.remove(y)
            for y in self.select_neighborhood1:
                if (y in self.select_neighbors):
                    self.select_neighborhood1.remove(y)
            
            for y in self.select_neighborhood1:
                if (y in self.select_neighborhood):
                    self.select_neighborhood1.remove(y)
            for y in self.select_neighborhood1:
                if (y in self.select_neighborhood):
                    self.select_neighborhood1.remove(y)
            for y in self.select_neighborhood1:
                if (y in self.select_neighborhood):
                    self.select_neighborhood1.remove(y)

            for n in self.select_neighborhood1:
                if n in self.bomb_neighbors:
                    for k, v in self.duplicate_bomb_neighbors.items():
                        if k == n:
                            if n == 0:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=10)
                                self.select_count += 1
                                
                            if n == 1:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=10)
                                self.select_count += 1
                                
                            if n == 2:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=10)
                                self.select_count += 1
                                
                            if n == 3:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=10)
                                self.select_count += 1
                                
                            if n == 4:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=10)
                                self.select_count += 1
                                
                            if n == 5:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=111)
                                self.select_count += 1
                                
                            if n == 6:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=111)
                                self.select_count += 1
                                
                            if n == 7:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=111)
                                self.select_count += 1
                                
                            if n == 8:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=111)
                                self.select_count += 1
                                
                            if n == 9:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=111)
                                self.select_count += 1
                                
                            if n == 10:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=212)
                                self.select_count += 1
                                
                            if n == 11:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=212)
                                self.select_count += 1
                                
                            if n == 12:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=212)
                                self.select_count += 1
                                
                            if n == 13:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=212)
                                self.select_count += 1
                                
                            if n == 14:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=212)
                                self.select_count += 1
                                
                            if n == 15:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=313)
                                self.select_count += 1
                                
                            if n == 16:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=313)
                                self.select_count += 1
                                
                            if n == 17:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=313)
                                self.select_count += 1
                                
                            if n == 18:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=313)
                                self.select_count += 1
                                
                            if n == 19:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=313)
                                self.select_count += 1
                                
                            if n == 20:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=414)
                                self.select_count += 1
                                
                            if n == 21:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=414)
                                self.select_count += 1
                                
                            if n == 22:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=414)
                                self.select_count += 1
                                
                            if n == 23:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=414)
                                self.select_count += 1
                                
                            if n == 24:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=414)
                                self.select_count += 1

                elif n not in self.bomb_neighbors:
                    if n == 0:
                        self.neighbor0().place(x=9, y=10)
                        self.select_count += 1
                        self.select_neighborhood2.extend([1, 5, 6])
                    if n == 1:
                        self.neighbor0().place(x=110, y=10)
                        self.select_count += 1
                        self.select_neighborhood2.extend([0, 2, 5, 6, 7])
                    if n == 2:
                        self.neighbor0().place(x=211, y=10)
                        self.select_count += 1
                        self.select_neighborhood2.extend([1, 3, 6, 7, 8])
                    if n == 3:
                        self.neighbor0().place(x=312, y=10)
                        self.select_count += 1
                        self.select_neighborhood2.extend([2, 4, 7, 8, 9])
                    if n == 4:
                        self.neighbor0().place(x=413, y=10)
                        self.select_count += 1
                        self.select_neighborhood2.extend([3, 8, 9])
                    if n == 5:
                        self.neighbor0().place(x=9, y=111)
                        self.select_count += 1
                        self.select_neighborhood2.extend([0, 1, 6, 10, 11])
                    if n == 6:
                        self.neighbor0().place(x=110, y=111)
                        self.select_count += 1
                        self.select_neighborhood2.extend([0, 1, 2, 5, 7, 10, 11, 12])
                    if n == 7:
                        self.neighbor0().place(x=211, y=111)
                        self.select_count += 1
                        self.select_neighborhood2.extend([1, 2, 3, 6, 8, 11, 12, 13])
                    if n == 8:
                        self.neighbor0().place(x=312, y=111)
                        self.select_count += 1
                        self.select_neighborhood2.extend([2, 3, 4, 7, 9, 12, 13, 14])
                    if n == 9:
                        self.neighbor0().place(x=413, y=111)
                        self.select_count += 1
                        self.select_neighborhood2.extend([3, 4, 8, 13, 14])
                    if n == 10:
                        self.neighbor0().place(x=9, y=212)
                        self.select_count += 1
                        self.select_neighborhood2.extend([5, 6, 11, 15, 16])
                    if n == 11:
                        self.neighbor0().place(x=110, y=212)
                        self.select_count += 1
                        self.select_neighborhood2.extend([5, 6, 7, 10, 12, 15, 16, 17])
                    if n == 12:
                        self.neighbor0().place(x=211, y=212)
                        self.select_count += 1
                        self.select_neighborhood2.extend([6, 7, 8, 11, 13, 16, 17, 18])
                    if n == 13:
                        self.neighbor0().place(x=312, y=212)
                        self.select_count += 1
                        self.select_neighborhood2.extend([7, 8, 9, 12, 14, 17, 18, 19])
                    if n == 14:
                        self.neighbor0().place(x=413, y=212)
                        self.select_count += 1
                        self.select_neighborhood2.extend([8, 9, 13, 18, 19])
                    if n == 15:
                        self.neighbor0().place(x=9, y=313)
                        self.select_count += 1
                        self.select_neighborhood2.extend([10, 11, 16, 20, 21])
                    if n == 16:
                        self.neighbor0().place(x=110, y=313)
                        self.select_count += 1
                        self.select_neighborhood2.extend([10, 11, 12, 15, 17, 20, 21, 22])
                    if n == 17:
                        self.neighbor0().place(x=211, y=313)
                        self.select_count += 1
                        self.select_neighborhood2.extend([11, 12, 13, 16, 18, 21, 22, 23])
                    if n == 18:
                        self.neighbor0().place(x=312, y=313)
                        self.select_count += 1
                        self.select_neighborhood2.extend([12, 13, 14, 17, 19, 22, 23, 24])
                    if n == 19:
                        self.neighbor0().place(x=413, y=313)
                        self.select_count += 1
                        self.select_neighborhood2.extend([13, 14, 18, 23, 24])
                    if n == 20:
                        self.neighbor0().place(x=9, y=414)
                        self.select_count += 1
                        self.select_neighborhood2.extend([15, 16, 21])
                    if n == 21:
                        self.neighbor0().place(x=110, y=414)
                        self.select_count += 1
                        self.select_neighborhood2.extend([15, 16, 17, 20, 22])
                    if n == 22:
                        self.neighbor0().place(x=211, y=414)
                        self.select_count += 1
                        self.select_neighborhood2.extend([16, 17, 18, 21, 23])
                    if n == 23:
                        self.neighbor0().place(x=312, y=414)
                        self.select_count += 1
                        self.select_neighborhood2.extend([17, 18, 19, 22, 24])
                    if n == 24:
                        self.neighbor0().place(x=413, y=414)
                        self.select_count += 1
                        self.select_neighborhood2.extend([18, 19, 23])

                    self.select_neighborhood2 = list(set(self.select_neighborhood2))

        if self.select_neighborhood2:

            for y in self.select_neighborhood2:
                if (y in self.index_selection_list):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.index_selection_list):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.index_selection_list):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.index_selection_list):
                    self.select_neighborhood2.remove(y)
            
            for y in self.select_neighborhood2:
                if (y in self.select_neighbors):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighbors):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighbors):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighbors):
                    self.select_neighborhood2.remove(y)
            
            for y in self.select_neighborhood2:
                if (y in self.select_neighborhood):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighborhood):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighborhood):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighborhood):
                    self.select_neighborhood2.remove(y)

            for y in self.select_neighborhood2:
                if (y in self.select_neighborhood1):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighborhood1):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighborhood1):
                    self.select_neighborhood2.remove(y)
            for y in self.select_neighborhood2:
                if (y in self.select_neighborhood1):
                    self.select_neighborhood2.remove(y)

            for n in self.select_neighborhood2:
                if n in self.bomb_neighbors:
                    for k, v in self.duplicate_bomb_neighbors.items():
                        if k == n:
                            if n == 0:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=10)
                                self.select_count += 1
                                
                            if n == 1:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=10)
                                self.select_count += 1
                                
                            if n == 2:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=10)
                                self.select_count += 1
                                
                            if n == 3:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=10)
                                self.select_count += 1
                                
                            if n == 4:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=10)
                                self.select_count += 1
                                
                            if n == 5:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=111)
                                self.select_count += 1
                                
                            if n == 6:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=111)
                                self.select_count += 1
                                
                            if n == 7:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=111)
                                self.select_count += 1
                                
                            if n == 8:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=111)
                                self.select_count += 1
                                
                            if n == 9:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=111)
                                self.select_count += 1
                                
                            if n == 10:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=212)
                                self.select_count += 1
                                
                            if n == 11:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=212)
                                self.select_count += 1
                                
                            if n == 12:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=212)
                                self.select_count += 1
                                
                            if n == 13:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=212)
                                self.select_count += 1
                                
                            if n == 14:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=212)
                                self.select_count += 1
                                
                            if n == 15:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=313)
                                self.select_count += 1
                                
                            if n == 16:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=313)
                                self.select_count += 1
                                
                            if n == 17:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=313)
                                self.select_count += 1
                                
                            if n == 18:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=313)
                                self.select_count += 1
                                
                            if n == 19:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=313)
                                self.select_count += 1
                                
                            if n == 20:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=414)
                                self.select_count += 1
                                
                            if n == 21:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=414)
                                self.select_count += 1
                                
                            if n == 22:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=414)
                                self.select_count += 1
                                
                            if n == 23:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=414)
                                self.select_count += 1
                                
                            if n == 24:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=414)
                                self.select_count += 1

                elif n not in self.bomb_neighbors:
                    if n == 0:
                        self.neighbor0().place(x=9, y=10)
                        self.select_count += 1
                        self.select_neighborhood3.extend([1, 5, 6])
                    if n == 1:
                        self.neighbor0().place(x=110, y=10)
                        self.select_count += 1
                        self.select_neighborhood3.extend([0, 2, 5, 6, 7])
                    if n == 2:
                        self.neighbor0().place(x=211, y=10)
                        self.select_count += 1
                        self.select_neighborhood3.extend([1, 3, 6, 7, 8])
                    if n == 3:
                        self.neighbor0().place(x=312, y=10)
                        self.select_count += 1
                        self.select_neighborhood3.extend([2, 4, 7, 8, 9])
                    if n == 4:
                        self.neighbor0().place(x=413, y=10)
                        self.select_count += 1
                        self.select_neighborhood3.extend([3, 8, 9])
                    if n == 5:
                        self.neighbor0().place(x=9, y=111)
                        self.select_count += 1
                        self.select_neighborhood3.extend([0, 1, 6, 10, 11])
                    if n == 6:
                        self.neighbor0().place(x=110, y=111)
                        self.select_count += 1
                        self.select_neighborhood3.extend([0, 1, 2, 5, 7, 10, 11, 12])
                    if n == 7:
                        self.neighbor0().place(x=211, y=111)
                        self.select_count += 1
                        self.select_neighborhood3.extend([1, 2, 3, 6, 8, 11, 12, 13])
                    if n == 8:
                        self.neighbor0().place(x=312, y=111)
                        self.select_count += 1
                        self.select_neighborhood3.extend([2, 3, 4, 7, 9, 12, 13, 14])
                    if n == 9:
                        self.neighbor0().place(x=413, y=111)
                        self.select_count += 1
                        self.select_neighborhood3.extend([3, 4, 8, 13, 14])
                    if n == 10:
                        self.neighbor0().place(x=9, y=212)
                        self.select_count += 1
                        self.select_neighborhood3.extend([5, 6, 11, 15, 16])
                    if n == 11:
                        self.neighbor0().place(x=110, y=212)
                        self.select_count += 1
                        self.select_neighborhood3.extend([5, 6, 7, 10, 12, 15, 16, 17])
                    if n == 12:
                        self.neighbor0().place(x=211, y=212)
                        self.select_count += 1
                        self.select_neighborhood3.extend([6, 7, 8, 11, 13, 16, 17, 18])
                    if n == 13:
                        self.neighbor0().place(x=312, y=212)
                        self.select_count += 1
                        self.select_neighborhood3.extend([7, 8, 9, 12, 14, 17, 18, 19])
                    if n == 14:
                        self.neighbor0().place(x=413, y=212)
                        self.select_count += 1
                        self.select_neighborhood3.extend([8, 9, 13, 18, 19])
                    if n == 15:
                        self.neighbor0().place(x=9, y=313)
                        self.select_count += 1
                        self.select_neighborhood3.extend([10, 11, 16, 20, 21])
                    if n == 16:
                        self.neighbor0().place(x=110, y=313)
                        self.select_count += 1
                        self.select_neighborhood3.extend([10, 11, 12, 15, 17, 20, 21, 22])
                    if n == 17:
                        self.neighbor0().place(x=211, y=313)
                        self.select_count += 1
                        self.select_neighborhood3.extend([11, 12, 13, 16, 18, 21, 22, 23])
                    if n == 18:
                        self.neighbor0().place(x=312, y=313)
                        self.select_count += 1
                        self.select_neighborhood3.extend([12, 13, 14, 17, 19, 22, 23, 24])
                    if n == 19:
                        self.neighbor0().place(x=413, y=313)
                        self.select_count += 1
                        self.select_neighborhood3.extend([13, 14, 18, 23, 24])
                    if n == 20:
                        self.neighbor0().place(x=9, y=414)
                        self.select_count += 1
                        self.select_neighborhood3.extend([15, 16, 21])
                    if n == 21:
                        self.neighbor0().place(x=110, y=414)
                        self.select_count += 1
                        self.select_neighborhood3.extend([15, 16, 17, 20, 22])
                    if n == 22:
                        self.neighbor0().place(x=211, y=414)
                        self.select_count += 1
                        self.select_neighborhood3.extend([16, 17, 18, 21, 23])
                    if n == 23:
                        self.neighbor0().place(x=312, y=414)
                        self.select_count += 1
                        self.select_neighborhood3.extend([17, 18, 19, 22, 24])
                    if n == 24:
                        self.neighbor0().place(x=413, y=414)
                        self.select_count += 1
                        self.select_neighborhood3.extend([18, 19, 23])

                    self.select_neighborhood3 = list(set(self.select_neighborhood3))

        if self.select_neighborhood3:

            for y in self.select_neighborhood3:
                if (y in self.index_selection_list):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.index_selection_list):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.index_selection_list):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.index_selection_list):
                    self.select_neighborhood3.remove(y)
            
            for y in self.select_neighborhood3:
                if (y in self.select_neighbors):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighbors):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighbors):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighbors):
                    self.select_neighborhood3.remove(y)
            
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood):
                    self.select_neighborhood3.remove(y)

            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood1):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood1):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood1):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood1):
                    self.select_neighborhood3.remove(y)

            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood2):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood2):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood2):
                    self.select_neighborhood3.remove(y)
            for y in self.select_neighborhood3:
                if (y in self.select_neighborhood2):
                    self.select_neighborhood3.remove(y)

            for n in self.select_neighborhood3:
                if n in self.bomb_neighbors:
                    for k, v in self.duplicate_bomb_neighbors.items():
                        if k == n:
                            if n == 0:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=10)
                                self.select_count += 1
                                
                            if n == 1:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=10)
                                self.select_count += 1
                                
                            if n == 2:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=10)
                                self.select_count += 1
                                
                            if n == 3:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=10)
                                self.select_count += 1
                                
                            if n == 4:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=10)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=10)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=10)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=10)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=10)
                                self.select_count += 1
                                
                            if n == 5:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=111)
                                self.select_count += 1
                                
                            if n == 6:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=111)
                                self.select_count += 1
                                
                            if n == 7:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=111)
                                self.select_count += 1
                                
                            if n == 8:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=111)
                                self.select_count += 1
                                
                            if n == 9:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=111)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=111)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=111)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=111)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=111)
                                self.select_count += 1
                                
                            if n == 10:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=212)
                                self.select_count += 1
                                
                            if n == 11:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=212)
                                self.select_count += 1
                                
                            if n == 12:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=212)
                                self.select_count += 1
                                
                            if n == 13:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=212)
                                self.select_count += 1
                                
                            if n == 14:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=212)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=212)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=212)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=212)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=212)
                                self.select_count += 1
                                
                            if n == 15:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=313)
                                self.select_count += 1
                                
                            if n == 16:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=313)
                                self.select_count += 1
                                
                            if n == 17:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=313)
                                self.select_count += 1
                                
                            if n == 18:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=313)
                                self.select_count += 1
                                
                            if n == 19:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=313)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=313)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=313)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=313)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=313)
                                self.select_count += 1
                                
                            if n == 20:
                                if v == 1:
                                    self.neighbor1().place(x=9, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=9, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=9, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=9, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=9, y=414)
                                self.select_count += 1
                                
                            if n == 21:
                                if v == 1:
                                    self.neighbor1().place(x=110, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=110, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=110, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=110, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=110, y=414)
                                self.select_count += 1
                                
                            if n == 22:
                                if v == 1:
                                    self.neighbor1().place(x=211, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=211, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=211, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=211, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=211, y=414)
                                self.select_count += 1
                                
                            if n == 23:
                                if v == 1:
                                    self.neighbor1().place(x=312, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=312, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=312, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=312, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=312, y=414)
                                self.select_count += 1
                                
                            if n == 24:
                                if v == 1:
                                    self.neighbor1().place(x=413, y=414)
                                elif v == 2:
                                    self.neighbor2().place(x=413, y=414)
                                elif v == 3:
                                    self.neighbor3().place(x=413, y=414)
                                elif v == 4:
                                    self.neighbor4().place(x=413, y=414)
                                elif v == 5:
                                    self.neighbor5().place(x=413, y=414)
                                self.select_count += 1

        if self.select_count == 20:
            self.playing = False
            self.after(500, self.user_win)

        self.select_neighbors.clear()
        self.select_neighborhood.clear()
        self.select_neighborhood1.clear()
        self.select_neighborhood2.clear()
        self.select_neighborhood3.clear()

    def user_lose(self):

        def restart_lose():
            self.playing = True
            self.select_neighbors = []
            self.select_count = 0
            self.index_selection = None
            self.index_selection_list = []
            self.bomb_neighbors = []
            self.bomb_locations = None
            self.duplicate_bomb_neighbors = []
            self.select_neighborhood = []
            self.select_neighborhood1 = []
            self.select_neighborhood2 = []
            self.select_neighborhood3 = []

            self.user_choice()

        def nukes():

            for x in self.bomb_locations:
                if x == 0:
                    self.bomb_triggered().place(x=9, y=10)
                if x == 1:
                    self.bomb_triggered().place(x=110, y=10)
                if x == 2:
                    self.bomb_triggered().place(x=211, y=10)
                if x == 3:
                    self.bomb_triggered().place(x=312, y=10)
                if x == 4:
                    self.bomb_triggered().place(x=413, y=10)
                if x == 5:
                    self.bomb_triggered().place(x=9, y=111)
                if x == 6:
                    self.bomb_triggered().place(x=110, y=111)
                if x == 7:
                    self.bomb_triggered().place(x=211, y=111)
                if x == 8:
                    self.bomb_triggered().place(x=312, y=111)
                if x == 9:
                    self.bomb_triggered().place(x=413, y=111)
                if x == 10:
                    self.bomb_triggered().place(x=9, y=212)
                if x == 11:
                    self.bomb_triggered().place(x=110, y=212)
                if x == 12:
                    self.bomb_triggered().place(x=211, y=212)
                if x == 13:
                    self.bomb_triggered().place(x=312, y=212)
                if x == 14:
                    self.bomb_triggered().place(x=413, y=212)
                if x == 15:
                    self.bomb_triggered().place(x=9, y=313)
                if x == 16:
                    self.bomb_triggered().place(x=110, y=313)
                if x == 17:
                    self.bomb_triggered().place(x=211, y=313)
                if x == 18:
                    self.bomb_triggered().place(x=312, y=313)
                if x == 19:
                    self.bomb_triggered().place(x=413, y=313)
                if x == 20:
                    self.bomb_triggered().place(x=9, y=414)
                if x == 21:
                    self.bomb_triggered().place(x=110, y=414)
                if x == 22:
                    self.bomb_triggered().place(x=211, y=414)
                if x == 23:
                    self.bomb_triggered().place(x=312, y=414)
                if x == 24:
                    self.bomb_triggered().place(x=413, y=414)

            self.after(10000, restart_lose)

        for x in self.bomb_locations:
            if x == 0:
                self.bomb().place(x=9, y=10)
            if x == 1:
                self.bomb().place(x=110, y=10)
            if x == 2:
                self.bomb().place(x=211, y=10)
            if x == 3:
                self.bomb().place(x=312, y=10)
            if x == 4:
                self.bomb().place(x=413, y=10)
            if x == 5:
                self.bomb().place(x=9, y=111)
            if x == 6:
                self.bomb().place(x=110, y=111)
            if x == 7:
                self.bomb().place(x=211, y=111)
            if x == 8:
                self.bomb().place(x=312, y=111)
            if x == 9:
                self.bomb().place(x=413, y=111)
            if x == 10:
                self.bomb().place(x=9, y=212)
            if x == 11:
                self.bomb().place(x=110, y=212)
            if x == 12:
                self.bomb().place(x=211, y=212)
            if x == 13:
                self.bomb().place(x=312, y=212)
            if x == 14:
                self.bomb().place(x=413, y=212)
            if x == 15:
                self.bomb().place(x=9, y=313)
            if x == 16:
                self.bomb().place(x=110, y=313)
            if x == 17:
                self.bomb().place(x=211, y=313)
            if x == 18:
                self.bomb().place(x=312, y=313)
            if x == 19:
                self.bomb().place(x=413, y=313)
            if x == 20:
                self.bomb().place(x=9, y=414)
            if x == 21:
                self.bomb().place(x=110, y=414)
            if x == 22:
                self.bomb().place(x=211, y=414)
            if x == 23:
                self.bomb().place(x=312, y=414)
            if x == 24:
                self.bomb().place(x=413, y=414)

        self.after(1000, nukes)

    def user_win(self):
        
        def restart_win():
            self.playing = True
            self.select_neighbors = []
            self.select_count = 0
            self.index_selection = None
            self.index_selection_list = []
            self.bomb_neighbors = []
            self.bomb_locations = None
            self.duplicate_bomb_neighbors = []
            self.select_neighborhood = []
            self.select_neighborhood1 = []
            self.select_neighborhood2 = []
            self.select_neighborhood3 = []

            self.user_choice()

        for x in self.bomb_locations:
            if x == 0:
                self.bomb().place(x=9, y=10)
            if x == 1:
                self.bomb().place(x=110, y=10)
            if x == 2:
                self.bomb().place(x=211, y=10)
            if x == 3:
                self.bomb().place(x=312, y=10)
            if x == 4:
                self.bomb().place(x=413, y=10)
            if x == 5:
                self.bomb().place(x=9, y=111)
            if x == 6:
                self.bomb().place(x=110, y=111)
            if x == 7:
                self.bomb().place(x=211, y=111)
            if x == 8:
                self.bomb().place(x=312, y=111)
            if x == 9:
                self.bomb().place(x=413, y=111)
            if x == 10:
                self.bomb().place(x=9, y=212)
            if x == 11:
                self.bomb().place(x=110, y=212)
            if x == 12:
                self.bomb().place(x=211, y=212)
            if x == 13:
                self.bomb().place(x=312, y=212)
            if x == 14:
                self.bomb().place(x=413, y=212)
            if x == 15:
                self.bomb().place(x=9, y=313)
            if x == 16:
                self.bomb().place(x=110, y=313)
            if x == 17:
                self.bomb().place(x=211, y=313)
            if x == 18:
                self.bomb().place(x=312, y=313)
            if x == 19:
                self.bomb().place(x=413, y=313)
            if x == 20:
                self.bomb().place(x=9, y=414)
            if x == 21:
                self.bomb().place(x=110, y=414)
            if x == 22:
                self.bomb().place(x=211, y=414)
            if x == 23:
                self.bomb().place(x=312, y=414)
            if x == 24:
                self.bomb().place(x=413, y=414)


        self.after(10000, restart_win)


class template(Label):
    def __init__(self):
        Label.__init__(self)
        self.board_image = PhotoImage(file='png\\mine_frame.png')
        self.board_label = Label(image=self.board_image, bd=7, background="medium sea green")
        self.board_label.place(x=3, y=3)


class game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("520x520")
        self.title("minesweeper")
        self.resizable(0,0)
        self.iconbitmap('png\\minesweeper.ico')

        self.Template = template()
        self.Play = play()


if __name__ == "__main__":
    root = game()
    root.mainloop()

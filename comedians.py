#%%
# Yellow Pepe

from os import path
import networkx as nx 
import pandas as pd 
import matplotlib.pyplot as plt 


class Comedy:

    def __init__(self, path):
        self.path = path 

    def parse_csv_to_graph(self):

        # I will create two variables that represent a list and i wil put each colum in one of them

        self.X = []
        self.Y = []

        with open(self.path) as comedy:
            for line in comedy:
                x,y = line.split(",")
                self.X.append(x)
                self.Y.append(y)
        # i will create the same list as previusly but more clean since the strip method will method returns a copy of the string by removing both the leading and the trailing characters (based on the string argument passed).
        self.source = []
        self.target = []
        for element1 in self.X:
            self.source.append(element1.strip())

        for element2 in self.Y:
            self.target.append(element2.strip())

        del self.target[0]
        del self.source[0]

        # I need a variable diagram that will represent my graph in an empty form first 
        # after that i will use the zip function to associate element by element each of my lists 
        # then i will use setdafault to avoid having the same source name duplicated many times, since in a dictionary this should no happend 
        
        self.diagram = {}
        for i, e in zip(self.source, self.target):
            self.diagram.setdefault(i, []).append(e)
        return self.diagram

        # This was not part of the task, but i created this function to print the graph line by line instead on in a disorder way (I like order)
    
    def print_line_by_line(self):
        for key, value in self.diagram.items():
            print(key, " : ", value)



        #return self.diagram
#comedy_graph = Comedy("comedians.csv")
#comedy_graph.parse_csv_to_graph()

class Comedy2:

    def __init__(self, start, end =None   ):
        self.start = start 
        self.end = end 

    def inlfuence_chains(self):
        if self.start is not None and self.end is None:
            return(comedy_graph.parse_csv_to_graph().get(str(self.start)))

        elif self.start is not None and self.end is not None:

            G = nx.Graph(comedy_graph.parse_csv_to_graph())
            a = nx.shortest_path(G, self.start, self.end)
            return a
            
            
        else:
            print("Pepe please provide a Start Comedian, My Suggestion will be George Carlin or Bill Cosby")

    def top_10_influencers(self):
        self.low_key = []
        self.number = []

        for k, v in comedy_graph.parse_csv_to_graph().items():
            self.low_key.append(k)
            self.number.append(len(v))
        return self.low_key, self.number

    def Nmaxelements(self, n):
        self.n = n 

        df1 = pd.DataFrame(list(comedy_path.top_10_influencers()))
        df = df1.T
        df.columns = ["Source", "Target"]
        df["Target"] = df["Target"].astype(float)
        df_final = df.drop(df.index[[199]])
        
        q = df.nlargest(self.n, ["Target"])
        
        return q

    def draw_graph(self):
        df_final_to_dic = comedy_path.Nmaxelements(10).to_dict()

        G = nx.Graph(df_final_to_dic)

        self.drawing = nx.draw_networkx(G = G,)

        
comedy_graph = Comedy("comedians.csv")

# HERE YOU SHOULD PICK UP THE PATH YOU WNAT TO EXPLORE FOR EXERCISE 2
comedy_path = Comedy2("George Carlin", "Bill Cosby")
# option 2 for Exercise 2, please comment the previus comedy_path befor trying this one 
#comedy_path = Comedy2("George Carlin")

question = input("Please tuype 1 or 2 or 3 or 4, depending on the Exercise you want to solve").lower()
if question == "1" : 


# EXERCISE 1 SOLUTION 
    question1 = input("Do you want just to return the graph?: yes or no").lower()
    if question1 == "yes":
        comedy_graph.parse_csv_to_graph()
    
    elif question1 == "no":
        print(" Please, anwer the next question Pepe")


        question2 = input("Do you want to convert the comedians.csv into a graph and print it line by line? (yes or no)").lower()      
        if question2 == "yes":
            comedy_graph.parse_csv_to_graph()
            comedy_graph.print_line_by_line()
        elif question2 == "no":
            print(" Game over Pepe")
        else:
            print(" please write yes or no, in one of the questions")
    else:
        print(" please write yes or no, in one of the questions")

elif question == "2":


# Exercise 2 Solution 
    print(comedy_path.inlfuence_chains())

elif question == "3":

# Excercise 3 Solution 
    print((comedy_path.Nmaxelements(10)))

elif question == "4":
# Exercise 4 Solution
#print(len(comedy_path.draw_graph()))
    comedy_path.draw_graph()

#print(len(comedy_graph.parse_csv_to_graph().get("Adam Sandler")))



# %%

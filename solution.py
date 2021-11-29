# Amir Ayoub
# aa2078

import sys
import math
import time 
import random

class Problem:
    
    def __init__(self, problem_path, mazes_folder):
        self.problem_path = problem_path
        self.mazes_folder=mazes_folder
        
        if not self.load_problem():
            return 
        if not self.load_maze():
            return
        
        self.can_simulate=True
        
        print("The maze was successfully been loaded")
        print("Maze size : ",self.width)
        print("Start (x, y): (",self.start_x,", ",self.start_y,")")
        
        self.paths=[[(self.start_x,self.start_y)]]     
        self.visited=[]
        self.true_path=[]
        self.resest=0
        self.visits=0
        
        print("Goal (x, y): (",self.goal_x,", ",self.goal_y,")")
        
        if self.algorithm==0:
            self.algorithm_str="Breadth-first search"
        elif self.algorithm==1:
            self.algorithm_str="Iterative deepening depth-first search"
            
        elif self.algorithm==2:
            self.algorithm_str="A* using one of h0"
           
        elif self.algorithm==3:
            self.algorithm_str="A* using one of h3"
           
        elif self.algorithm==4:
            self.algorithm_str="A* custom"
        else:
            self.can_simulate=False
            print("Invalid Algorithm")
            
        print("Algorithm: ",self.algorithm_str)
        self.maze_count_current=0
        self.di={}
        self.di[self.maze_path]={}
        
    def reset_maze(self):
        self.paths=[[(self.start_x,self.start_y)]]     
        self.visited=[]
        self.true_path=[]
        self.resest=0
        self.visits=0
        self.maze_count=0
        
    def run_50_sim(self):
        self.di={}
        i=0
        while True:
            if i<10:
                self.maze_path="00"+str(i)
            else:
                self.maze_path="0"+str(i)
            i+=1
            
            self.reset_maze()
            if not self.load_maze():
                return
            self.can_simulate=True
            print("The maze ",self.maze_path," was successfully been loaded")
            print("Maze size : ",self.width)
            print("Start (x, y): (",self.start_x,", ",self.start_y,")")
            print("Goal (x, y): (",self.goal_x,", ",self.goal_y,")")
            print("Algorithm: ",self.algorithm_str)

            start_time = time.time()
            if self.can_simulate == False:
                print("Can't simulate")
                continue
            # self.display_maze()
            res=None
            if self.algorithm==0:
                res=self.breadth_first_s()

            elif self.algorithm==1:
                res=self.iterative_deepening_depth_first()
            elif self.algorithm==2:
                res=self.a_start_h0()
            elif self.algorithm==3:
                res=self.a_start_h3()
            elif self.algorithm==4:
                res=self.a_start_h_custom()
            if not res:
                self.di[self.maze_path]="Failed"
                print("Unable to find the goal using ", self.algorithm_str)
                continue
            self.di[self.maze_path]={}
            end_time=time.time()
            self.diplay_path()
            self.di[self.maze_path]["Time"]=end_time-start_time
            
            print("Time ",end_time-start_time)
            if i>=50:
                break
# ,",",self.di[i]['Cost'],",",self.di[i]['Length']
        for i in self.di:
            print("maze_",i,end=" : ")
            print(self.di[i])

        # print()
        # print("Time") 
        # for i in self.di:
           
        #     if type(self.di[i])==type({}):
        #         print(self.di[i]['Time'])
        
        # print("Length")
        # for i in self.di:
         
        #     if type(self.di[i])==type({}):
        #         print(self.di[i]['Length'])
        # print("Cost")
        # for i in self.di:
         
        #     if type(self.di[i])==type({}):
        #         print(self.di[i]['Cost'])
        # print("Maze")
        # for i in self.di:
         
        #     if type(self.di[i])==type({}):
        #         print(i)
        
    def get_file(self, path):
        try:
            f=open(path,"r")
            data=f.readlines()
            f.close()
            return data
        except:
            print("Error file: "+path+" could not be opened")
            return None

    def load_problem(self):
        data=self.get_file(self.problem_path)
        if data==None:
            return False
        elif len(data)<5:
            print("Invalid data in the problem file")
            return False
        for i in range(len(data)):
            data[i]=data[i].strip()
            data[i]=data[i].strip("\n")

        self.width=int(data[0])
        self.hight=int(data[0])
        data[1]=data[1].split(" ")
        self.start_x=int(data[1][0])
        self.start_y=int(data[1][1])
        data[2]=data[2].split(" ")
        self.goal_x=int(data[2][0])
        self.goal_y=int(data[2][1])
        self.algorithm=int(data[3])            
        self.maze_path=data[4]
        return True
    
    def load_maze(self):
        data=self.get_file(self.mazes_folder+"/maze_"+self.maze_path+".txt")
        if data==None:
            return False
        elif len(data)<5:
            print("Invalid data in the maze file")
            return False
        raw=range(self.width)
        self.maze=[]
        for i in range(self.hight):
            self.maze.append(list(raw))
        for i in range(len(data)):
            temp=data[i].split(" ")
            x=int(temp[0])
            y=int(temp[1])
            self.maze[y][x]=int(temp[2])
        return True

    def display_maze(self):
        for y in range(self.hight):
            for x in range(self.width):
                if self.maze[y][x]==0:
                    if (x,y)==(self.start_x,self.start_y):
                        print("x",end="")
                    elif (x,y)==(self.goal_x,self.goal_y):
                        print(0, end="")
                    else:
                        print(" ",end="")
                else:
                    print("|", end="")
            print()
    def generate_next_nodes(self,current_node):
        i=current_node
        if current_node in self.visited:
            return []
        self.visited.append(current_node)
        next_nodes=[]
        next_nodes.append((current_node[0]+1,current_node[1]))
        next_nodes.append((current_node[0]-1,current_node[1]))
        next_nodes.append((current_node[0],current_node[1]+1))
        next_nodes.append((current_node[0],current_node[1]-1))
        ret=[]
        for i in next_nodes:
            if i in self.visited:
                continue
            elif i[0]>=0 and i[1]>=0 and i[0]<self.width and i[1]<self.hight and self.maze[i[1]][i[0]]==0:
                ret.append(i)
        return ret

    def breadth_first_s(self):
        visits=0
        resest=0
        print("Searching")
        while len(self.paths)>0:
            current_path=self.paths.pop(0)
            current_node=current_path[-1]
            next_queue=self.generate_next_nodes(current_node)
            visits+=len(next_queue)
            if visits%1000==0:
                print(">",end="")
                resest+=1
            if resest==10:
                print("")
                resest=0
            for i in next_queue:
                self.paths.append(current_path+[i])
               
                if i[0]==self.goal_x and i[1]==self.goal_y:
                    print("Path found after searching in ", visits," nodes")
                    self.true_path=current_path+[i]
                    return True
        return False
    
    def iterative_deepening_depth_first(self,current=[]):
        while True:
            current_path=self.paths.pop(len(self.paths)-1)
            current_node=current_path[-1]
            next_queue=self.generate_next_nodes(current_node)
            self.visits+=len(next_queue)
            if self.visits%1000==0:
                print(">",end="")
                self.resest+=1
            if self.resest==10:
                print("")
                self.resest=0
            for i in next_queue:
                self.paths.append(current_path+[i])
                if i[0]==self.goal_x and i[1]==self.goal_y:
                    print("Path found after searching in ", self.visits," nodes")
                    self.true_path=current_path+[i]
                    return True
            if self.paths:
                continue
            else:
                return False
    def a_start_h0(self):
        closed_list=[]
        open_list=list(self.paths)
        open_list_v_f=[0]
        while open_list:
            best=0
            for i in range(len(open_list)):
                if open_list_v_f[best]>open_list_v_f[i]:
                    best=i
            f=open_list_v_f.pop(best)
            q=open_list.pop(best)
            # current_path=self.paths.pop(best)
            current_node=q[-1]
            next_queue=self.generate_next_nodes(current_node)
            self.visits+=len(next_queue)
            if self.visits%1000==0:
                print(">",end="")
                self.resest+=1
            if self.resest==10:
                print("")
                self.resest=0
            for i in next_queue:
                open_list.append(q+[i])
                open_list_v_f.append(math.sqrt((self.goal_x-i[0])**2+(self.goal_y-i[1])**2))
                if i[0]==self.goal_x and i[1]==self.goal_y:
                    print("Path found after searching in ", self.visits," nodes")
                    self.true_path=q+[i]
                    return True
            if self.paths:
                continue
            else:
                return False

    def a_start_h3(self):
        closed_list=[]
        open_list=list(self.paths)
        open_list_v_f=[0]
        while open_list:
            best=0
            for i in range(len(open_list)):
                if open_list_v_f[best]>open_list_v_f[i]:
                    best=i
            f=open_list_v_f.pop(best)
            q=open_list.pop(best)
            # current_path=self.paths.pop(best)
            current_node=q[-1]
            next_queue=self.generate_next_nodes(current_node)
            self.visits+=len(next_queue)
            if self.visits%1000==0:
                print(">",end="")
                self.resest+=1
            if self.resest==10:
                print("")
                self.resest=0
            for i in next_queue:
                open_list.append(q+[i])
                h0=math.sqrt((self.goal_x-i[0])**2+(self.goal_y-i[1])**2)
                h1=(self.goal_x-i[0])+(self.goal_y-i[1])
                if h1<0:
                    h1=h1*-1
                h2=max(i[0],i[1])
                open_list_v_f.append(min(h0,h1,h2))
                if i[0]==self.goal_x and i[1]==self.goal_y:
                    print("Path found after searching in ", self.visits," nodes")
                    self.true_path=q+[i]
                    return True
            if self.paths:
                continue
            else:
                return False

    def a_start_h_custom(self):
        closed_list=[]
        open_list=list(self.paths)
        open_list_v_f=[0]
        while open_list:
            best=0
            for i in range(len(open_list)):
                if open_list_v_f[best]>open_list_v_f[i]:
                    best=i
            f=open_list_v_f.pop(best)
            q=open_list.pop(best)
            # current_path=self.paths.pop(best)
            current_node=q[-1]
            next_queue=self.generate_next_nodes(current_node)
            self.visits+=len(next_queue)
            if self.visits%1000==0:
                print(">",end="")
                self.resest+=1
            if self.resest==10:
                print("")
                self.resest=0
            for i in next_queue:
                open_list.append(q+[i])
               
                h2=min(i[0],i[1])
                open_list_v_f.append(h2)
                if i[0]==self.goal_x and i[1]==self.goal_y:
                    print("Path found after searching in ", self.visits," nodes")
                    self.true_path=q+[i]
                    return True
            if self.paths:
                continue
            else:
                return False

    def calculate_cost(self):
        cost=0
        current_node=self.true_path[0]
        for i in self.true_path:
            if current_node[0] != i[0]:
                cost+=1
            elif current_node[1]!=i[1]:
                cost+=2
            current_node=i
            
        print("The cost is of : ",cost)
        return cost

    def simulate_cost(self):
        start_time = time.time()
        if self.can_simulate == False:
            print("Can't simulate")
            return
        # self.display_maze()
        res=None
        if self.algorithm==0:
            res=self.breadth_first_s()

        elif self.algorithm==1:
            res=self.iterative_deepening_depth_first()
        elif self.algorithm==2:
            res=self.a_start_h0()
        elif self.algorithm==3:
            res=self.a_start_h3()
        elif self.algorithm==4:
            res=self.a_start_h_custom()
        if not res:
            print("Unable to find the goal using ", self.algorithm_str)
            return
        end_time=time.time()
        self.diplay_path()
        print("Time ",end_time-start_time)


    def diplay_path(self):
        path_printed=[]
        count=0
        for y in range(self.hight):
            for x in range(self.width):
                if self.maze[y][x]==0:
                    node=(x,y)
                    if (x,y)==(self.start_x,self.start_y):
                        print("x",end="")
                    elif (x,y)==(self.goal_x,self.goal_y):
                        print(0, end="")
                    elif node in self.true_path:
                        path_printed.append(node)
                        index=self.true_path.index(node)
                        node_prev=self.true_path[index-1]
                        if node_prev[0]+1 == node[0]:
                            print(">",end="")
                        elif node_prev[0]-1 == node[0]:
                            print("<",end="")
                        elif node_prev[1]-1 == node[1]:
                            print("^",end="")
                        elif node_prev[1]+1 == node[1]:
                            print("v",end="")
                    else:
                        print(" ",end="")
                else:
                    print("|", end="")
            print()
            if len(path_printed)+2== len(self.true_path):
                count+=1
            if len(path_printed)+2== len(self.true_path) and count==4:
                break
        print("Path length: ", len(path_printed))
        self.di[self.maze_path]["Length"]=len(path_printed)
        self.di[self.maze_path]["Cost"]=self.calculate_cost()

            
       
if __name__=="__main__":
    
    sim = Problem("problem.txt","mazes")
    # sim.simulate_cost()
    sim.run_50_sim()


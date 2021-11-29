# Search-Algorithms
Intro to Artificial Intelligence

<h3>Search Algorithms</h3>

<table>
  <tr>
    <th>Algorithm</th>
    <th>Summary</th>
    <th>Algorithm</th>
    <th>Environments</th>
  </tr>
  <tr>
    <td>0</td>
    <td>
        It’s completed because it was able to reach the goal on the given 50 environments where 
        the agent was not enclosed in a space where there is no possible way to reach the goal. <br>
        This algorithm is not OPTIMAL because of the cost the agent 
        took to reach the goal, and before discovering another path it had to first exhaust 
        the current path
    </td>
    <td>Breath First Search</td>
    <td>50 tasks</td>
  </tr>
  <tr>
    <td>1</td>
    <td>
        It’s completed because it was able to reach the goal on the given 50 environments where the 
        agent was not enclosed in a space where there is no possible way to reach the goal. <br> 
      	This algorithm is not OPTIMAL because of the cost the agent took to reach the 
        goal, and before discovering another path it had to first exhaust the current path 

    </td>
    <td>Iterative deepening depth-first search </td>
    <td>50 tasks</td>
  </tr>
  <tr>
    <td>2</td>
    <td>
        This algorithm calculated h0 as the Eucliden distance and this heuristic is consistent because 
        it was able to perform the same way the breath first search performed <br>
        This alogrithm is ADMISSIBLE because only the OPTIMAL distance is considered
    </td>
    <td>A* using h0 </td>
    <td>50 tasks</td>
  </tr>
  <tr>
    <td>3</td>
    <td>
        This heuristic is partly consistent because it was able to perform the same as breath frist 
        search on some enviroment. <br>
        This algorithm is ADMISSIBLE partly because on some cases it will choose lower value which 
        is not in the direction of the goal
    </td>
    <td>A* using h3 </td>
    <td>50 tasks</td>
  </tr>
  <tr>
    <td>4</td>
    <td>
        This algorithm clculated h was given by the lowest value either going in y direction to the goal
        or x direction to the goal. <br>
        This heuristic is consistent because it was able to perform with lower cost as breath first search 
        on some environments. <br>
        This algorithm is ADMISSIBLE because the agent can only move up or down and left or right, so the 
        Eucliden distance is very OPTIMAL here.
    </td>
    <td>A* using h custom </td>
    <td>50 tasks</td>
  </tr>
 
</table>



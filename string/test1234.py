# def foo(x):
#     x[0] = ['def']
#     x[1] = ['abc']
#     return id(x)
#
#
# q = ['abc', 'def']
# print(id(q) == foo(q))

# i = 1
# while True:
#     if i%0O7 == 0:
#         break
#     print(i)
#     i += 1
#
# Write a Python program to print all distinct values in a dictionary.
# L =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# out = []
# for dic in L:
#     for value in dic.values():
#         out.append(value)
# output = set(val for dic in L for val in dic.values())
# print (set(output))

# op- "S001"
# "S002"
# "S005"
# S009
# S007


# insert into employee_details values('name',"department",,,"salary");

# select max(salary) from employee where salary < (select max(salary) from employee);
# select salary from employee group by salary order by salary desc limit 1,1;

# 1write tcs to ensurer test that they. don't collide
# consider a 4*4 grid
# 2 robots


# initial position -> (0,0)


# Moving - Upward -- (0,0) --- (0,1)
# MOving - Down  ---(0,1) ---(0,0)
# moving Down - (0,0)  --- (0,-1)
# moving left - (0,-1)  ---(-1,-1)
# moving right -- (-1,-1)   ---(0,-1)
# moving left --(0,-1)  --- (-1,1)

# final ----(-1,-1)

# 1. robots can move simultenousyly
# 2. robots should 1 will stop another one will move in same direction.
# 3. robots shoud 1 will stop another one will move in same direction.

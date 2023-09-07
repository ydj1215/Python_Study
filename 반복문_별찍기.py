"""
[1]
*
**
***
****
*****
"""
# n = int(input("별 개수를 입력해주세요 : "))
# for i in range(n):
#     print("*"*(i+1))

"""
[2]
*****
****
***
**
*
"""
n = int(input())
for i in range(n,0,-1):
    print("*"*i)

"""
[3]
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""
# n = int(input())
#
# for i in range(n, 0, -1):
#     for s in range(0, n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()

"""
[4] 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
n = int(input())

# for i in range(n):
#     for s in range(i):
#         print(" ", end=" ")
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

for i in range(n, 0, -1):
    for j in range(0, n - i):
        print(end=" ")
    print("*" * i)

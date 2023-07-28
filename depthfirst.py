class node():
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.right=right
        self.left=left

#iterative
def ri(root,t=None):
    if not root:return False
    newarray=[] #for printing in array format
    sum=0 #total sum
    minx=float("inf") # infinity boundary

    stack= [root]
    while stack:
        item=stack.pop() 
        newarray.append(item.val)  #for printing in array format
        sum+=item.val #total sum
        minx=min(minx,item.val) #minimum
        if item.val == t:return True

        if item.left:stack.append(item.left)
        if item.right:stack.append(item.right)
    return newarray,sum,minx

#recursive
def ref(root):
    if not root:return 0 #for sum
    # if not root:return float("inf") #for min value
    # if not root:return []  #for array printing

    rl=ref(root.left)
    rr=ref(root.right)
    # return [root.val ,*rl, *rr] #for array
    # return min(root.val , rl,rr) #for min
    return root.val + rl + rr #for sum


a=node(10)
b=node(90)
c=node(30)
d=node(10)
e=node(10)
f=node(1)
a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

# print(ri(a,100))
print(ref(a))


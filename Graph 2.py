# Force-Directed Graph Drawing

import
import random
import math

# d = [
#     [.0, .3, .3, .0],
#     [.3, .0, .3, .0],
#     [.3, .3, .0, .3],
#     [.0, .0, .3, .0]
# ]

d = []

#
# for i in xrange(nrows * ncols):
#     ci = i % ncols
#     ri = i / ncols
#     dr = []
#     for j in xrange(nrows * ncols):
#         cj = j % ncols
#         rj = j / ncols
#         if ((ci == cj) and (ri == rj - 1 or ri == rj + 1)
#             or (ri == rj and (ci == cj - 1 or ci == cj + 1))):
#             dr.append(.1)
#         else:
#             dr.append(.0)
#     d.append(dr)

print "Enter file name you want to read from..."
fname = raw_input()

def graph_input(nodes, edges, lists=[]):
    V = nodes
    E = edges

    adj_matrix = []
    # vertex numbering starts from 0
    for i in range(0, V):
        temp = []
        for j in range(0, V):
            temp.append(0)
        adj_matrix.append(temp)

    for i in range(2, (E * 2 + 2), 2):
        u = lists[i]
        v = lists[i + 1]
        print "i = ", i, "u = ", u, "v= ", v
        # u,v= s.split()
        # u = int(u)
        # v = int(v)
        # w = int(w)
        adj_matrix[v][u] = adj_matrix[u][v] = 1

    print "adjacency matrix is : "
    # print the adjacency matrix
    for i in range(0, V):
        print adj_matrix[i]

    return adj_matrix

with open(fname+".txt") as f:
    lines = f.read().split()

lines = [int(i) for i in lines]

print "pppp"
print lines

nodes = lines[0]
edges = lines[1]

print "no of nodes = ",nodes
print "no of edges = ",edges

d = graph_input(nodes, edges,lines)



# d  = [[0,0.1,0.1,0,0],
#       [0.1,0,0,0,0],
#       [0.1,0,0,0.1,0.1],
#       [0,0,0.1,0,0],
#       [0,0,0.1,0,0]]

# mass
alpha = 1.0
beta = .0001
k = 1.0
#damping
eta = .99
delta_t = .01

m = len(d)

root = Tkinter.Tk()

canvas = Tkinter.Canvas(root, width=2000, height=2000, background="blue")
canvas.pack()

x = []
v = []
ids = []


def move_oval(i):
    newx = int(x[i][0] * 500)
    newy = int(x[i][1] * 500)
    canvas.coords(ids[i], newx - 5, newy - 5, newx + 5, newy + 5)

for i in xrange(m):
    xi = [random.random(), random.random()]
    x.append(xi)
    v.append([0.0, 0.0])
    id = canvas.create_oval(245, 245, 255, 255, fill="red")
    ids.append(id)
    move_oval(i)

lids = []


def move_line(id, xi, xj):
    canvas.coords(id,
                  int(xi[0] * 500),
                  int(xi[1] * 500),
                  int(xj[0] * 500),
                  int(xj[1] * 500))

for i in xrange(m):
    for j in xrange(m):
        if d[i][j] != 0:
            id = canvas.create_line(0, 0, 0, 0)
            lids.append(id)
            move_line(id, x[i], x[j])


def Coulomb_force(xi, xj):
    dx = xj[0] - xi[0]
    dy = xj[1] - xi[1]
    ds2 = dx * dx + dy * dy
    ds = math.sqrt(ds2)
    ds3 = ds2 * ds
    if ds3 == 0.0:
        const = 0
    else:
        const = beta / (ds2 * ds)
    return [-const * dx, -const * dy]


def Hooke_force(xi, xj, dij):
    dx = xj[0] - xi[0]
    dy = xj[1] - xi[1]
    ds = math.sqrt(dx * dx + dy * dy)
    dl = ds - dij
    const = k * dl / ds
    return [const * dx, const * dy]


def move():
    ekint = [0.0, 0.0]
    for i in xrange(m):
        Fx = 0.0
        Fy = 0.0
        for j in xrange(m):
            if j == 1:
                continue
            dij = d[i][j]
            Fij = 0.0
            if dij == 0.0:
                Fij = Coulomb_force(x[i], x[j])
            else:
                Fij = Hooke_force(x[i], x[j], dij)
            Fx += Fij[0]
            Fy += Fij[1]
        v[i][0] = (v[i][0] + alpha * Fx * delta_t) * eta
        v[i][1] = (v[i][1] + alpha * Fy * delta_t) * eta
        ekint[0] = ekint[0] + alpha * (v[i][0] * v[i][0])
        ekint[1] = ekint[1] + alpha * (v[i][1] * v[i][1])

    print ("total kinetic energy: %lf" % math.sqrt(ekint[0] * ekint[0] + ekint[1] * ekint[1]))

    for i in range(m):
        x[i][0] += v[i][0] * delta_t
        x[i][1] += v[i][1] * delta_t
        move_oval(i)

    li = 0
    for i in range(m):
        for j in range(m):
            if d[i][j] != 0:
                id = lids[li]
                move_line(id, x[i], x[j])
                li += 1

    root.after(1, move)

root.after(1, move)

root.mainloop()
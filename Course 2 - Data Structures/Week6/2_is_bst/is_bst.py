#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def get_vertex(tree, idx):
    return tree[idx]
def get_key(vertex):
    return vertex[0]
def get_left(vertex):
    return vertex[1]
def get_right(vertex):
    return vertex[2]

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if tree == []:
      return True
  idx = 0
  result = []
  def recur(idx):
      nonlocal result
      v = get_vertex(tree, idx)
      if get_left(v) != -1 and get_right(v) != -1:
          recur(get_left(v))
          result += [get_key(v)]
          recur(get_right(v))
      elif get_left(v) != -1:
          recur(get_left(v))
          result += [get_key(v)]
      elif get_right(v) != -1:
          result += [get_key(v)]
          recur(get_right(v))
      else:
          result += [get_key(v)]
  recur(0)
  bigger = result[0]
  for e in result[1:]:
      if e < bigger:
          return False
      bigger = e

  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

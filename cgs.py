def norm2(M: np.array):
  M = M**2
  return np.sqrt(M.sum(axis=0))

# cgs
def cgs(A):
  """
    Q,R = cgs(A)
    Apply classical Gram-Schmidt to mxn rectangular/square matrix. 

    Parameters
    -------
    A: mxn rectangular/square matrix   

    Returns
    -------
    Q: mxn square matrix
    R: nxn upper triangular matrix

  """

  # ADD YOUR CODES
  m=len(A)# get the number of rows of A
  n=len(A[0]) # get the number of columns of A
  R= np.zeros((n,n)) # create a zero matrix of nxn
  Q= np.ones(A.shape) # copy A (deep copy)

  for i in range(0, len(A[0])):
    w = A[:, i]
    sum = np.zeros(len(w))
    for q in range(0, i):
      R[q,i]= np.dot(w , Q[:, q])
      sum += (w * Q[:, q]) * Q[:, q]
    qVal= w - sum
    if norm2(qVal) ==0:
      Q[:,i]= qVal
    else:
      R[i,i]= norm2(qVal)
      qVal /= R[i,i]

    Q[:,i]= qVal


  return Q, R


arr = np.array(
    [[1,2,4],
     [0,0,5],
     [0,3,6]])
Q, R = cgs(arr)

print(Q)
print("\n\n\n")
print(R)
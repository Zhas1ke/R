N_round = 0
N = 0

for (i in 1:100000000){
  point <- runif(2, min=-1, max=1);
  x <- point[c(0,1)]
  y <- point[c(0,2)]
  N = N + 1
  if (x*x + y*y <= 1) {
    N_round = N_round + 1
  }
  if (!N %% 1000000){
    print (N_round*4/N)
    print ((N_round*4/N) - pi)
  }
}
print (N_round*4/N)
print ((N_round*4/N) - pi)
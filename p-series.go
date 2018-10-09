package main

import ( "fmt"
	 "math"
 )

func main(){
var(
     k float64 =1
     p float64 =1.1
     ps float64
     ran int
)
  fmt.Println("range")
  fmt.Scan(&ran)
  fmt.Println("exponent")
  fmt.Scan(&p)
  fmt.Println("P-Series")
  for count :=0; count< ran; count++{
    ps = 1/math.Pow(k,p)
    fmt.Println(ps)
    k += 1
    }
}

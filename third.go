package main

import ( 
    "fmt"
    "strings"
    "unicode/utf8"
)
    
func main() {
    var a string

    a = "1.345.679"
	a = strings.Replace(a,".","",-1)
	a = strings.Replace(a,",","",-1)
    b := utf8.RuneCountInString(a)
    c := b-1
    
    for i := 0; i < b; i++ {
		fmt.Print(string(a[i]))

		for j :=0;j<c;j++ {
	   		fmt.Print("0")
		}
		fmt.Print("\n")
		c -=1
    }
}
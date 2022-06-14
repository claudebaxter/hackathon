package main

import (
	"fmt"
	"github.com/algorand/go-algorand-sdk/crypto"
)


func main() {
	appID := 95223182
	actual := crypto.GetApplicationAddress(uint64 (appID))
	fmt.Printf("Application Address: %s\n", actual)
}
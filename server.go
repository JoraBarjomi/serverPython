package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"strings"
)

func main() {
	ln, err := net.Listen("tcp", ":12345")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Server running...")
	conn, err := ln.Accept()
	if err != nil {
		log.Fatal(err)
	}
	for {
		msg, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println("Client send: ", string(msg))
		newmsg := strings.ToUpper(msg)
		conn.Write([]byte(newmsg + "\n"))
	}
}

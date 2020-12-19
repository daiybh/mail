package main

import (
	"fmt"
	"log"
	"strings"

	"github.com/emersion/go-sasl"
	"github.com/emersion/go-smtp"
)

func ExampleSendMail() {
	log.Print("start")
	// Set up authentication information.
	auth := sasl.NewPlainClient("", "13348926569@189.cn", "PWD")

	// Connect to the server, authenticate, set the sender and recipient,
	// and send the email all in one step.
	to := []string{"daiybh@qq.com"}
	msg := strings.NewReader("To: daiybh@qq.com\r\n" +
		"Subject: discount Gophers!\r\n" +
		"\r\n" +
		"This is the email body.\r\n")
	err := smtp.SendMail("smtp.189.cn:25", auth, "13348926569@189.cn", to, msg)
	if err != nil {
		log.Fatal(err)
	}
	log.Print("done")
}
func main() {
	ExampleSendMail()
	return
	// Connect to the remote SMTP server.
	c, err := smtp.Dial("localhost:31025")
	if err != nil {
		log.Fatal(err)
	}
	c.Hello("HELLO")

	// Set the sender and recipient first
	if err := c.Mail("daiybh@qq.com", nil); err != nil {
		log.Fatal(err)
	}
	if err := c.Rcpt("daiybh@qq.com"); err != nil {
		log.Fatal(err)
	}

	// Send the email body.
	wc, err := c.Data()
	if err != nil {
		log.Fatal(err)
	}
	_, err = fmt.Fprintf(wc, "This is the email body")
	if err != nil {
		log.Fatal(err)
	}
	err = wc.Close()
	if err != nil {
		log.Fatal(err)
	}

	// Send the QUIT command and close the connection.
	err = c.Quit()
	if err != nil {
		log.Fatal(err)
	}
}

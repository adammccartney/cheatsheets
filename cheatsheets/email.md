# Some info about Email protocols

## SMTP commands

- HELO
- MAIL FROM
- RCPT TO
- DATA
- CRLF.CRLF
- QUIT

SMTP servers are usually looking to communicate over an encrypted connection

While it is possible to use `telnet <server> 25` to start a dialogue, this only
gets you as far as `enter STARTTLS` request.

Found one alternative on stack overflow:
`openssl s_client -starttls smtp -crlf -connect <server>:25`
